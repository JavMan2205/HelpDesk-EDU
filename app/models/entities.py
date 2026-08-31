from dataclasses import dataclass, field
from typing import Optional
from app.models.enums import TicketStatus, TicketPriority

@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class Requester(User):
    department: str = "General"

@dataclass
class Technician(User):
    specialty: str = "General Support"

@dataclass
class Comment:
    id: int
    author_id: int
    text: str

@dataclass
class Ticket:
    id: int
    title: str
    description: str
    category: str
    priority: str
    requester_id: int
    assignee_id: Optional[int] = None
    status: TicketStatus = TicketStatus.OPEN
    comments: list[Comment] = field(default_factory=list)