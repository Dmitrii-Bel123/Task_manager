# task_manager_project/celery.py

import os
from celery import Celery

# Устанавливаем настройки Django для приложения Celery
# Это необходимо, чтобы Celery мог получать доступ к настройкам Django, таким как DATABASES, SECRET_KEY и т.д.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_main.settings')

# Создаем экземпляр Celery-приложения
# 'task_manager_project' - это имя вашего проекта, которое используется как префикс для всех задач
app = Celery('crm_main')

# Загружаем настройки из файла settings.py Django
# Пространство имен 'CELERY' означает, что все настройки Celery должны начинаться с префикса CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем и регистрируем задачи из всех файлов tasks.py в INSTALLED_APPS
app.autodiscover_tasks()

# Опционально: task_manager_project - это имя для отладки, отображается в логах
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')