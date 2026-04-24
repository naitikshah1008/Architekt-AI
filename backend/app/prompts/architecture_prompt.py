import json

from app.schemas.requirement import RequirementSpec

def build_architecture_prompt(user_prompt: str, requirements: RequirementSpec) -> str:
    requirements_json = json.dumps(requirements.model_dump(), indent=2)
    return f"""
    You are a senior backend architect.
    Design a scalable backend architecture based on the user's request and structured requirements.
    Return ONLY valid JSON.
    Do not include markdown.
    Do not include explanation text before or after the JSON.
    The JSON must follow this exact structure:
    {{
    "services": [
        {{
        "name": "string",
        "responsibility": "string"
        }}
    ],
    "communication_patterns": [
        {{
        "source": "string",
        "target": "string",
        "protocol": "string",
        "reason": "string"
        }}
    ],
    "databases": ["string"],
    "infrastructure_components": ["string"],
    "scalability_strategy": ["string"],
    "fault_tolerance_strategy": ["string"]
    }}
    Guidelines:
    - Break the system into clear backend services.
    - Include REST, gRPC, Kafka, or message queues where appropriate.
    - Include storage choices such as PostgreSQL, Redis, object storage, search indexes, or NoSQL if needed.
    - Include practical scaling and failure-handling strategies.
    - Keep the architecture realistic.
    Original user request:
    "{user_prompt}"
    Structured requirements:
    {requirements_json}
    """