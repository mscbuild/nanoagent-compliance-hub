def generate_report(
    findings,
    score,
    recommendation
):

    report = f"""
# Expense Audit Report

Risk Score: {score}

Recommendation:
{recommendation}

Findings:
"""

    for item in findings:
        report += f"\n- {item}"

    return report
