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
inplace_change('./sci-wms/sciwms/urls.py',
               '''url(r'^$', 'sciwms.apps.wms.views.index', name="index"),''',
               '')
inplace_change('./sci-wms/sciwms/settings/defaults.py',
               "'south'",
 """'south',
    'celery',
    'test',""")
print "******************************"
