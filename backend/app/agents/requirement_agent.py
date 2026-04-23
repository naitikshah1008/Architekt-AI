import json

from app.prompts.requirement_prompt import build_requirement_prompt
from app.schemas.requirement import RequirementSpec
from app.services.llm_service import LLMService

class RequirementAgent:
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def run(self, user_prompt: str) -> RequirementSpec:
        prompt = build_requirement_prompt(user_prompt)
        raw_output = self.llm_service.generate(prompt)
        try:
            parsed_output = json.loads(raw_output)
            return RequirementSpec(**parsed_output)
        except Exception as exc:
            raise ValueError(
                f"Failed to parse Requirement Agent output.\nRaw output:\n{raw_output}"
            ) from exc