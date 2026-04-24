from pydantic import BaseModel
from typing import List

class ServiceSpec(BaseModel):
    name: str
    responsibility: str

class CommunicationPattern(BaseModel):
    source: str
    target: str
    protocol: str
    reason: str

class ArchitectureSpec(BaseModel):
    services: List[ServiceSpec]
    communication_patterns: List[CommunicationPattern]
    databases: List[str]
    infrastructure_components: List[str]
    scalability_strategy: List[str]
    fault_tolerance_strategy: List[str]