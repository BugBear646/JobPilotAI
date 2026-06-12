from typing import Optional
from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    company: str
    title: str
    url: str

    location: Optional[str] = None
    description: Optional[str] = None

    platform: str = "LinkedIn"

    employment_type: Optional[str] = None

    work_mode: Optional[str] = None


class JobResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    company: str

    title: str

    url: str

    location: Optional[str]

    description: Optional[str]

    platform: str

    employment_type: Optional[str]

    work_mode: Optional[str]

    match_score: float

    status: str