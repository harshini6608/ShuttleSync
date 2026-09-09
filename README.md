# ShuttleSync

ShuttleSync is a full-stack VIT Vellore campus shuttle tracking demo. Shuttle locations are simulated on the server so the app can demonstrate live movement without GPS hardware.

## Features

- Demo login with a VIT register number from a small allowlist.
- Live Leaflet map centered on VIT Vellore.
- Two simulated routes: Mens Hostel ↔ Academics and Girls Hostel ↔ Academics.
- Four shuttles that move every 2.5 seconds, with the map refreshing on the same cadence.
- Click the map to set a student location.
- Nearest-shuttle distance, ETA, route filtering, and seats left.
- Typed OpenAPI contract with generated React Query and Zod helpers.

## Demo register numbers

- `21BCE1234`
- `22BCB0101`
- `23BME0456`

## Run locally

Install dependencies from the repository root:

```bash
pnpm install
```

Start the API server in one terminal:

```bash
pnpm --filter @workspace/api-server run dev
```

Start the frontend in another terminal:

```bash
pnpm --filter @workspace/shuttlesync run dev
```

Open the preview URL provided by Replit. The API is available under `/api`.

## Useful checks

```bash
pnpm --filter @workspace/api-server run typecheck
pnpm --filter @workspace/shuttlesync run typecheck
pnpm run build
```

If the OpenAPI contract changes, regenerate the clients:

```bash
pnpm --filter @workspace/api-spec run codegen
```

## Project structure

- `artifacts/shuttlesync` — React + Vite frontend.
- `artifacts/api-server` — Express API and in-memory shuttle simulator.
- `lib/api-spec/openapi.yaml` — source API contract.
- `lib/api-client-react` — generated frontend hooks.
- `lib/api-zod` — generated server validation schemas.