from datetime import datetime

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict


class FlowerReceptionCreate(BaseModel):
    lot_code: str = Field(min_length=5, max_length=40)
    supplier: str = Field(min_length=2, max_length=120)
    strain: str = Field(min_length=2, max_length=120)
    weight_grams: float = Field(gt=0)
    received_at: datetime
    notes: str | None = None


class ExtractBatchCreate(BaseModel):
    lot_code: str = Field(min_length=5, max_length=40)
    source_lot_code: str = Field(min_length=5, max_length=40)
    method: str = Field(min_length=2, max_length=40)
    status: str = Field(min_length=2, max_length=40)
    input_grams: float = Field(gt=0)
    output_grams: float = Field(gt=0)
    started_at: datetime
    finished_at: datetime | None = None
    notes: str | None = None


class SupplyCreate(BaseModel):
    code: str = Field(min_length=3, max_length=40)
    name: str = Field(min_length=2, max_length=120)
    unit: str = Field(min_length=1, max_length=20)
    current_stock: float = Field(ge=0)
    minimum_stock: float = Field(ge=0)


class SupplyMovementCreate(BaseModel):
    movement_type: str = Field(pattern="^(in|out|adjust)$")
    quantity: float = Field(gt=0)
    reason: str = Field(min_length=2, max_length=255)

