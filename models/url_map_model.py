from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URLMapping(Base):
    __tablename__ = "url_mapping"

    id = Column(Integer, Sequence("url_id_seq"), primary_key=True)
    short_key = Column(String(6), unique=True, index=True)
    original_url = Column(String(2048), index=True)

DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/url_shortener"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
