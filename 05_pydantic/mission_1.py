from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class Product(BaseModel):
    name:        str   = Field(min_length=1)
    price:       float = Field(gt=0)
    stock:       int   = Field(ge=0)
    description: Optional[str] = None

# ① 정상 생성
p = Product(name="노트북", price=1200000, stock=5)
print(p)
print(p.model_dump())

# ② 에러 확인
try:
    Product(name="", price=-1000, stock=5)
except ValidationError as e: print(e)