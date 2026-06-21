from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///expenses.db"
    )

    AUTO_APPROVE_LIMIT = int(
        os.getenv("AUTO_APPROVE_LIMIT", 100)
    )

    RISK_THRESHOLD = int(
        os.getenv("RISK_THRESHOLD", 70)
    )

settings = Settings()
