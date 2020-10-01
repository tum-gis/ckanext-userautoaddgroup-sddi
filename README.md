# ckanext-grouphierarchy - group hierarchy for CKAN

This CKAN extension is intended to be used in combination with the [SDDI CKAN Docker container](https://github.com/tum-gis/SDDI-CKAN-Docker).

## Overview

New users are added automatically to the parent groups, which allows them to create datasets linked to these groups.
Alls children groups are inherited from the parent groups.

Forms (hierachy_form plugin):
* /group/new
* /group/edit/{id}

Templates (hierarchy_display plugin):
* /group - now shows the group hierarchy instead of list
* /group/about/{id} - now also shows the relevant part of the hierarchy

Snippets (used by hierarchy_display and ckanext-scheming):
* /scheming/form_snippets/group_hierarchy.html

You can use this extension with CKAN as it is, enabling both plugins. Or if you
use an extension to customise the form already with an IGroupForm, then you
will want to only use the hierarchy_display plugin, and copy bits of the
hierarchy_form into your own. If you have your own templates then you can use
the snippets (or logic functions) that this extension provides to display the
trees.


## Compatibility

This extension has been tested with CKAN v2.8.0 or later. 

## Installation

Install the extension in your python environment
```
$ . /usr/lib/ckan/default/bin/activate
(pyenv) $ cd /usr/lib/ckan/default/src
(pyenv) $ pip install -e "git+https://tum-gis/ckanext-guserautoaddgroup-sddi.git#egg=ckanext-userautoaddgroup-sddi"
```
Then change your CKAN ini file (e.g. development.ini or production.ini)
```
ckan.plugins = stats text_view recline_view ... userautoaddgroup
```

If you do not use the [grouphierarchy extension](https://github.com/tum-gis/ckanext-grouphierarchy-sddi), you need to adjust the production.ini file.
```
ckan.userautoaddgroup.group_name_1 = main-categories
ckan.userautoaddgroup.group_name_2 = topics
```

## Copyright & Licence

This module is Crown Copyright 2013 and openly licensed with AGPLv3 - see LICENSE file.
