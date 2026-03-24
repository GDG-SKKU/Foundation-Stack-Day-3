from pydantic import BaseModel, Field


class Member(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=14)
    point: int = Field(default=0)
    is_premium: bool = Field(default=False)

m = Member(username="alice", age=20)
print(m)  # point=0, is_premium=False 가 자동으로!
