from pydantic import BaseModel

class CustomerCreate(BaseModel):
    customer_name: str
    email: str
    phone_number: str
    customer_id: int
    

class UpdatePhone(BaseModel):
    phone_number: str