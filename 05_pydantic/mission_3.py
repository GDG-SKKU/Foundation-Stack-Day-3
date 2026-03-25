from pydantic import BaseModel, Field, field_validator

class SignUp(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=8)
    age:      int = Field(gt=0)

    # 여기에 field_validator를 추가해서
    # username에 특수문자(!@#$ 등)가 들어오면 에러가 나게 만들어보세요!
    @field_validator("username")
    @classmethod
    def username_must_be_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError("username은 영숫자만 사용 가능합니다")
        return v

# 테스트
s1 = SignUp(username="alice123", password="pass1234", age=20)
print(s1)  # 정상 출력

s2 = SignUp(username="ali ce!", password="pass1234", age=20)