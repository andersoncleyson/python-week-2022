from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select

class Beer(SQLModel, table=True):
  id: Optional[int] = Field(primary_key=True, default=None, index=True)
  name: str
  style: str
  flavor: int
  image: int
  cost: int

#Objeto
brewdog = Beer(name="Sewdog", style="NEIPA", flavor=6, image=8, cost=10)
  