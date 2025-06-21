# Импортируем Celery-приложение, чтобы оно инициализировалось при запуске Django
from .celery import app as celery_app

# Необходимо для совместимости с Django и Celery
__all__ = ('celery_app',)