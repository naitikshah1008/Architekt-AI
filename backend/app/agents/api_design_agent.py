import json

from app.prompts.api_design_prompt import build_api_design_prompt
from app.schemas.api_design import APIDesignSpec
from app.schemas.architecture import ArchitectureSpec
from app.schemas.requirement import RequirementSpec
from app.services.llm_service import LLMService

class APIDesignAgent:
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def run(
        self,
        user_prompt: str,
        requirements: RequirementSpec,
        architecture: ArchitectureSpec
    ) -> APIDesignSpec:
        prompt = build_api_design_prompt(user_prompt, requirements, architecture)
        raw_output = self.llm_service.generate(prompt)
        try:
            parsed_output = json.loads(raw_output)
            return APIDesignSpec(**parsed_output)
        except Exception as exc:
            raise ValueError(
                f"Failed to parse API Design Agent output.\nRaw output:\n{raw_output}"
            ) from exc