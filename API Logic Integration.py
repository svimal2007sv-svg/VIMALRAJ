import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.document import DocumentRequest, DocumentResponse
from app.services.gemini_service import generate_legal_document

app = FastAPI(
    title="LegalEase API",
    version="1.0.0",
    description="Backend API for LegalEase: AI-Powered Legal Document Generator"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "LegalEase API"}

@app.post("/api/v1/documents/generate", response_model=DocumentResponse)
def create_document(request: DocumentRequest):
    try:
        content = generate_legal_document(request)
        return DocumentResponse(
            document_id=str(uuid.uuid4()),
            document_type=request.document_type,
            generated_content=content,
            disclaimer="Notice: This document is AI-generated for informational and drafting purposes. Have qualified legal counsel review before execution."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))