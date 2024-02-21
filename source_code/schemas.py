from pydantic import BaseModel, ConfigDict


class Book(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    year: int
    is_loaned: bool
