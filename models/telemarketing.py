from pydantic import BaseModel

class Telemarketing(BaseModel):
    age: int | None = None
    job: str | None = None
    marital: str | None = None
    education: str | None = None
    default: str | None = None
    balance: int | None = None
    housing: str | None = None
    loan: str | None = None
    contact: str | None = None
    month: str | None = None
    day: int | None = None
    duration: int | None = None
    campaign: int | None = None
    pdays: int | None = None
    previous: int | None = None
    poutcome: str | None = None
    