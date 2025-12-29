# Discord_Bot_30_Day_Challenge - Backend Systems Practice (Build in Public)

A build-in-public Discord bot focused on practicing backend engineering fundamentals and system design principles using Python.

This project emphasizes clean architecture, observability, and scalability-ready patterns over feature count. Discord serves as the event source — the real focus is designing and evolving a maintainable backend system through daily iteration and reflection.

🚀 Purpose

This project exists to:

Practice real-world backend system design

Explore event-driven architectures

Build intuition around async flow control

Introduce observability early (logging, performance tracking)

Develop scalable, maintainable Python codebases

Learn publicly through daily progress and lessons learned

🧠 Backend Concepts Demonstrated

Event-Driven Architecture
Commands are triggered by Discord events and routed through a centralized command handler.

Asynchronous Execution Model
Uses Python’s async / await to handle concurrent command execution efficiently.

Modular Architecture
Command routing, execution, caching, and logging are cleanly separated into dedicated layers.

Observability & Performance Awareness
Structured logging and in-memory caching provide insight into command execution and response times.

Separation of Concerns
Infrastructure-level concerns (logging, caching) are isolated from business logic.

🗂️ Project Structure
```
Discord_Bot/
├── main.py                      # Application entry point & event wiring
├── handlers/
│   └── command_handler.py       # Central command routing
├── commands/                    # Individual command implementations
├── infrastructure/
│   ├── bot_cache.py             # In-memory caching layer
│   └── logging_config.py        # Centralized logging configuration
├── config/
│   └── .env                     # Environment variables
```


The infrastructure/ layer contains cross-cutting system concerns that support the application without being tied to specific commands.

⚙️ Current Capabilities

Dynamic command discovery and loading

Centralized command routing

Structured logging for command execution

Response-time caching for performance insights

Async event-driven execution

Environment-based configuration

📈 What I’m Learning

How backend systems evolve incrementally

Why observability should be introduced early

How architectural decisions compound over time

How to reason about performance before adding persistence

How to structure Python projects for long-term maintainability

🛣️ Roadmap

Planned improvements include:

Command-level error handling

Metrics aggregation (average response times, cache hit ratios)

Database integration with caching strategies

Reliability patterns (timeouts, retries)

Deployment and environment hardening

Production-ready logging output

🧪 Why Discord?

Discord provides a natural event-driven environment that mirrors backend request/response flows, making it ideal for practicing:

Async concurrency

Performance measurement

Observability

System design trade-offs

The platform itself is secondary — the backend design is the focus.

📚 Build in Public

This project is developed publicly with daily progress updates, refactors, and lessons learned.
The emphasis is on learning through iteration, improving code quality, and making architectural decisions explicit.

Feedback, suggestions, and critiques are always welcome.

🔗 Links

GitHub Repository: [add link here](https://github.com/bjoseph25/Discord_Bot_30_Day_Challenge)

Build in Public Updates: [optional (LinkedIn / blog)](https://www.linkedin.com/in/brandonjosephcs/)

⭐ For Reviewers

This project reflects my approach to backend engineering:
iterate, observe, refactor, and document the why.
