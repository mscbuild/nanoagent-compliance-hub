from agents.security_agent import (
    SecurityAgent
)

from agents.compliance_agent import (
    ComplianceAgent
)

from agents.risk_agent import (
    RiskAgent
)

from agents.manager_agent import (
    ManagerAgent
)

from app.config import settings


class ExpenseWorkflow:

    def __init__(self):

        self.security = SecurityAgent()

        self.compliance = ComplianceAgent()

        self.risk = RiskAgent()

        self.manager = ManagerAgent()

    def run(self, expense):

        if expense.amount < (
            settings.AUTO_APPROVE_LIMIT
        ):
            return {
                "status": "auto_approved"
            }

        security = self.security.scan(
            expense
        )

        expense.description = (
            security["clean_description"]
        )

        compliance = (
            self.compliance.review(
                expense
            )
        )

        findings = (
            security["findings"]
            + compliance["findings"]
        )

        risk = self.risk.evaluate(
            expense,
            security["injection_detected"],
            compliance["violations"],
            findings
        )

        if (
            risk["score"]
            >= settings.RISK_THRESHOLD
        ):

            return self.manager.request_review(
                expense,
                risk["report"]
            )

        return {
            "status": "approved",
            "risk": risk
        }
