from datetime import timedelta, timezone
from  .models import Task

def handle_task_completion(task):
    if task.recurrence == 'daily':
        next_due_date = task.due_date + timedelta(days=1)
    elif task.recurrence == 'weekly':
        next_due_date = task.due_date + timedelta(weeks=1)
    elif task.recurrence == 'monthly':
        next_due_date = task.due_date + timedelta(weeks=4)
    
    # Create the next task if recurrence_end is not reached
    if task.recurrence_end is None or next_due_date <= task.recurrence_end:
        Task.objects.create(
            name=task.name,
            description=task.description,
            due_date=next_due_date,
            recurrence=task.recurrence,
            recurrence_end=task.recurrence_end
        )


# time tracking for tasks
def start_task(task):
    task.start_time = timezone.now()
    task.save()

def stop_task(task):
    task.end_time = timezone.now()
    task.time_spent = task.end_time - task.start_time
    task.save()
