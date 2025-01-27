from pydantic import BaseModel

from .core.messages.request_message import RequestMessage


class BorderParameters(BaseModel):
    messageId: str
    user_id: str
    project_id: str
    inputImageURI: str
    configValue: float 
    configColor: str # Not used in this tool

BorderRequestMessage = RequestMessage[BorderParameters]
