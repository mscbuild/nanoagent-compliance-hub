from app.database import (
    SessionLocal,
    ExpenseRecord
)


class ExpenseRepository:

    def create(
        self,
        submitter,
        amount,
        category,
        description,
        status,
        score,
        report
    ):

        db = SessionLocal()

        expense = ExpenseRecord(
            submitter=submitter,
            amount=amount,
            category=category,
            description=description,
            status=status,
            risk_score=score,
            audit_report=report
        )

        db.add(expense)
        db.commit()

        db.close()

    def get_all(self):

        db = SessionLocal()

        data = db.query(
            ExpenseRecord
        ).all()

        db.close()

        return data

    def get_by_id(self, id):

        db = SessionLocal()

        expense = db.query(
            ExpenseRecord
        ).filter(
            ExpenseRecord.id == id
        ).first()

        db.close()

        return expense

    def update_status(
        self,
        id,
        status
    ):

        db = SessionLocal()

        expense = db.query(
            ExpenseRecord
        ).filter(
            ExpenseRecord.id == id
        ).first()

        expense.status = status

        db.commit()
        db.close()
