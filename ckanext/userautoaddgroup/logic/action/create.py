#import pylons.config as config
from ckan.common import config

import ckan.logic as logic
from ckan.logic.action.create import user_create as ckan_user_create
import ckan.plugins.toolkit as toolkit

#@toolkit.chained_action
def user_create(context, data_dict):
    user = ckan_user_create(context, data_dict)

    org_name_1 = config.get('ckan.userautoaddgroup.group_name_1', '')
    org_name_2 = config.get('ckan.userautoaddgroup.group_name_2', '')
    org_name_3 = config.get('ckan.userautoaddgroup.group_name_3', '')
    role = config.get('ckan.userautoaddgroup.group_role', '')
    admin = config.get('ckan.userautoaddgroup.admin_username', '')


    try:
        toolkit.get_action('group_show')(
            context, {
                'id': org_name_1,
            }
        )
    except logic.NotFound:    
        return user

    try:
        toolkit.get_action('group_show')(
            context, {
                'id': org_name_2,
            }
        )
    except logic.NotFound:    
        return user

    try:
        toolkit.get_action('group_show')(
            context, {
                'id': org_name_3,
            }
        )
    except logic.NotFound:    
        return user
        

    toolkit.get_action('group_member_create')(
        {'user': admin}, {
            'id': org_name_1,
            'username': user['name'],
            'role': role,
        }
        )
    toolkit.get_action('group_member_create')(
        {'user': admin}, {
            'id': org_name_2,
            'username': user['name'],
            'role': role,
        }
        )
    toolkit.get_action('group_member_create')(
        {'user': admin}, {
            'id': org_name_3,
            'username': user['name'],
            'role': role,
        }        
    )
    return user