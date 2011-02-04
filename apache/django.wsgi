import os
import sys
import site

BASE_PATH = os.path.join(os.path.dirname(__file__), '..', '..')
vepath= os.path.join(BASE_PATH, 'env', 'lib', 'python2.%d' % sys.version_info[1], 'site-packages')

prev_sys_path = list(sys.path)
# add the site-packages of our virtualenv as a site dir
site.addsitedir(vepath)
# add the app's directory to the PYTHONPATH
sys.path.append(os.path.join(BASE_PATH, 'django-srd20'))

new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

print vepath
print sys.path

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

