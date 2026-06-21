from app.workflow import ExpenseWorkflow


class Expense:

    amount = 40

    submitter = "Alice"

    category = "Meals"

    description = "Lunch meeting"


def test_auto_approve():

    workflow = ExpenseWorkflow()

    result = workflow.run(
        Expense()
    )

    assert (
        result["status"]
        == "auto_approved"
    )
