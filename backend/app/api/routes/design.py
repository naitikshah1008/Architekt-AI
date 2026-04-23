from fastapi import APIRouter, HTTPException

from app.agents.requirement_agent import RequirementAgent
from app.schemas.design_request import DesignRequest
from app.services.llm_service import LLMService

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