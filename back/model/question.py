from datetime import datetime
from typing import Self

class Question:
    
    def __init__(self: Self, title: str, goal: str | None = None) -> None:
        self.title = title
        self.goal = goal
        self.is_active = True
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
