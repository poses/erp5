# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 Nexedi SA and Contributors. All Rights Reserved.
#                    Jean-Paul Smets-Solanes <jp@nexedi.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

import zope.interface
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName
from Products.ERP5Type import Permissions, PropertySheet, interfaces
from Products.ERP5Type.XMLObject import XMLObject
from Products.ERP5.mixin.solver import SolverMixin
from Products.ERP5.mixin.configurable import ConfigurableMixin

class QuantitySplitSolver(SolverMixin, ConfigurableMixin, XMLObject):
  """
  QUESTION: is a solver a process ? (ie. subprocess of Solver Process)
  """
  meta_type = 'ERP5 Quantity Split Solver'
  portal_type = 'Quantity Split Solver'
  add_permission = Permissions.AddPortalContent
  isIndexable = 0 # We do not want to fill the catalog with objects on which we need no reporting

  # Declarative security
  security = ClassSecurityInfo()
  security.declareObjectProtected(Permissions.AccessContentsInformation)

  # Default Properties
  property_sheets = ( PropertySheet.Base
                    , PropertySheet.XMLObject
                    , PropertySheet.CategoryCore
                    , PropertySheet.DublinCore
                    , PropertySheet.Arrow
                    , PropertySheet.TargetSolver
                    )
  # Declarative interfaces
  zope.interface.implements(interfaces.ISolver,
                            interfaces.IConfigurable,
                           )

  # ISolver Implementation
  def solve(self):
    """
    """    
    for delivery_line in self.getDeliveryValueList(): 
      decision_quantity = delivery_line.getQuantity()
      simulation_movement_list = delivery_line.getDeliveryRelatedValueList()
      configuration_dict = self.getConfigurationPropertyDict()
      delivery_solver = self.portal_solvers.newDeliverySolver(
        configuration_dict['delivery_solver'], simulation_movement_list)
      # Update the quantity using delivery solver algorithm
      split_list = delivery_solver.setTotalQuantity(decision_quantity)
      # Create split movements
      for (simulation_movement, split_quantity) in split_list:
        new_movement = simulation_movement.Base_createCloneDocument(
          batch_mode=True) # Copy at same level
        new_movement._setDelivery(None)
        new_movement._setQuantity(split_quantity)
        start_date = configuration_dict.get('start_date', None)
        if start_date is not None:
          new_movement._setStartDate(start_date)
        stop_date = configuration_dict.get('stop_date', None)
        if stop_date is not None:
          new_movement._setStopDate(stop_date)
