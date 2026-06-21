import json

from app.models import Expense

from app.workflow import (
    ExpenseWorkflow
)


def process_expense(path):

    with open(path) as f:
        payload = json.load(f)

    expense = Expense(**payload)

    workflow = ExpenseWorkflow()

    result = workflow.run(
        expense
    )

    print(result)


if __name__ == "__main__":

    process_expense(
        "sample_expenses/conference.json"
    )
