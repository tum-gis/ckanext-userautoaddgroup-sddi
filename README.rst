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

Tested with CKAN v2.8.0

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
    ckan.userautoaddgroup.group_name_1 = main-categories
    ckan.userautoaddgroup.group_name_2 = agricultural-research-stations
    ckan.userautoaddgroup.group_name_3 = themes

    # The role the new users will have
    ckan.userautoaddgroup.group_role = editor



-----
About
-----
This code is an adaptation of following programers:

Copyright (c) 2016 `MapAction <http://mapaction.org>`_. Developed by `Aptivate <http://aptivate.org>`_.

Development of v1 of this plugin was funded by `ECHO <http://ec.europa.eu/echo>`_.

.. image:: http://www.echo-visibility.eu/wp-content/uploads/2014/02/EU_Flag_HA_2016_EN-300x272.png
   :alt: "Funded by European Union Humanitarian Aid"
