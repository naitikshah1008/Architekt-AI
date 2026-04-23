from pydantic import BaseModel

class DesignRequest(BaseModel):
    prompt: str