from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CleanedDevSalary(Base):
    __tablename__ = "cleaned_dev_salary"

    id = Column(Integer, primary_key = True, autoincrement=True)

    Age = Column(String, nullable=True)
    EdLevel = Column(String, nullable=True)
    Employment = Column(String, nullable=True)
    WorkExp = Column(String, nullable=True)
    YearsCode = Column(String, nullable=True)
    DevType = Column(String, nullable=True)
    OrgSize = Column(String, nullable=True)
    RemoteWork = Column(String, nullable=True)
    Industry = Column(String, nullable=True)
    Country = Column(String, nullable=True)
    LanguageHaveWorkedWith = Column(String, nullable=True)
    ConvertedCompYearly = Column(Float, nullable=True)

def create_tables(engine):
    Base.metadata.create_all(engine)
    print("[db] Tables created")