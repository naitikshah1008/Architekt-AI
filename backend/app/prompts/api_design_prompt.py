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
    Your task is to design practical REST API contracts based on the user's request, structured requirements, and backend architecture.
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
    - Generate practical REST endpoints only.
    - Keep endpoints aligned with the architecture services.
    - Each endpoint must belong to a backend service from the architecture.
    - Do not create frontend routes.
    - Do not create database queries as endpoints.
    - Include request and response schemas as JSON objects.
    - Include validation rules for required fields, IDs, pagination, authentication, authorization, and state transitions where relevant.
    - Prefer realistic API paths such as /users, /rides, /drivers/location, /payments, /notifications, and /admin/users.
    - Avoid over-designing. Include the most important endpoints needed for the MVP.
    - For asynchronous workflows, expose the API that starts the workflow and mention event-related fields in the response if needed.
    Original user request:
    "{user_prompt}"
    Structured requirements:
    {requirements_json}
    Backend architecture:
    {architecture_json}
    """