##############################################################################
#
# Copyright (c) 2006 Nexedi SARL and Contributors. All Rights Reserved.
#                    Ivan Tyagov <ivan@nexedi.com>
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
from Products.ERP5Type import Permissions, PropertySheet, interfaces
from Products.ERP5Type.XMLObject import XMLObject
from Products.ERP5Configurator.mixin.configurator_item import ConfiguratorItemMixin
from Products.ERP5Type.Cache import CachingMethod
from zLOG import LOG, INFO

class StandardBT5ConfiguratorItem(ConfiguratorItemMixin, XMLObject):
  """ This class will install standard ERP5 template from a repository to
  fake site. """

  meta_type = 'ERP5 Standard BT5 Configurator Item'
  portal_type = 'Standard BT5 Configurator Item'
  add_permission = Permissions.AddPortalContent
  isPortalContent = 1
  isRADContent = 1

  # Declarative security
  security = ClassSecurityInfo()
  security.declareObjectProtected(Permissions.AccessContentsInformation)

  # Declarative interfaces
  zope.interface.implements(interfaces.IConfiguratorItem)

  # Declarative properties
  property_sheets = ( PropertySheet.Base
                    , PropertySheet.XMLObject
                    , PropertySheet.CategoryCore
                    , PropertySheet.DublinCore
                    , PropertySheet.StandardBT5ConfiguratorItem
                    )

  def _build(self, business_configuration):
    template_tool = self.getPortalObject().portal_templates
    installed_bt5_list = template_tool.getInstalledBusinessTemplateTitleList()
    bt5_id_list = []
    bt5_id_list_append = bt5_id_list.append
    for bt5_id in self.getBt5IdList():
      if bt5_id in installed_bt5_list:
        continue
      bt5_id_list_append(bt5_id)
    if not bt5_id_list:
      return "Everything already Installed"
    template_tool.upgradeSite(bt5_id_list, dry_run=0)
    return '%s Installed' % ','.join(bt5_id_list)
