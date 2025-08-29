"""Database models for BidBrief.

This module defines SQLAlchemy models corresponding to the high‑level
entities described in the product requirements document (PRD).  Only a
subset of fields are included here to illustrate the pattern; additional
fields, indices and relationships should be added as you expand the
application.
"""
from __future__ import annotations

import datetime as dt
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    JSON,
)
from sqlalchemy.orm import relationship

from .database import Base


class Organisation(Base):
    __tablename__ = "organisations"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False)
    plan: str = Column(String(50), nullable=False, default="free")
    seats: int = Column(Integer, nullable=False, default=1)
    created_at: dt.datetime = Column(DateTime, default=dt.datetime.utcnow, nullable=False)

    users = relationship("User", back_populates="organisation", cascade="all, delete-orphan")
    tenders = relationship("Tender", back_populates="organisation", cascade="all, delete-orphan")


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    org_id: int = Column(Integer, ForeignKey("organisations.id"), nullable=False, index=True)
    email: str = Column(String(255), unique=True, nullable=False)
    name: str = Column(String(255), nullable=True)
    role: str = Column(String(20), nullable=False, default="writer")
    created_at: dt.datetime = Column(DateTime, default=dt.datetime.utcnow, nullable=False)

    organisation = relationship("Organisation", back_populates="users")


class Tender(Base):
    __tablename__ = "tenders"

    id: int = Column(Integer, primary_key=True, index=True)
    org_id: int = Column(Integer, ForeignKey("organisations.id"), nullable=False, index=True)
    source: str = Column(String(50), nullable=True)
    title: str = Column(String(255), nullable=True)
    buyer: str = Column(String(255), nullable=True)
    cpv: str = Column(String(50), nullable=True)
    region: str = Column(String(100), nullable=True)
    reference: str = Column(String(100), nullable=True)
    deadlines_json = Column(JSON, nullable=True)
    url: str = Column(Text, nullable=True)
    created_at: dt.datetime = Column(DateTime, default=dt.datetime.utcnow, nullable=False)

    organisation = relationship("Organisation", back_populates="tenders")
    requirements = relationship("Requirement", back_populates="tender", cascade="all, delete-orphan")
    questions = relationship("Question", back_populates="tender", cascade="all, delete-orphan")


class Requirement(Base):
    __tablename__ = "requirements"

    id: int = Column(Integer, primary_key=True, index=True)
    tender_id: int = Column(Integer, ForeignKey("tenders.id"), nullable=False, index=True)
    type: str = Column(String(50), nullable=False)
    label: str = Column(String(255), nullable=False)
    value: str = Column(Text, nullable=True)
    confidence: float = Column(Float, nullable=True)
    status: str = Column(String(20), nullable=True)
    source_ref: str = Column(String(255), nullable=True)

    tender = relationship("Tender", back_populates="requirements")


class Question(Base):
    __tablename__ = "questions"

    id: int = Column(Integer, primary_key=True, index=True)
    tender_id: int = Column(Integer, ForeignKey("tenders.id"), nullable=False, index=True)
    text: str = Column(Text, nullable=False)
    word_limit: int = Column(Integer, nullable=True)
    weight: int = Column(Integer, nullable=True)
    section: str = Column(String(100), nullable=True)
    confidence: float = Column(Float, nullable=True)
    source_ref: str = Column(String(255), nullable=True)

    tender = relationship("Tender", back_populates="questions")
    answer_plans = relationship("AnswerPlan", back_populates="question", cascade="all, delete-orphan")


class AnswerPlan(Base):
    __tablename__ = "answer_plans"

    id: int = Column(Integer, primary_key=True, index=True)
    question_id: int = Column(Integer, ForeignKey("questions.id"), nullable=False, index=True)
    structure_json = Column(JSON, nullable=True)
    evidence_json = Column(JSON, nullable=True)
    word_limit: int = Column(Integer, nullable=True)
    weight: int = Column(Integer, nullable=True)
    status: str = Column(String(20), nullable=True)

    question = relationship("Question", back_populates="answer_plans")


# Additional models (Draft, Document, Exports, etc.) would follow the same pattern.