from mcp_server.expense_policy_server import (
    ExpensePolicyServer
)


def test_meal_policy():

    policy = (
        ExpensePolicyServer
        .get_meal_limit()
    )

    assert (
        policy["max_amount"]
        == 100
    )


def test_vendor_lookup():

    result = (
        ExpensePolicyServer
        .lookup_vendor("Hilton")
    )

    assert (
        result["approved"]
        is True
    )
