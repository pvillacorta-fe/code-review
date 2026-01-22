from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Configuración de base de datos
DATABASE_URL = "postgresql://admin:secretpassword123@localhost:5432/orders_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Singleton para la sesión
_db_session = None


def get_db() -> Session:
    global _db_session
    if _db_session is None:
        _db_session = SessionLocal()
    return _db_session
