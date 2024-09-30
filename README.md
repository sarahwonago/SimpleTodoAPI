# Personal Task Management API
A robust, secure, and scalable Task Management API built with Django Rest Framework for personal use. The API allows users to create, manage, and organize tasks, set priorities, track progress, and much more. It supports authentication via JWT tokens and integrates advanced features such as task reminders, recurring tasks, time tracking, and analytics.

## Key Features
1. **User Authentication & Authorization**: Secure authentication via JWT, with user registration and login endpoints. Users must authenticate themselves to access the application using secure JWT tokens

2. **Profile Management**: Users can update their profiles, including basic details.

3. **Task**: Organize tasks  to keep track of various types of tasks. Task fields: title, description, priority level, timestamp, due date, recurrence, recurrence_end , tags, start_time, end_time, time_spent, status,

4. **Task CRUD Operations**: Create, view, update, and delete tasks. Users can also:
Mark tasks as done or undone. Tasks cannot be marked "Done" or "Undone" once the due date has passed.
Tasks with due dates that have passed cannot be updated.

5. **Task Filters and Sorting**.Filter tasks by tags, status, due date, or priority.

6. **Task Prioritization**: Assign priority levels to tasks and automatically sort them based on importance.

7. **Task History**: Users can view the history of tasks, including completed and overdue tasks.

8. **Task Recurrence**: Set recurring tasks (e.g., daily, weekly) to streamline repetitive activities. A recurring task is a task that repeats on a regular schedule, such as daily, weekly, or monthly. Once a task is marked as done or its due date passes, a new task with the same properties (but a new due date) is automatically created according to the recurrence pattern.

9. **Task Reminders**: Get notifications or reminders for tasks nearing their due dates.

10. **Time Tracking**: Track the time spent on tasks, including start and end times. Allows users to record the amount of time they spend on a task. This could help users analyze how much time is spent on different tasks, and it could be tied into analytics.

11. **Bulk Task Operations**: Perform bulk actions like marking multiple tasks as done or deleting several tasks at once.

12. **Task Tagging**: Add tags to tasks for better organization and filtering.Tags allow users to categorize tasks using custom labels (e.g., "work", "personal", "urgent"). Tags are useful for filtering and organizing tasks.

13. **Task Analytics & Insights**: Gain insights into task completion rates, average time spent, overdue tasks, and more.

14. **API Documentation**: Automatically generated Swagger or OpenAPI documentation for developers.
Security & CORS: Integrated with django-cors-headers and Django security middleware for production-grade security.


## Technology Stack
- **Backend**: Django, Django Rest Framework
- **Database**: Default(sqlite). You can use PostgreSQL
- **Caching**: Redis
- **Task Scheduling & Background Jobs**: Celery with Redis
- **User Management**: djoser, you can use dj-rest-auth, django-allauth
- **Authentication**: JWT via djangorestframework-simplejwt
- **API Documentation**: Swagger/OpenAPI (drf-spectacular)
- **Security**: Django Security Middleware, django-cors-headers
- **Filtering**: django-filter
- **Ordering**: rest_framework.filters.OrderingFilter
- **Testing**: pytest, pytest-django
- **Deployment**: Docker, Gunicorn, Nginx

## Endpoints

| Method | Endpoint                             | Description                                     |
|--------|--------------------------------------|-------------------------------------------------|
| POST   | `/api/auth/users/`                  | Register a new user                            |
| POST   | `/api/auth/jwt/create/`             | Login and get JWT tokens                       |
| POST   | `/api/auth/jwt/refresh/`            | Refresh JWT access token                       |
| GET    | `/api/auth/users/me/`               | Retrieve current user's information            |
| PUT    | `/api/auth/users/me/`               | Update the current user's profile              |
| POST   | `/api/auth/users/set_password/`     | Change the current user's password             |
| POST   | `/api/auth/users/reset_password/`   | Request a password reset email                 |
| POST   | `/api/tasks/`                       | Create a new task                              |
| GET    | `/api/tasks/`                       | Retrieve all tasks for the authenticated user  |
| GET    | `/api/tasks/{id}/`                  | Retrieve details for a specific task           |
| PUT    | `/api/tasks/{id}/`                  | Update an existing task                        |
| DELETE | `/api/tasks/{id}/`                  | Delete a task                                  |
| POST   | `/api/tasks/tags/`                  | Create a new tag                           |
| GET    | `/api/tasks/tags/`                   | Retrieve all tags  |
| GET    | `/api/tasks/tags/{id}/`               | Retrieve details for a specific tag          |
| PUT    | `/api/tasks/tag/{id}/`                  | Update an existing tag                   |
| DELETE | `/api/tasks/tags/{id}/`                  | Delete a tag                                 |





### Testing endpoints using postman
1. **Register a New user**: create a POST request to /api/auth/users with the following JSON payload

```

{
    "email": "user4@example.com",
    "username": "tes4tuser",
    "password": "password123!",
    "re_password": "password123!"
}

```
Response:

```

{
  "username": "tes4tuser",
  "email": "user4@example.com",
  "id": "6fd3a24c-b7fa-447c-8b1a-9210ccf10204"
}

```

2. **Login**: send a POST request to /api/auth/jwt/create/ with the following JSON payload:

```

{
    "email": "testuser@example.com",
    "password": "strong_password_123"
}

```

Response:
```

{
    "access": "<your_access_token>",
    "refresh": "<your_refresh_token>"
}
```

3. **User Information**: send a GET request to api/auth/users/me/ and add an authorization header:

```

Key: Authorization
Value: Bearer <your_access_token>

```

Response:
```
{
  "username": "tes4tuser",
  "id": "6fd3a24c-b7fa-447c-8b1a-9210ccf10204",
  "email": "user4@example.com"
}
```
4. **Update User info**: send a PUT reuest to api/auth/users/me and add an authorization header, with the following JSON payload

```
{
    "email": "newemail@example.com",
    "username": "newusername"
}

```
Response: updated the user profile
```
{
  "username": "newusername",
  "id": "6fd3a24c-b7fa-447c-8b1a-9210ccf10204",
  "email": "user4@example.com"
}
```

5. **Change password**: send a POST request to api/auth/users/set_password/ add an authorization header with the following JSON payload:

```
{
    "current_password": "strong_password_123",
    "new_password": "new_strong_password_123",
    "re_new_password": "new_strong_password_123"
}

```
Response: 

```
{
    "detail": "New password has been saved."
}
```
6. **Token Refresh**: send a POST request to api/auth/jwt/refresh/ with the following JSON payload:
```
{
    "refresh": "<your_refresh_token>"
}

```
Response:
```
{
    "access": "<new_access_token>"
}

```

7. **Password Reset**: send a POST request to api/auth/users/reset_password/ with payload:
```
{
    "email": "user@example.com"
}

```

Response:

8. **Create a new task**: send a POST request to api/tasks/ with the folliwing payload:

```
{
  "title": "New Task",
  "description": "A task with tags",
  "status": "pending",
  "priority": "high",
  "due_date": "2024-12-01T12:00:00Z",
  "tags": ["work", "urgent"]
}

```

Response:
```
{
  "id": "32af09ab-2e12-4eb2-b53a-38432fbe6301",
  "user": "zaza",
  "tags": [
    "work",
    "urgent"
  ],
  "title": "New Task",
  "description": "A task with tags",
  "status": "pending",
  "priority": "high",
  "recurrence": "none",
  "recurrence_end": null,
  "due_date": "2024-12-01T12:00:00Z",
  "start_time": null,
  "end_time": null,
  "time_spent": null,
  "created_at": "2024-09-25T13:12:00.532205Z"
}
```

9. **Fetch tasks**: send a GET request to api/tasks/ with the Authorization header:

Response:

```
[
  {
    "id": "d4937a5a-354a-40d9-b54e-c879e5aa4330",
    "user": "zaza",
    "title": "Learn Celery",
    "description": "Supposed to learn celery.",
    "status": "pending",
    "priority": "medium",
    "recurrence": "none",
    "recurrence_end": null,
    "due_date": null,
    "start_time": null,
    "end_time": null,
    "time_spent": null,
    "created_at": "2024-09-25T12:03:57.370501Z",
    "tags": []
  },
  {
    "id": "b4038c30-11dd-40f2-a9ce-c64eba6bad24",
    "user": "zaza",
    "title": "Learn Redis",
    "description": "Learn redis and integrate in your project",
    "status": "in_progress",
    "priority": "high",
    "recurrence": "daily",
    "recurrence_end": "2024-09-28T12:16:01Z",
    "due_date": "2024-09-25T12:16:47Z",
    "start_time": "12:16:54",
    "end_time": "18:00:00",
    "time_spent": null,
    "created_at": "2024-09-25T12:17:05.946469Z",
    "tags": []
  }
]
```

10. **Detail task**: send a GET request to api/tasks/id/ with authorization headers:

Response:
```
{
  "id": "32af09ab-2e12-4eb2-b53a-38432fbe6301",
  "user": "zaza",
  "tags": [
    "work",
    "urgent"
  ],
  "title": "New Task",
  "description": "A task with tags",
  "status": "pending",
  "priority": "high",
  "recurrence": "none",
  "recurrence_end": null,
  "due_date": "2024-12-01T12:00:00Z",
  "start_time": null,
  "end_time": null,
  "time_spent": null,
  "created_at": "2024-09-25T13:12:00.532205Z"
}
```

11. **Update task**: send a PUT request to api/tasks/id/ with the following JSON payload 

```

{
  "title": "New Task Updated",
  "description": "A task with tags updated",
  "status": "done",
  "priority": "high",
  "tags":["work"]
}
```

Response:

```

{
  "id": "32af09ab-2e12-4eb2-b53a-38432fbe6301",
  "user": "zaza",
  "tags": [
    "work"
  ],
  "title": "New Task Updated",
  "description": "A task with tags updated",
  "status": "done",
  "priority": "high",
  "recurrence": "none",
  "recurrence_end": null,
  "due_date": "2024-12-01T12:00:00Z",
  "start_time": null,
  "end_time": null,
  "time_spent": null,
  "created_at": "2024-09-25T13:12:00.532205Z"
}
```

12. **Delete task**: send a DELETE request to api/tasks/id/ with authorization headers:

Response:

```
{
  "detail": "Task deleted successfully"
}
```

13. **List tags**: send a GET request to api/tasks/tags/ with authorization headers:

Response:

```
[
  {
    "id": "908c1aca-267e-491e-bf61-73754be55c91",
    "name": "urgent"
  },
  {
    "id": "77d5b605-4c30-44c6-8496-e28f06b99329",
    "name": "coding"
  }
]
```

14. **Create a tag**: send a POST request to api/tasks/tags/ with JSON Payload:

```

{
  "name":"work"
}

```

Response:
```
{
  "id": "513a82b8-2a9c-4071-9584-5cc5d12e8196",
  "name": "work"
}
```

15. **Update a tag**: send a PUT request to api/tasks/tags/{id}/ with JSON Payload:

```
{
  "name":"work-updated"
}

```

Response:
```
{
  "id": "513a82b8-2a9c-4071-9584-5cc5d12e8196",
  "name": "work-updated"
}
```

16. **Delete a tag**: send a DELETE request to api/tasks/tags/{id}/ with authorization headers:

Response:

```

```

## Future Enhancements
1. **Build a frontend**- build a frontend using frameworks like React. 

## Contributing
Contributions are welcome! Please submit a pull request or open an issue if you would like to suggest new features or report bugs.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Developer: --
Email: --