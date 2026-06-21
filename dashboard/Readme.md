## Dashboard Screenshot Architecture
```mermaid
 flowchart TD

A[Pending Expense]

A --> B[View Audit Report]

B --> C[Manager Review]

C --> D[Approve]

C --> E[Reject]

D --> F[Database Updated]

E --> F
```

## Running the Dashboard
~~~bash
uvicorn dashboard.app:app --reload
~~~

**Open:**
~~~bash
http://localhost:8000
~~~

## Demo Workflow

**Expense Submitted**
~~~bash
{
  "amount": 500,
  "submitter": "Bob",
  "category": "Meals",
  "description": "Conference dinner"
}
~~~

