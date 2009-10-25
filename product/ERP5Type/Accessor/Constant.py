# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2007 Nexedi SA and Contributors. All Rights Reserved.
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

from Accessor import Accessor

# Creation of default constructor
class func_code: pass

class Getter(Accessor):
  """
  Returns a constant value, either by method call
  or through type cast (ex. boolean, int, float).
  This method can be useful to turn existing constant
  properties of classes into methods, yet retaining 
  compatibility.

  TODO:
  - make unit test
  """
  _need__name__=1

  # Generic Definition of Method Object
  # This is required to call the method form the Web
  # More information at http://www.zope.org/Members/htrd/howto/FunctionTemplate
  func_code = func_code()
  func_code.co_varnames = ('self', )
  func_code.co_argcount = 1
  func_defaults = ()

  def __init__(self, id, accessor_id, value):
    self._id = id
    self.__name__ = id
    self._accessor_id = accessor_id
    self.value = value

  def __call__(self, instance):
    return self.value

  def __nonzero__(self):
    return bool(self.value)

  def __int__(self):
    return int(self.value)

  def __float__(self):
    return float(self.value)
