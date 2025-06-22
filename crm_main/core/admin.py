
from django.contrib import admin
from .models import Project, Task, Comment, Attachment

# Регистрация модели Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'owner__username')
    # Добавление фильтра для участников (members)
    filter_horizontal = ('members',) # Это удобный виджет для ManyToManyField в админке

# Регистрация модели Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'reporter', 'status', 'priority', 'due_date', 'created_at')
    list_filter = ('status', 'priority', 'project', 'assigned_to', 'reporter', 'created_at', 'due_date')
    search_fields = ('title', 'description', 'project__title', 'assigned_to__username', 'reporter__username')
    raw_id_fields = ('project', 'assigned_to', 'reporter',) # Для больших проектов, удобно искать по ID

# Регистрация модели Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'created_at', 'content_preview')
    list_filter = ('created_at', 'author', 'task')
    search_fields = ('content', 'task__title', 'author__username')

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Содержимое' # Название колонки в админке

# Регистрация модели Attachment
@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file', 'task', 'uploaded_by', 'created_at')
    list_filter = ('created_at', 'uploaded_by', 'task')
    search_fields = ('file', 'task__title', 'uploaded_by__username')
    raw_id_fields = ('task', 'uploaded_by',) # Удобно для поиска по ID, если много задач/пользователей