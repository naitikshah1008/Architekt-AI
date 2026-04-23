from pydantic import BaseModel
from typing import List

class RequirementSpec(BaseModel):
    system_name: str
    actors: List[str]
    functional_requirements: List[str]
    non_functional_requirements: List[str]
    scale_assumptions: List[str]
    constraints: List[str]
    open_questions: List[str]