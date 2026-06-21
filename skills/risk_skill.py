def calculate_risk_score(
    amount: float,
    injection_detected: bool,
    policy_violations: int
):

    score = 0

    if amount > 100:
        score += 20

    if amount > 500:
        score += 20

    if amount > 1000:
        score += 20

    score += policy_violations * 15

    if injection_detected:
        score += 50

    return min(score, 100)
