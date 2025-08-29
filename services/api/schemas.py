"""Pydantic schemas shared across API endpoints.

These schemas define the shape of request and response bodies exchanged between
the frontend and backend.  They mirror the JSON examples provided in the
product requirements document.  When updating models in `models.py`, ensure
the corresponding schemas here are adjusted accordingly.
"""
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class RequirementItem(BaseModel):
    type: str = Field(..., description="Category of requirement (e.g. pass_fail, mandatory_doc, date)")
    label: str = Field(..., description="Human‑readable label for the requirement")
    value: Optional[str] = Field(None, description="Value associated with the requirement (e.g. £5m, 60%)")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score between 0 and 1")
    source_ref: str = Field(..., description="Pointer to the source document and location")
    status: Optional[str] = Field(None, description="Status of the requirement (e.g. satisfied, missing)")


class RequirementResponse(BaseModel):
    tender_id: str = Field(..., description="Unique identifier of the tender")
    requirements: List[RequirementItem] = Field(..., description="List of extracted requirements")


class AnswerPlan(BaseModel):
    tender_id: str = Field(..., description="Unique identifier of the tender")
    question_id: str = Field(..., description="Unique identifier of the question")
    question: str = Field(..., description="Full question text")
    structure: List[str] = Field(..., description="Ordered list of section headings for the answer")
    evidence_prompts: List[str] = Field(..., description="Evidence prompts to gather supporting material")
    word_limit: Optional[int] = Field(None, description="Maximum number of words allowed")
    weight: Optional[int] = Field(None, description="Weighting of the question in the evaluation")


__all__ = [
    "RequirementItem",
    "RequirementResponse",
    "AnswerPlan",
]