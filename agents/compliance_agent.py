from skills.compliance_skill import (
    detect_category_mismatch
)

from mcp_server.expense_policy_server import (
    ExpensePolicyServer
)


class ComplianceAgent:

    def review(self, expense):

        findings = []

        violations = 0

        mismatch = detect_category_mismatch(
            expense.category,
            expense.description
        )

        if mismatch:
            findings.append(
                "Category mismatch"
            )
            violations += 1

        if expense.category == "Meals":

            policy = (
                ExpensePolicyServer
                .get_meal_limit()
            )

            if expense.amount > policy["max_amount"]:

                findings.append(
                    "Meal policy exceeded"
                )

                violations += 1

        return {
            "violations": violations,
            "findings": findings
        }
