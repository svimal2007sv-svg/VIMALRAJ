from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class DocumentRequest(BaseModel):
    document_type: str = Field(..., description="e.g., NDA, Employment Agreement, Rental Contract")
    jurisdiction: str = Field(default="Generic/US Common Law", description="Governing state or country")
    party_a: str = Field(..., description="First party / Disclosing party / Employer")
    party_b: str = Field(..., description="Second party / Receiving party / Employee")
    key_terms: Dict[str, Any] = Field(default_factory=dict, description="Custom clauses, durations, compensation, etc.")

class DocumentResponse(BaseModel):
    document_id: str
    document_type: str
    generated_content: str
    disclaimer: str