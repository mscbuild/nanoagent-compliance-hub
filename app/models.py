from pydantic import BaseModel
from typing import Optional


class Expense(BaseModel):
    amount: float
    submitter: str
    category: str
    description: str
    date: Optional[str] = None


class AuditResult(BaseModel):
    risk_score: int
    risk_level: str
    recommendation: str
    findings: list[str]
