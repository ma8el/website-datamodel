from sqlalchemy import Column, Integer, Date, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Greeting(Base):
    """Schema LandingSocials"""
    __tablename__ = "greeting"
    id = Column(Integer, primary_key=True, autoincrement=True)
    header = Column(Text, nullable=False)
    sub_header = Column(Text, nullable=False)
    image_ref = Column(Text, nullable=True)


class LandingSocials(Base):
    """Schema LandingSocials"""
    __tablename__ = "landing_socials"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    icon = Column(Text, nullable=False)
    href = Column(Text, nullable=False)
    color = Column(Text, nullable=False)
