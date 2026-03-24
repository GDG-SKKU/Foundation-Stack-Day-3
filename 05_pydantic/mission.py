from pydantic import BaseModel


class Member(BaseModel):
    pass  # 여기를 채워보세요!

m = Member(username="alice", age=20)
print(m)  # point=0, is_premium=False 가 자동으로!
