# ShuttleSync

ShuttleSync is a generic smart transit tracking prototype for city buses,
college buses, school buses, office shuttles, and private transit providers.
Vehicle movement, passenger entry/exit, and historical boarding data are
simulated so the app works without GPS hardware, cameras, or a database.

## Features

- Leaflet/OpenStreetMap live map with six simulated buses across three generic routes.
- Trip planning from a pickup location to a destination.
- Route matching using ordered stop lists.
- Seat prediction using:
  `predicted_occupancy = current_occupancy + expected_boarding_before_pickup - expected_alighting_before_pickup`
  and `predicted_seats = max(0, capacity - predicted_occupancy)`.
- Recommended bus, limited-seat/full states, and alternatives for the next bus,
  shared ride, and auto/cab estimates.
- Google Routes estimate when `GOOGLE_MAPS_API_KEY` is configured, with a
  Haversine/average-speed fallback when it is unavailable or fails.
- Privacy-aware future design notes for anonymous occupancy counters and
  optional driver/tracker GPS.
- No login, payment, booking, facial recognition, or passenger identity data.

## Run locally

Install JavaScript dependencies from the repository root:

```bash
pnpm install
```

Install Python dependencies into the Replit-managed environment:

```bash
uv pip install -r backend/requirements.txt
```

Start the FastAPI service:

```bash
uv run uvicorn backend.main:app --host 0.0.0.0 --port 8080
```

Start the frontend in another terminal:

```bash
pnpm --filter @workspace/shuttlesync run dev
```

Open the Replit preview URL. The API is available under `/api`.

## Useful checks

```bash
python3 -m compileall -q backend
pnpm --filter @workspace/shuttlesync run typecheck
pnpm run typecheck
pnpm run build
```

If the OpenAPI contract changes, regenerate the clients:

```bash
pnpm --filter @workspace/api-spec run codegen
```

## Project structure

- `artifacts/shuttlesync` — React + Vite frontend with the preserved Leaflet UI.
- `backend` — Python 3 + FastAPI models, simulator, algorithms, and Google Routes adapter.
- `lib/api-spec/openapi.yaml` — source API contract.
- `lib/api-client-react` — generated frontend hooks.
- `lib/api-zod` — generated TypeScript validation schemas for legacy package checks.
- `backend/README_BACKEND.md` — backend-specific operation notes.