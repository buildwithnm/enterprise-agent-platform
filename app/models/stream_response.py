from pydantic import BaseModel


class StreamChunk(BaseModel):

    token: str
    finished: bool
