from fastapi import (
    FastAPI,
    Request
)

from fastapi.templating import (
    Jinja2Templates
)

from fastapi.responses import (
    RedirectResponse
)

from app.repository import (
    ExpenseRepository
)

app = FastAPI()

repo = ExpenseRepository()

templates = Jinja2Templates(
    directory="dashboard/templates"
)


@app.get("/")
def home(
    request: Request
):

    expenses = repo.get_all()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "expenses": expenses
        }
    )


@app.get("/approve/{id}")
def approve(id: int):

    repo.update_status(
        id,
        "approved"
    )

    return RedirectResponse(
        "/",
        status_code=302
    )


@app.get("/reject/{id}")
def reject(id: int):

    repo.update_status(
        id,
        "rejected"
    )

    return RedirectResponse(
        "/",
        status_code=302
    )
