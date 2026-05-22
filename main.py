from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Customer
from schemas import CustomerCreate, UpdatePhone

#Create tables
Base.metadata.create_all(bind=engine)

#FastAPI object
app = FastAPI()

#Database session function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#ADD CUSTOMER
@app.post("/add_customer")
def add_customer(customer: CustomerCreate):

    db = SessionLocal()

    try:
        new_customer = Customer(
            customer_id=customer.customer_id,
            customer_name=customer.customer_name,
            email=customer.email,
            phone_number=customer.phone_number
        )

        db.add(new_customer)
        db.commit()

        return {"message": "Customer Added Successfully"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        db.close()


#VIEW ALL CUSTOMERS
@app.get("/customers")
def get_customers():

    db = SessionLocal()

    customers = db.query(Customer).all()

    db.close()

    return customers


#SEARCH CUSTOMER BY ID
@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):

    db = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()

    db.close()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer Not Found"
        )

    return customer


#UPDATE PHONE NUMBER
@app.put("/update_phone/{customer_id}")
def update_phone(customer_id: int, data: UpdatePhone):

    db = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()

    if customer is None:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="Customer Not Found"
        )

    customer.phone_number = data.phone_number

    db.commit()

    db.close()

    return {"message": "Phone Number Updated"}


#DELETE CUSTOMER
@app.delete("/delete_customer/{customer_id}")
def delete_customer(customer_id: int):

    db = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()

    if customer is None:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="Customer Not Found"
        )

    db.delete(customer)

    db.commit()

    db.close()

    return {"message": "Customer Deleted"}