## 1. Entities and relations:
User:
- username
- email
- password
- first_name
- last_name
- date_joined
Many projects, many tasks

Project:
- title (Char)
- description (Text)
- owner (Foreign Key to User)
- members (ManyToMany to User)
- status ("Active", "Completed", "Archived")
- created_at (DateTime)
- updated_at (DateTime)


Task:
- title (Char)
- description (Text)
- project (Foreign Key to Project)
- assigned_to (Foreign Key to User. Many users on one task)
- reporter (Foreign Key to User. Who created task)
- status ("To Do", "Doing", "Check it", "Stopped", "Blocked")
- priority ("Low", "Medium", "High", "Critical")
- due_date (DateTime)
- created_at (DateTime)
- updated_at (DateTime)


Comment:
- task (Foreign Key to Task)
- author (Foreign Key to User)
- content (Text)
- created_at (DateTime)

Attachment:
- task (Foreign Key to Task)
- file (FileField)
- uploaded_by (Foreign Key to User)
- created_at (DateTime)

## API routs:
Django Rest Framework for creating RESTful API. Standard CRUD operations will be created for each entity.

Authentication:
- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/logout/`
- `GET /api/auth/me/`

Projects:
- `GET /api/projects/` - Get list of all projects. With permissions
- `POST /api/projects/` - Create new project
- `GET /api/projects/{id}/` - Get details about project
- `PUT /api/projects/{id}/` - Update the project
- `DELETE /api/projects/{id}/` - Delete the project
- `POST /api/projects/{id}/members/add/` - Add new member to project
- `POST /api/projects/{id}/members/remove/` - Remove member from project

Tasks:
- `GET api/tasks/` - Get list of all tasks in project
- `POST api/tasks/` - Create new task
- `GET api/tasks/{id}/` - Get details about task
- `PUT api/tasks/{id}/` - Update the task
- `DELETE api/tasks/{id}/` - Delete the task

Comments:
- `GET api/tasks/{task_id}/comments/` - Get list of comments for task
- `POST api/tasks/{task_id}/comments/` - Create new comment for task (All)
- `PUT api/comments/{id}/` - Update the comment (Only who wrote it and admin)
- `DELETE api/comments/{id}/` - Delete comment (Only who wrote it and admin)

Attachments:
- `GET api/tasks/{task_id}/attachments/` - Get all attachments for task
- `POST api/tasks/{task_id}/attachments/` - Upload new attachment fot task
- `DELETE api/attachments/{id}/` - Delete the attachment


