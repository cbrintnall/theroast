from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

ENGINE = create_engine("sqlite:///tmp/test.db", echo=True)
Base = declarative_base()

# Sessionmaker returns a class, not object.
Session = sessionmaker(bind=ENGINE)
SESSION = Session()