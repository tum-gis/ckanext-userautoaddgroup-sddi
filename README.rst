===================
ckanext-userautoaddgroup
===================

CKAN plugin to add new users to top(parent) groups automatically.

This plugin implements the ``user_create`` action to add users to an existing
parent group with a given role (both specified in the configuration - See Config
Settings below).

This code is adjusted from:
´´https://github.com/aptivate/ckanext-userautoadd´´

------------
Requirements
------------

Tested with CKAN v2.9

------------
Installation
------------


To install ckanext-userautoadd:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-userautoadd Python package into your virtual environment::

     pip install ckanext-userautoaddgroup

3. Add ``userautoaddgroup`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

::

    # The organization to which new users are added
    ckan.userautoaddgroup.group_name_1 = [name1]
    ckan.userautoaddgroup.group_name_2 = [name2]
    ckan.userautoaddgroup.group_name_3 = [name3]

    # The role the new users will have
    ckan.userautoaddgroup.group_role = [editor / admin]
    
    # The name of the admin
    ckan.userautoaddgroup.admin_username = [admin user name]



-----------
Background
-----------
This code is inspired by the "ckanext-userautoadd":
https://github.com/aptivate/ckanext-userautoadd

-----------
License
-----------
This ckan extension is available as free and open source and is licensed under the terms of the GNU Affero General Public License, version 3, as published by the Free Software Foundation. 
