import json

from app.prompts.architecture_prompt import build_architecture_prompt
from app.schemas.architecture import ArchitectureSpec
from app.schemas.requirement import RequirementSpec
from app.services.llm_service import LLMService

class ArchitectureAgent:
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def run(self, user_prompt: str, requirements: RequirementSpec) -> ArchitectureSpec:
        prompt = build_architecture_prompt(user_prompt, requirements)
        raw_output = self.llm_service.generate(prompt)
        try:
            parsed_output = json.loads(raw_output)
            return ArchitectureSpec(**parsed_output)
        except Exception as exc:
            raise ValueError(
                f"Failed to parse Architecture Agent output.\nRaw output:\n{raw_output}"
            ) from exc