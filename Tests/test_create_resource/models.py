from  pydantic import BaseModel

class bodyModel(BaseModel):
    title: str
    body: str
    userId: str

