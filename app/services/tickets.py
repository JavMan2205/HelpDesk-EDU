from typing import Union, Optional
from app.models.entities import Ticket, Comment
from app.models.enums import TicketStatus

class TicketService:
    def __init__(self):
        self._tickets: list[Ticket] = []
        self._next_ticket_id = 1
        self._next_comment_id = 1

    def create(self, title: str, description: str, category: str, priority: str, requester_id: int) -> Ticket:
        ticket = Ticket(
            id=self._next_ticket_id,
            title=title,
            description=description,
            category=category,
            priority=priority,
            requester_id=requester_id
        )
        self._tickets.append(ticket)
        self._next_ticket_id += 1
        return ticket

    def get_by_id(self, ticket_id: int) -> Optional[Ticket]:
        for ticket in self._tickets:
            if ticket.id == ticket_id:
                return ticket
        return None

    def assign_technician(self, ticket_id: int, technician_id: int) -> bool:
        ticket = self.get_by_id(ticket_id)
        if ticket:
            ticket.assignee_id = technician_id
            ticket.status = TicketStatus.IN_PROGRESS
            return True
        return False

    def add_comment(self, ticket_id: int, author_id: int, text: str) -> bool:
        ticket = self.get_by_id(ticket_id)
        if ticket and text.strip():
            comment = Comment(id=self._next_comment_id, author_id=author_id, text=text)
            ticket.comments.append(comment)
            self._next_comment_id += 1
            return True
        return False

    # --- Consultas Incremento Semana 9 ---

    def list_by_technician(self, technician_id: int) -> list[Ticket]:
        """Devuelve únicamente los tickets asignados a un técnico específico."""
        return [t for t in self._tickets if t.assignee_id == technician_id]

    def list_by_category(self, category: str) -> list[Ticket]:
        """Devuelve únicamente los tickets que pertenecen a una categoría específica."""
        category_clean = category.strip().lower()
        return [t for t in self._tickets if t.category.strip().lower() == category_clean]

    def list_by_status(self, status: Union[str, TicketStatus]) -> list[Ticket]:
        """Devuelve únicamente los tickets que se encuentran en un estado determinado."""
        if isinstance(status, str):
            status_value = status.strip().upper()
        elif isinstance(status, TicketStatus):
            status_value = status.value.upper()
        else:
            status_value = str(status).upper()

        matching = []
        for t in self._tickets:
            t_status = t.status.value.upper() if isinstance(t.status, TicketStatus) else str(t.status).upper()
            if t_status == status_value:
                matching.append(t)
        return matching