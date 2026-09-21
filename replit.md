# ShuttleSync

Generic smart transit tracking and seat availability prediction prototype for
city buses, college buses, school buses, office shuttles, and private transit
providers. All vehicle and occupancy data is simulated.

## Run & Operate

- `uv run uvicorn backend.main:app --host 0.0.0.0 --port 8080` — run FastAPI locally.
- `pnpm --filter @workspace/shuttlesync run dev` — run the React frontend.
- `pnpm run typecheck` — full TypeScript typecheck across packages.
- `pnpm run build` — typecheck and build all JavaScript packages.
- `python3 -m compileall -q backend` — check Python syntax.
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and schemas.
- No database or external integrations are required.

## Stack

- Frontend: React, Vite, TypeScript, Tailwind CSS, Leaflet/OpenStreetMap.
- Backend: Python 3, FastAPI, Pydantic, Uvicorn, HTTPX.
- Contract: OpenAPI with generated React Query and Zod helpers.
- State: in-memory simulator only.

## Where things live

- `artifacts/shuttlesync` — React + Vite map UI.
- `backend/main.py` — FastAPI routes.
- `backend/simulator.py` — simulated movement and occupancy.
- `backend/algorithms.py` — route matching, ETA, ranking, and seat prediction.
- `backend/google_maps.py` — server-side Google Routes adapter with fallback.
- `lib/api-spec/openapi.yaml` — source API contract.

## Architecture decisions

- Bus movement advances every 2.5 seconds in memory.
- Passenger changes happen at simulated stops; no real GPS, camera, or hardware is used.
- Seat prediction uses current occupancy plus expected boarding minus expected alighting.
- `GOOGLE_MAPS_API_KEY` is read only by the backend with `os.getenv`; it is never
  returned, logged, or shown.
- Leaflet/OpenStreetMap remains the visible map fallback so Preview works without
  Google services.
- Route matching uses ordered stop lists and returns ranked matching buses.
- No login, passenger identity, facial recognition, payment, booking, or database.

## Product

Users choose a generic pickup point and destination, see simulated buses moving
on a live map, and receive a recommendation based on ETA and predicted seats.
The UI also documents a future privacy-aware path for anonymous occupancy
counters and optional driver/tracker location updates.

## Gotchas

- Start both the FastAPI and frontend workflows for the full preview.
- Run API codegen after changing `lib/api-spec/openapi.yaml`.
- Google Routes is optional; the fallback estimate is expected in Preview when
  no key is configured or the provider is unavailable.