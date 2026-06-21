import re

PROMPT_PATTERNS = [
    "ignore previous",
    "override",
    "system prompt",
    "approve instantly",
    "bypass"
]

SSN_REGEX = r"\b\d{3}-\d{2}-\d{4}\b"

CC_REGEX = r"\b(?:\d{4}[- ]?){3}\d{4}\b"


class SecurityAgent:

    def scan(self, expense):

        findings = []

        description = expense.description

        if re.search(SSN_REGEX, description):
            findings.append("SSN detected")

        if re.search(CC_REGEX, description):
            findings.append("Credit card detected")

        injection = any(
            pattern in description.lower()
            for pattern in PROMPT_PATTERNS
        )

        if injection:
            findings.append(
                "Prompt injection detected"
            )

        description = re.sub(
            SSN_REGEX,
            "[REDACTED_SSN]",
            description
        )

        description = re.sub(
            CC_REGEX,
            "[REDACTED_CC]",
            description
        )

        return {
            "clean_description": description,
            "injection_detected": injection,
            "findings": findings
        }
