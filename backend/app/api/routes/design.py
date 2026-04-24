from fastapi import APIRouter, HTTPException

from app.agents.requirement_agent import RequirementAgent
from app.schemas.design_request import DesignRequest
from app.services.llm_service import LLMService
from app.agents.architecture_agent import ArchitectureAgent

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