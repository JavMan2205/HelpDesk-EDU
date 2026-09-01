# HelpDesk EDU — Sistema de Gestión de Incidencias

**HelpDesk EDU** es una aplicación desarrollada en Python para la gestión y seguimiento de tickets de soporte técnico en entornos académicos. Este proyecto forma parte del curso de Programación / Desarrollo de Software (v0.3).

---

## Stack Tecnológico

- **Lenguaje:** Python 3.13+
- **Gestor de Entorno y Paquetes:** `uv`
- **Framework de Pruebas:** `pytest`
- **Control de Versiones:** Git & GitHub (Flujo Gitflow / Feature Branch)

---

## Arquitectura del Proyecto

El sistema está estructurado bajo principios de Programación Orientada a Objetos (POO), con separación estricta de responsabilidades entre entidades y servicios:

```text
HelpDesk-EDU/
├── app/
│   ├── models/
│   │   ├── entities.py       # Entidades de dominio (Ticket, User, Requester, Technician, Comment)
│   │   └── enums.py          # Enumeraciones (TicketStatus, TicketPriority)
│   └── services/
│       └── tickets.py        # Servicios de negocio y lógica de consultas
├── tests/
│   └── test_week09_queries.py# Pruebas automatizadas del módulo de consultas
├── pyproject.toml            # Configuración del proyecto y pytest
└── README.md

Funcionalidades de Consultas (Semana 9)
El servicio TicketService responde a preguntas reales del negocio mediante las siguientes consultas sobre el modelo relacional:

list_by_technician(technician_id): Retorna los tickets asignados a un técnico específico para evaluar su carga de trabajo.

list_by_category(category): Filtra los tickets por área temática (ej. Hardware, Software) para derivación y análisis de incidencias.

list_by_status(status): Permite consultar el estado de avance de las solicitudes (OPEN, IN_PROGRESS, RESOLVED, CLOSED).

Ejecución de Pruebas
Para ejecutar el suite de pruebas automatizadas con la validación mínima:

Bash
uv run pytest -q