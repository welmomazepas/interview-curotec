from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = ("sqlite:///db1.db")

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=0)
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
except Exception as error:
    print(error)
    print("error: Engine not defined")


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
