from pydantic import BaseModel

from .core.messages.request_message import RequestMessage


class BorderParameters(BaseModel):
    inputImageURI: str
    outputImageURI: str
    bSize: int 
    bColor: str

BorderRequestMessage = RequestMessage[BorderParameters]
