# Architecture

## Multi-Agent Workflow

```mermaid
flowchart TD

A[Expense]
--> B[Security Agent]

B --> C[Compliance Agent]

C --> D[MCP Policy Server]

D --> E[Risk Agent]

E --> F[Manager Agent]

F --> G[Decision]
```
