# ShuttleSync

VIT Vellore campus shuttle tracking demo with simulated live vehicle movement.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm --filter @workspace/shuttlesync run dev` — run the ShuttleSync frontend
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- No database or external integrations are required; shuttle positions live in the server simulator.

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `artifacts/shuttlesync` — React + Vite map UI.
- `artifacts/api-server/src/lib/shuttle-simulator.ts` — route geometry and movement loop.
- `artifacts/api-server/src/routes/shuttles.ts` — login, routes, shuttles, and nearest-shuttle endpoints.
- `lib/api-spec/openapi.yaml` — source of truth for generated API clients and Zod schemas.

## Architecture decisions

- Shuttle locations are simulated in memory so the demo works without GPS hardware or database setup.
- The frontend polls the simulator through the generated API hooks; server movement remains independent of any one browser session.
- Register-number login intentionally uses a small allowlist for review-demo access rather than production authentication.

## Product

Students log in with a demo VIT register number, watch shuttles move around campus, click the map to set their location, and see the nearest vehicle, ETA, and available seats.

## User preferences

The user wants working demo behavior prioritized over perfection.

## Gotchas

- Run API codegen after changing `lib/api-spec/openapi.yaml`.
- Start both the API and frontend workflows for the full preview.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
