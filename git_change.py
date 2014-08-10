#!/usr/bin/python
import subprocess

def inplace_change(filename, old_string, new_string):
        s=open(filename).read()
        if old_string in s:
                print 'Changing "{old_string}" to "{new_string}"'.format(**locals())
                s=s.replace(old_string, new_string)
                f=open(filename, 'w')
                f.write(s)
                f.flush()
                f.close()
        else:
                print 'No occurances of "{old_string}" found.'.format(**locals())

print "********fvcom change**********"
# urls.py
inplace_change('./sci-wms/sciwms/urls.py',
               '''url(r'^$', 'sciwms.apps.wms.views.index', name="index"),''',
               '''url(r'^$', include('fvcom.urls')),''')

# setting.py
inplace_change('./sci-wms/sciwms/settings/defaults.py',
"""    'south'
)""",
"""    'south',
    'djcelery',
    'fvcom'
)""")
inplace_change('./sci-wms/sciwms/settings/defaults.py',
               "'django.contrib.admin',",
 """#'django_admin_bootstrapped',
    'django.contrib.admin',"""
)
inplace_change('./sci-wms/sciwms/settings/defaults.py',
"""TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
)""",
"""TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), "templates")),
    os.path.abspath(os.path.join(PROJECT_ROOT,"fvcom/templates")) 
)""")
inplace_change('./sci-wms/sciwms/settings/defaults.py',
"""STATICFILES_DIRS = (
    COMMON_STATIC_FILES,
)""",
"""STATICFILES_DIRS = (
    COMMON_STATIC_FILES,
    os.path.abspath(os.path.join(PROJECT_ROOT,"fvcom/static"))
)""")
print "******************************"
