from pydantic import BaseModel
from typing import List, Optional

# Schema for creating a task
class TaskCreate(BaseModel):
    title: str
    is_completed: Optional[bool] = False

# Schema for updating a task
class TaskUpdate(BaseModel):
    title: Optional[str]
    is_completed: Optional[bool]

# Schema for bulk adding tasks
class BulkTaskCreate(BaseModel):
    tasks: List[TaskCreate]

# Schema for bulk deleting tasks
class BulkTaskDelete(BaseModel):
    task_ids: List[int]
