from skills.risk_skill import (
    calculate_risk_score
)

from skills.reporting_skill import (
    generate_report
)


class RiskAgent:

    def evaluate(
        self,
        expense,
        injection_detected,
        policy_violations,
        findings
    ):

        score = calculate_risk_score(
            expense.amount,
            injection_detected,
            policy_violations
        )

        if score < 30:
            level = "LOW"
            recommendation = "APPROVE"

        elif score < 70:
            level = "MEDIUM"
            recommendation = "MANAGER_REVIEW"

        else:
            level = "HIGH"
            recommendation = "REJECT_OR_REVIEW"

        report = generate_report(
            findings,
            score,
            recommendation
        )

        return {
            "score": score,
            "level": level,
            "recommendation": recommendation,
            "report": report
        }
