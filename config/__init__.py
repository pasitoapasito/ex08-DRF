import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()


from core.utils.migrate import MigrateParticipant

res = MigrateParticipant.data_migrate()
if res:
    print(res)
