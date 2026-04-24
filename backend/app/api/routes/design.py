from fastapi import APIRouter, HTTPException

from app.agents.requirement_agent import RequirementAgent
from app.schemas.design_request import DesignRequest
from app.services.llm_service import LLMService
from app.agents.architecture_agent import ArchitectureAgent
from app.agents.api_design_agent import APIDesignAgent

router = APIRouter()

@router.post("/requirements")
def generate_requirements(request: DesignRequest):
    try:
        llm_service = LLMService()
        requirement_agent = RequirementAgent(llm_service)
        result = requirement_agent.run(request.prompt)
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@router.post("/architecture")
def generate_architecture(request: DesignRequest):
    try:
        llm_service = LLMService()
        requirement_agent = RequirementAgent(llm_service)
        requirements = requirement_agent.run(request.prompt)
        architecture_agent = ArchitectureAgent(llm_service)
        architecture = architecture_agent.run(request.prompt, requirements)
        return {
            "requirements": requirements,
            "architecture": architecture
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@router.post("/api-design")
def generate_api_design(request: DesignRequest):
    try:
        llm_service = LLMService()
        requirement_agent = RequirementAgent(llm_service)
        requirements = requirement_agent.run(request.prompt)
        architecture_agent = ArchitectureAgent(llm_service)
        architecture = architecture_agent.run(request.prompt, requirements)
        api_design_agent = APIDesignAgent(llm_service)
        api_design = api_design_agent.run(
            request.prompt,
            requirements,
            architecture
        )
        return {
            "requirements": requirements,
            "architecture": architecture,
            "api_design": api_design
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))