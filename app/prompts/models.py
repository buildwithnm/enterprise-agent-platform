from pydantic import BaseModel

class PromptDefinition(BaseModel):

    name: str
    version: str
    description: str
    system: str