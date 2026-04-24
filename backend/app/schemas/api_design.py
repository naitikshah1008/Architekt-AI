from pydantic import BaseModel
from typing import Any, Dict, List

class EndpointSpec(BaseModel):
    service_name: str
    method: str
    path: str
    purpose: str
    request_schema: Dict[str, Any]
    response_schema: Dict[str, Any]
    validation_rules: List[str]

class APIDesignSpec(BaseModel):
    endpoints: List[EndpointSpec]