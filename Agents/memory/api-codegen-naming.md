---
name: OpenAPI codegen naming
description: Avoid response-schema name collisions with Orval-generated operation types.
---

When adding OpenAPI response schemas, avoid naming a component after the operation's generated response type (for example, `LoginResponse`). Prefer a domain-specific name such as `StudentSession`.

**Why:** Orval emits operation response schemas and component schemas into shared barrels; matching names can fail the workspace typecheck even when codegen itself succeeds.

**How to apply:** After every OpenAPI change, run the API codegen command and the workspace library typecheck before importing generated types into application code.