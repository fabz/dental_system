#!/usr/bin/symlink/python-ce-logistic
import os
import sys
running_mode = sys.argv[1]

# LOCAL
if running_mode == 'local':
    django_settings_module_string = 'dental_system.settings.local'
    mode = 'local'
# DEVELOPMENT
elif running_mode == 'dev':
    django_settings_module_string = 'dental_system.settings.dev'
    mode = 'dev'
# PRODUCTION
elif running_mode == 'production':
    django_settings_module_string = 'dental_system.settings.production'
    mode = 'production'
else:
    raise Exception('MODE NOT SUPPORTED')

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module_string)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.utils import timezone
import traceback


def execute(func_list, report_filename):
    for func in func_list:
        try:
            func()
        except:
            with open('data/results/{}'.format(report_filename), 'a') as file_to_write:
                file_to_write.write(
                    '{}\n{}\n\n\n'.format(timezone.now().strftime('%Y-%m-%d %H:%M:%S'), traceback.format_exc()))
