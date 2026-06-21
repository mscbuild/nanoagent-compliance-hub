from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Text
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

from app.config import settings

Base = declarative_base()

engine = create_engine(
    settings.DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class ExpenseRecord(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)

    submitter = Column(String)

    amount = Column(Float)

    category = Column(String)

    description = Column(Text)

    status = Column(String)

    risk_score = Column(Integer)

    audit_report = Column(Text)


def init_db():
    Base.metadata.create_all(bind=engine)
