import json

from app.schemas.architecture import ArchitectureSpec
from app.schemas.requirement import RequirementSpec

def build_api_design_prompt(
    user_prompt: str,
    requirements: RequirementSpec,
    architecture: ArchitectureSpec
) -> str:
    requirements_json = json.dumps(requirements.model_dump(), indent=2)
    architecture_json = json.dumps(architecture.model_dump(), indent=2)
    return f"""
    You are a senior backend API designer.
    Your task is to design REST API contracts based on the user's request, structured requirements, and backend architecture.
    Return ONLY valid JSON.
    Do not include markdown.
    Do not include explanation text before or after the JSON.
    The JSON must follow this exact structure:
    {{
    "endpoints": [
        {{
        "service_name": "string",
        "method": "GET | POST | PUT | PATCH | DELETE",
        "path": "string",
        "purpose": "string",
        "request_schema": {{}},
        "response_schema": {{}},
        "validation_rules": ["string"]
        }}
    ]
    }}
    Guidelines:
    - Generate practical REST endpoints.
    - Keep endpoints aligned with the architecture services.
    - Include request and response schemas as JSON objects.
    - Include validation rules for required fields, IDs, pagination, auth, and state transitions where relevant.
    - Do not create endpoints for services that do not exist in the architecture.
    - Avoid over-designing. Include the most important endpoints only.
    Original user request:
    "{user_prompt}"
    Structured requirements:
    {requirements_json}
    Architecture:
    {architecture_json}
    """