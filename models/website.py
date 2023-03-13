from sqlalchemy import Column, Integer, Date, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Greeting(Base):
    """Schema Greeting"""
    __tablename__ = "greeting"
    id = Column(Integer, primary_key=True, autoincrement=True)
    header = Column(Text, nullable=False)
    sub_header = Column(Text, nullable=False)
    image_ref = Column(Text, nullable=True)


class Socials(Base):
    """Schema Socials"""
    __tablename__ = "socials"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    icon = Column(Text, nullable=False)
    href = Column(Text, nullable=False)
    color = Column(Text, nullable=False)

class Skills(Base):
    """Schema Skills"""
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    logo_url = Column(Text, nullable=False)