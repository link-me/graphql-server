# Roadmap (2023)

Goals for GraphQL Server (Ariadne + FastAPI) organized by 2023 quarters.

Q1 2023
- Baseline schema: `User`, `Post`, queries and mutations.
- In-memory storage for prototyping; health route and Playground.
- Validation basics on resolvers; unified error shapes.

Q2 2023
- Auth: JWT login, role-based access in resolvers/middleware.
- Persistence: SQLite → PostgreSQL, DAO/repository layer.
- Pagination/filters for `users`/`posts`; DataLoader to fix N+1.
- Tests: `pytest` (unit/integration), fixtures for DB.

Q3 2023
- CI: GitHub Actions (Python 3.13), caching, lint/test matrix.
- Observability: structured logging, Prometheus metrics, tracing.
- Subscriptions via WebSocket for new posts/events.
- Security: CORS, request size limits, operation safelist.

Q4 2023
- Migrations: Alembic, schema versioning policy.
- Persisted queries and CDN/edge caching.
- Multi-tenant readiness and sharding strategy.
- Federation/stitching readiness for scaling services.

Technical Notes
- SDL + resolvers; keep schema and business logic separate.
- Layers: `schema` → `services` → `repos` → `db`.
- Error mapping: single format for GraphQL errors.
- Validate config via `pydantic-settings`; fail-fast on critical deps.