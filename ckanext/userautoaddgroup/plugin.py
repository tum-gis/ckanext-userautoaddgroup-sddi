import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.userautoaddgroup.logic.action.create


class UserautoaddgroupPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    
    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'userautoaddgroup')

    # IActions
    def get_actions(self):
        return {
            'user_create':
            ckanext.userautoaddgroup.logic.action.create.user_create,
        }
