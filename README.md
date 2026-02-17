# Task Scheduler System 

A priority-based task scheduling system written in Python, built as part of a Data Structures course at Ben-Gurion University.

## Overview

This system manages tasks and workers efficiently using custom-implemented data structures. Tasks are prioritized by urgency, importance, and time constraints, then automatically allocated to workers based on skills and availability.

## Features

### Task Management
- **Priority-based insertion** — tasks sorted by urgency, importance, and time window
- **Task attributes:** ID, description, urgency, importance, time window (hours), required skills
- **Dynamic updates** — modify task properties while maintaining priority order
- **Completion tracking** — completed tasks stored in a stack

### Worker Management
-  **Worker profiles** — ID, name, skills (with proficiency levels), availability, salary
- **Availability tracking** — multiple time windows per worker
- **Salary updates** — increment worker compensation
- **Skill progression** — add skills and increase proficiency levels

### Task Allocation
- **Skill matching** — allocates tasks only to workers with required skills
- **Time validation** — ensures worker availability covers task time window
- **Re-queuing** — tasks without suitable workers return to the queue

## Data Structures Implemented

### Custom Queue (`MyQueue`)
- Linked list implementation
- **Operations:** `enqueue()`, `dequeue()`, `is_empty()`
- **Usage:** Task queue, worker queue

### Custom Stack (`Stack`)
- List-based implementation
- **Operations:** `push()`, `pop()`, `peek()`, `is_empty()`
- **Usage:** Completed tasks history

## Task Priority Algorithm

Tasks are ordered by:
1. **Urgency** (highest first)
2. **Importance** (if urgency is equal)
3. **Start time** (earlier first, if urgency and importance are equal)
4. **End time** (earlier first, if all above are equal)

```python
# Priority comparison logic
if task1.urgency > task2.urgency: return True
elif task1.urgency == task2.urgency:
    if task1.importance > task2.importance: return True
    elif task1.importance == task2.importance:
        if task1.time_window[0] < task2.time_window[0]: return True
        # ... and so on
```

## Project Structure

```
├── TaskScheduler.py        # Main scheduler with allocation logic
├── Task.py                 # Task class with validation
├── Worker.py               # Worker class with skills/availability
├── ADTs.py                 # Custom Queue and Stack implementations
└── id_generator.py         # ID generation utilities
```

## How to Run

**Requirements:** Python 3.7+

### Example Usage

```python
from TaskScheduler import TaskScheduler
from Task import Task
from Worker import Worker

# Create scheduler
scheduler = TaskScheduler()

# Add tasks
task1 = Task(
    task_id=1,
    description="Deploy backend API",
    urgency=5,
    importance=4,
    time_window=(9, 17),  # 9 AM - 5 PM
    needed_skills={"Python": 3, "Docker": 2}
)
scheduler.add_task(task1)

# Add workers
worker1 = Worker(
    worker_id=101,
    name="Alice",
    skills={"Python": 4, "Docker": 3, "AWS": 2},
    availability=[(9, 12), (14, 18)],
    salary=5000
)
scheduler.add_worker(worker1)

# Allocate task to worker
scheduler.allocate_task()

# Update task properties
scheduler.update_task(
    task_id=1,
    urgency=6,
    description="URGENT: Deploy backend API"
)

# Update worker
worker1.update_skills(["Kubernetes"])
worker1.update_salary(500)
```

## Validation & Error Handling

### Task Validation
-  Task ID must be integer
-  Description must be non-empty string
-  Urgency and importance must be positive integers
-  Time window: `(start, end)` where `0 ≤ start < end ≤ 23`
-  Skills: dictionary with string keys and positive integer values

### Worker Validation
- Worker ID must be integer
- Name must be non-empty string
- Skills: dictionary with string keys and positive integer values
- Availability: list of tuples `(start, end)` where `0 ≤ start < end ≤ 23`
- Salary must be positive integer

### Exceptions
```python
raise TypeError("task must be a Task type")
raise ValueError("task_id not exist")
raise RuntimeError("Queue is empty")
```

## Key Algorithms

### Task Insertion (Priority Queue)
1. Dequeue all tasks into temporary queue
2. Insert new task at correct priority position
3. Enqueue all tasks back to main queue
- **Time Complexity:** O(n)

### Task Allocation (Greedy Matching)
1. Dequeue highest-priority task
2. Iterate through workers to find skill match
3. Check worker availability overlaps with task time window
4. If match found → push to completed stack
5. If no match → re-enqueue task
- **Time Complexity:** O(w × a) where w = workers, a = availability slots

## Concepts Demonstrated

- **Custom ADT implementation** — Queue and Stack from scratch
- **Priority queue** — insertion with multiple comparison criteria
- **Encapsulation** — private attributes with getters
- **Validation** — comprehensive input checking with exceptions
- **Greedy algorithms** — task allocation strategy
- **Time window matching** — interval overlap detection

## Technologies

- Python 3
- Object-Oriented Programming
- Custom data structures (Queue, Stack)
- Algorithm design

## Course

Data Structures — Ben-Gurion University of the Negev
