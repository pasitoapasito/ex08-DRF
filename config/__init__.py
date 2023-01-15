import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()


from core.utils.migrate import MigrateParticapant


res = MigrateParticapant.data_migrate()
if res:
    print(res)
