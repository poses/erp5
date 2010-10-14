##############################################################################
#
# Copyright (c) 2002 Nexedi SARL and Contributors. All Rights Reserved.
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

from Products.CMFCore.Expression import Expression

class Arrow:
    """
        Properties which allow to define a generic Arrow. Arrows are
        used by Path and Movements to define a source and a destination
        with attributes (payment, decision, etc.) which allow to qualify
        a movement
    """

    _properties = (
        # Source reference
        {   'id'          : 'source_relative_url',
            'description' : 'The titles of the destination of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        {   'id'          : 'source_person_title',
            'description' : 'The title of the source person of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source',),
            'acquisition_portal_type'       : ('Person'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'r' },
        {   'id'          : 'source_organisation_title',
            'description' : 'The title of the source organisation of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source',),
            'acquisition_portal_type'       : ('Organisation'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'r' },
        # Destination reference
        {   'id'          : 'destination_relative_url',
            'description' : 'The titles of the destination of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        {   'id'          : 'destination_person_title',
            'description' : 'The title of the destination person of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination',),
            'acquisition_portal_type'       : ('Person'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'r' },
        {   'id'          : 'destination_organisation_title',
            'description' : 'The title of the destination organisation of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination',),
            'acquisition_portal_type'       : ('Organisation'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'r' },
        # Source decision reference
        {   'id'          : 'source_decision_relative_url',
            'description' : 'The titles of the source decision of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_decision',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination decision reference
        {   'id'          : 'destination_decision_relative_url',
            'description' : 'The titles of the destination decision of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_decision',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source section reference
        {   'id'          : 'source_section_relative_url',
            'description' : 'The titles of the source section of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_section',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination section reference
        {   'id'          : 'destination_section_relative_url',
            'description' : 'The titles of the destination section of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_section',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source administration reference
        {   'id'          : 'source_administration_relative_url',
            'description' : 'The titles of the source administration of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_administration',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination administration reference
        {   'id'          : 'destination_administration_relative_url',
            'description' : 'The titles of the destination administration of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_administration',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source payment reference
        {   'id'          : 'source_payment_relative_url',
            'description' : 'The titles of the source payment of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_payment',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination payment reference
        {   'id'          : 'destination_payment_relative_url',
            'description' : 'The titles of the destination payment of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_payment',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # more properties to make the difference between person and organisation
        {   'id'          : 'destination_decision_person_title',
            'description' : 'The title of the destination decision person of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_decision',),
            'acquisition_portal_type'       : 'Person',
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        {   'id'          : 'destination_decision_organisation_title',
            'description' : 'The title of the destination decision organisation of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_decision',),
            'acquisition_portal_type'       : 'Organisation',
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        {   'id'          : 'destination_administration_person_title',
            'description' : 'The title of the destination administration person of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_administration',),
            'acquisition_portal_type'       : 'Person',
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        {   'id'          : 'destination_administration_organisation_title',
            'description' : 'The title of the destination administration organisation of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_administration',),
            'acquisition_portal_type'       : 'Organisation',
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getTitle',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source trade reference
        {   'id'          : 'source_trade_relative_url',
            'description' : 'The titles of the source trade of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_trade',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination trade reference
        {   'id'          : 'destination_trade_relative_url',
            'description' : 'The titles of the destination trade of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_trade',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source project reference
        {   'id'          : 'source_project_relative_url',
            'description' : 'The titles of the source project of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_project',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalProjectTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination project reference
        {   'id'          : 'destination_project_relative_url',
            'description' : 'The titles of the destination project of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_project',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalProjectTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source function reference
        {   'id'          : 'source_function_relative_url',
            'description' : 'The titles of the source function of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_function',),
            'acquisition_portal_type'       : ('Category',),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination function reference
        {   'id'          : 'destination_function_relative_url',
            'description' : 'The titles of the destination function of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_function',),
            'acquisition_portal_type'       : ('Category',),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source transport reference
        {   'id'          : 'source_transport_relative_url',
            'description' : 'The titles of the source transport of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_transport',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalOrderTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination transport reference
        {   'id'          : 'destination_transport_relative_url',
            'description' : 'The titles of the destination transport of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_transport',),
            'acquisition_portal_type'       : Expression('python: portal.getPortalOrderTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Source advice, use for the consultant who helps taking the decision
        {   'id'          : 'source_advice_relative_url',
            'description' : 'The titles of the source advice of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('source_advice',),
            'acquisition_portal_type'       : Expression('python: \
                                                portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
        # Destination advice
        {   'id'          : 'destination_advice_relative_url',
            'description' : 'The titles of the destination advice of this movement',
            'type'        : 'string',
            'acquisition_base_category'     : ('destination_advice',),
            'acquisition_portal_type'       : Expression('python: \
                                                portal.getPortalNodeTypeList()'),
            'acquisition_copy_value'        : 0,
            'acquisition_accessor_id'       : 'getRelativeUrl',
            'acquisition_depends'           : None,
            'mode'        : 'w' },
   )

    _categories = ( 'source', 'destination',
                    'source_section', 'destination_section',
                    'source_decision', 'destination_decision',
                    'source_administration', 'destination_administration',
                    'source_payment', 'destination_payment',
                    'source_trade', 'destination_trade',
                    'source_function', 'destination_function',
                    'source_project', 'destination_project',
                    'source_carrier', 'destination_carrier',
                    'source_referral', 'destination_referral',
                    'source_account', 'destination_account',
                    #'source_advice', 'destination_advice',
                    #'source_transport', 'destination_transport',
                    # Virtual categories
                    'source_region', 'destination_region',
                    'source_payment_region', 'destination_payment_region',
                    )
