from app.db import Base
from app.db import db
from sqlalchemy import Column, Integer, String, TEXT, DateTime


class TextSummary(Base):
    __tablename__ = "text_summary"
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    summary = Column(TEXT)
    create_at = Column(DateTime)

    def insert(self):
        db.add(self)
        db.commit()
        db.refresh(self)
        
    def delete(self):
        db.delete(self)
        db.commit()

    @classmethod
    def get_by_id(cls, id):
        return db.query(cls).filter_by(id = id).first()



