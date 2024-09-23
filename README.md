# Personal Task Management API
A robust, secure, and scalable Task Management API built with Django Rest Framework for personal use. The API allows users to create, manage, and organize tasks into categories, set priorities, track progress, and much more. It supports authentication via JWT tokens and integrates advanced features such as task reminders, recurring tasks, time tracking, and analytics.

## Key Features
1. **User Authentication & Authorization**: Secure authentication via JWT, with user registration and login endpoints. Users must authenticate themselves to access the application using secure JWT tokens

2. **Profile Management**: Users can update their profiles, including basic details.
3. **Task**: Organize tasks  to keep track of various types of tasks. Task fields: name, description, priority level, timestamp, due date, recurrence, recurrence_end , tags, start_time, end_time, time_spent, is_done,
4. **Task CRUD Operations**: Create, view, update, and delete tasks. Users can also:
Mark tasks as done or undone. Tasks cannot be marked "Done" or "Undone" once the due date has passed.
Tasks with due dates that have passed cannot be updated.
5. **Task Filters and Sorting**.Filter tasks by tags, status, due date, or priority.
6. **Task Prioritization**: Assign priority levels to tasks and automatically sort them based on importance.
7. **Task History**: Completed tasks are archived after a specified period (e.g., 30 days) to keep the task list manageable.
Users can view the history of archived tasks, including completed and overdue tasks.
8. **Task Recurrence**: Set recurring tasks (e.g., daily, weekly) to streamline repetitive activities. A recurring task is a task that repeats on a regular schedule, such as daily, weekly, or monthly. Once a task is marked as done or its due date passes, a new task with the same properties (but a new due date) is automatically created according to the recurrence pattern.
9. **Task Reminders**: Get notifications or reminders for tasks nearing their due dates.
10. **Time Tracking**: Track the time spent on tasks, including start and end times. Allows users to record the amount of time they spend on a task. This could help users analyze how much time is spent on different tasks, and it could be tied into analytics
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
- **Deployment**: Docker, Gunicorn, Nginx

## Endpoints

## Future Enhancements
1. **Build a frontend**- build a frontend using frameworks like React. 

## Contributing
Contributions are welcome! Please submit a pull request or open an issue if you would like to suggest new features or report bugs.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Developer: --
Email: --