from pydantic import BaseModel


class Layout(BaseModel):

    id: str

    type: str

    style: str

    active: bool