import json

from app.schemas.api_design import APIDesignSpec
from app.schemas.architecture import ArchitectureSpec
from app.schemas.requirement import RequirementSpec

def build_data_design_prompt(
    user_prompt: str,
    requirements: RequirementSpec,
    architecture: ArchitectureSpec,
    api_design: APIDesignSpec
) -> str:
    requirements_json = json.dumps(requirements.model_dump(), indent=2)
    architecture_json = json.dumps(architecture.model_dump(), indent=2)
    api_design_json = json.dumps(api_design.model_dump(), indent=2)
    return f"""
    You are a senior backend data architect.
    Your task is to design a practical database schema based on the user's request, structured requirements, backend architecture, and API contracts.
    Return ONLY valid JSON.
    Do not include markdown.
    Do not include explanation text before or after the JSON.
    The JSON must follow this exact structure:
    {{
    "tables": [
        {{
        "name": "string",
        "fields": [
            {{
            "name": "string",
            "type": "string",
            "nullable": true,
            "description": "string"
            }}
        ],
        "primary_key": ["string"],
        "indexes": ["string"]
        }}
    ],
    "relationships": [
        {{
        "table": "string",
        "field": "string",
        "linked_table": "string",
        "linked_field": "string"
        }}
    ],
    "partitioning_strategy": ["string"],
    "caching_strategy": ["string"]
    }}
    Guidelines:
    - Design tables that support the API contracts.
    - Keep table names practical, such as users, drivers, rides, payments, locations, ratings, and notifications.
    - Include important fields only.
    - Include primary keys.
    - Include indexes for high-read or high-filter fields.
    - Include relationships between tables.
    - Include partitioning strategy for high-volume tables such as rides, payments, and location updates.
    - Include caching strategy for frequently accessed data.
    - Prefer PostgreSQL for transactional data unless the architecture requires another database.
    - Mention Redis only in caching_strategy, not as a relational table.
    - Keep the output realistic for an MVP but scalable enough for production growth.
    - primary_key must always be a JSON array of field names, even when there is only one primary key column.
    - relationships must always be a JSON array of objects with table, field, linked_table, and linked_field.
    - partitioning_strategy must always be included. Use an empty array if no partitioning is needed.
    - caching_strategy must always be included. Use an empty array if no caching is needed.
    - primary_key must always be a JSON array of field names.
    Original user request:
    "{user_prompt}"
    Structured requirements:
    {requirements_json}
    Backend architecture:
    {architecture_json}
    API design:
    {api_design_json}
    """