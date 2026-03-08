from pydantic import BaseModel


class Voice(BaseModel):

    id: str

    language: str

    gender: str

    style: str

    energy: str

    active: bool