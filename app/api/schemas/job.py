from pydantic import BaseModel


class Job(BaseModel):

    region_id: str

    status: str

    forecast_type: str