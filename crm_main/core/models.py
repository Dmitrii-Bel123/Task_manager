from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Project(models.Model):
    STATUS_CHOICES = [
        ("Active","Active"),
        ("Completed","Completed"),
        ("Archived","Archived"),
    ]

    title = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(blank=True, verbose_name="Описание проекта")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects', verbose_name="Владелец")
    members = models.ManyToManyField(User, related_name='joined_projects', verbose_name="Участники")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active',verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title

class Task(models.Model):
    STATUS_CHOICES = [
        ("To Do","To Do"),
        ("Doing","Doing"),
        ("Check it","Check it"),
        ("Stopped", "Stopped"),
        ("Blocked", "Blocked"),
    ]

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(blank=True, verbose_name="Описание задачи")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", verbose_name='Проект')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks', verbose_name="Исполнитель")
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_owner', verbose_name="Создатель")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do", verbose_name="Статус")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Low", verbose_name="Приоритет")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Срок выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return f"{self.title} ({self.project.title})"

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments_task", verbose_name="Задача")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_author", verbose_name="Автор комментария")
    content = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий к задаче {self.task.title} от ({self.author.username})"

class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="attachments", verbose_name="Задача")
    file = models.FileField(upload_to="attachments/", verbose_name="Файл")  # Файлы будут храниться в media/attachments/
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="uploaded_attachments", verbose_name="Кем загржено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Вложение"
        verbose_name_plural = "Вложения"

    def __str__(self):
        return f"Вложение к задаче {self.task.title}: ({self.file.name})"