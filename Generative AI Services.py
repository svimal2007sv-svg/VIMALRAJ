import os
import google.generativeai as genai
from app.schemas.document import DocumentRequest

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
You are LegalEase, an expert legal drafting assistant. 
Generate precise, clearly structured legal documents based on user parameters.
Always include appropriate standard clauses (Severability, Governing Law, Entire Agreement).
Format your output in clean Markdown.
"""

def generate_legal_document(req: DocumentRequest) -> str:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=SYSTEM_INSTRUCTION,
        generation_config={
            "temperature": 0.2,  # Low temperature for formal consistency
            "top_p": 0.95,
            "max_output_tokens": 4096,
        }
    )

    prompt = f"""
    Draft a legally structured {req.document_type}.
    
    Parties Involved:
    - Party A: {req.party_a}
    - Party B: {req.party_b}
    
    Jurisdiction: {req.jurisdiction}
    
    Specific Clauses & Terms:
    {req.key_terms}
    
    Include title, preamble, definitions, substantive clauses, and signature blocks.
    """

    response = model.generate_content(prompt)
    return response.text