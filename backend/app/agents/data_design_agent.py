import json

from app.prompts.data_design_prompt import build_data_design_prompt
from app.schemas.api_design import APIDesignSpec
from app.schemas.architecture import ArchitectureSpec
from app.schemas.data_design import DataDesignSpec
from app.schemas.requirement import RequirementSpec
from app.services.llm_service import LLMService

class DataDesignAgent:
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def run(
        self,
        user_prompt: str,
        requirements: RequirementSpec,
        architecture: ArchitectureSpec,
        api_design: APIDesignSpec
    ) -> DataDesignSpec:
        prompt = build_data_design_prompt(
            user_prompt,
            requirements,
            architecture,
            api_design
        )
        raw_output = self.llm_service.generate(prompt)
        try:
            parsed_output = json.loads(raw_output)
            return DataDesignSpec(**parsed_output)
        except Exception as exc:
            raise ValueError(
                f"Failed to parse Data Design Agent output.\n"
                f"Error: {str(exc)}\n"
                f"Raw output:\n{raw_output}"
            ) from exc