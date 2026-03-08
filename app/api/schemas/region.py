from pydantic import BaseModel


class Region(BaseModel):

    id: str

    name: str

    country: str

    language: str

    latitude: float

    longitude: float

    timezone: str

    priority: int

    active: bool