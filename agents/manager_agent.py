class ManagerAgent:

    def request_review(
        self,
        expense,
        report
    ):

        return {
            "status": "pending_review",
            "expense": expense,
            "report": report
        }
