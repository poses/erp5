##############################################################################
#
# Copyright (c) 2002-2003 Nexedi SARL and Contributors. All Rights Reserved.
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

from Base import func_code, type_definition, list_types, ATTRIBUTE_PREFIX, Method
from TypeDefinition import asList, identity
import Base

from Products.CMFCore.Expression import Expression
from Products.ERP5Type.Utils import createExpressionContext
from Products.ERP5Type.Cache import CachingMethod

from zLOG import LOG

class DefaultSetter(Method):
    """
      Sets the default attribute in a list
    """
    _need__name__=1

    # Generic Definition of Method Object
    # This is required to call the method form the Web
    # More information at http://www.zope.org/Members/htrd/howto/FunctionTemplate
    func_code = func_code()
    func_code.co_varnames = ('self','value')
    func_code.co_argcount = 2
    func_defaults = ()

    def __init__(self, id, key, property_type, reindex=1, storage_id=None):
      self._id = id
      self.__name__ = id
      self._key = key
      self._reindex = reindex
      self._property_type = property_type
      if property_type in list_types: # classic list
        self._cast = type_definition[property_type]['cast']
        self._item_cast = identity
      else: # Multivalued
        self._cast = asList
        self._item_cast = type_definition[property_type]['cast']
      self._null = type_definition[property_type]['null']
      if storage_id is None:
        storage_id = "%s%s" % (ATTRIBUTE_PREFIX, key)
      self._storage_id = storage_id
      self._is_tales_type = (property_type == 'tales')

    def __call__(self, instance, *args, **kw):
      # Turn the value into a list
      value = args[0]
      if not self._reindex:
        # Modify the property
        if self._is_tales_type:
          if value in self._null:
            value = None
          setattr(instance, self._storage_id, value)
        elif value in self._null:
          # The value has no default property -> it is empty
          setattr(instance, self._storage_id, ())
        else:
          value = self._cast(args[0])
          if self._item_cast is not identity:
            value = map(self._item_cast, value)
          if len(value) > 0:
            default_value = value[0]
            list_value = getattr(instance, self._storage_id, None)
            if list_value is None: list_value = []
            new_list_value = [default_value]
            keep_value = 0
            for k in list_value:
              # Only delete the first occurence if exists
              if keep_value or k is not default_value:
                new_list_value += [k]
                keep_value = 1
          else:
            # The list has no default property -> it is empty
            new_list_value = []
          setattr(instance, self._storage_id, tuple(new_list_value))
      else:
        # Call the private setter
        method = getattr(instance, '_' + self._id)
        method(*args, **kw)
      if self._reindex: instance.reindexObject()

class Setter(DefaultSetter):

    def __call__(self, instance, *args, **kw):
      value = args[0]
      if not self._reindex:
        # Modify the property
        if value in self._null:
          setattr(instance, self._storage_id, None)
        elif self._is_tales_type:
          setattr(instance, self._storage_id, str(value))
        else:
          value = self._cast(args[0])
          if self._item_cast is not identity:
            value = map(self._item_cast, value)
          setattr(instance, self._storage_id, tuple(value))
      else:
        # Call the private setter
        method = getattr(instance, '_' + self._id)
        method(*args, **kw)
      if self._reindex: instance.reindexObject()

ListSetter = Setter


class SetSetter(Method):
    """
      Sets the default attribute in a list
    """
    _need__name__=1

    # Generic Definition of Method Object
    # This is required to call the method form the Web
    # More information at http://www.zope.org/Members/htrd/howto/FunctionTemplate
    func_code = func_code()
    func_code.co_varnames = ('self','value')
    func_code.co_argcount = 2
    func_defaults = ()

    def __init__(self, id, key, property_type, reindex=1, storage_id=None):
      self._id = id
      self.__name__ = id
      self._key = key
      self._reindex = reindex
      self._property_type = property_type
      if property_type in list_types: # classic list
        self._cast = type_definition[property_type]['cast']
        self._item_cast = identity
      else: # Multivalued
        self._cast = asList
        self._item_cast = type_definition[property_type]['cast']
      self._null = type_definition[property_type]['null']
      if storage_id is None:
        storage_id = "%s%s" % (ATTRIBUTE_PREFIX, key)
      self._storage_id = storage_id
      self._is_tales_type = (property_type == 'tales')

    def __call__(self, instance, *args, **kw):
      # Turn the value into a list
      value = args[0]
      if not self._reindex:
        # Modify the property
        if self._is_tales_type:
          if value in self._null:
            value = None
          setattr(instance, self._storage_id, value)
        elif value in self._null:
          # The value has no default property -> it is empty
          setattr(instance, self._storage_id, ())
        else:
          value = self._cast(args[0])
          if self._item_cast is not identity:
            value = map(self._item_cast, value)
          if len(value) > 0:
            list_value = getattr(instance, self._storage_id, None)
            if list_value is None: list_value = []
            if len(list_value) > 0:
              my_dict = {}
              default_value = list_value[0]
              for v in value:
                my_dict[v] = 0
              if my_dict.has_key(default_value):
                del my_dict[default_value]
              # If we change the set, the default value must be in the new set
              if default_value in value:
                new_list_value = [default_value] + my_dict.keys()
              else:
                new_list_value = my_dict.keys()
            else:
              new_list_value = value
          else:
            # The list has no default property -> it is empty
            new_list_value = []
          setattr(instance, self._storage_id, tuple(new_list_value))
      else:
        # Call the private setter
        method = getattr(instance, '_' + self._id)
        method(*args, **kw)
      if self._reindex: instance.reindexObject()


def _evaluateTales(instance=None, value=None):
  expression = Expression(value)
  econtext = createExpressionContext(instance)
  return expression(econtext)

evaluateTales = CachingMethod(_evaluateTales, id = 'evaluateTales', cache_duration=300)

class DefaultGetter(Method):
    """
      Gets the first item of a list
    """
    _need__name__=1

    # Generic Definition of Method Object
    # This is required to call the method form the Web
    func_code = func_code()
    func_code.co_varnames = ('self',)
    func_code.co_argcount = 1
    func_defaults = ()

    def __init__(self, id, key, property_type, default_value = None, storage_id=None):
      self._id = id
      self.__name__ = id
      self._key = key
      self._type = property_type
      self._null = type_definition[property_type]['null']
      self._default = default_value
      if storage_id is None:
        storage_id = "%s%s" % (ATTRIBUTE_PREFIX, key)
      self._storage_id = storage_id
      self._is_tales_type = (property_type == 'tales')

    def __call__(self, instance, *args, **kw):
      if len(args) > 0:
        default = args[0]
      else:
        default = self._default
      list_value = getattr(instance, self._storage_id, None)
      if list_value is not None:
        if self._is_tales_type:
          if kw.get('evaluate', 1):
            list_value = evaluateTales(instance=instance, value=list_value)
          else:
            return list_value
        if len(list_value) > 0:
          return list_value[0]
      return default

Getter = DefaultGetter

class ListGetter(Method):
    """
      Gets an attribute value. A default value can be
      provided if needed
    """
    _need__name__=1

    # Generic Definition of Method Object
    # This is required to call the method form the Web
    func_code = func_code()
    func_code.co_varnames = ('self',)
    func_code.co_argcount = 1
    func_defaults = ()

    def __init__(self, id, key, property_type, default_value=None, storage_id=None):
      self._id = id
      self.__name__ = id
      self._key = key
      self._type = property_type
      self._null = type_definition[property_type]['null']
      self._default = default_value
      if storage_id is None:
        storage_id = "%s%s" % (ATTRIBUTE_PREFIX, key)
      self._storage_id = storage_id
      self._is_tales_type = (property_type == 'tales')

    def __call__(self, instance, *args, **kw):
      if len(args) > 0:
        default = args[0]
      else:
        default = self._default
      list_value = getattr(instance, self._storage_id, None)
      # We should not use here self._null but None instead XXX
      if list_value not in self._null:
        if self._is_tales_type:
          if kw.get('evaluate', 1):
            list_value = evaluateTales(instance=instance, value=list_value)
          else:
            return list_value
        return list(list_value)
      return default

SetGetter = ListGetter

Tester = Base.Tester
