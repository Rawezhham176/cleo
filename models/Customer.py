from utils.extensions import db


class Customer(db.Model):
    __tablename__ = "customer"

    customer_id =     contract_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    customer_name = db.Column(db.String(80), nullable=False)
    customer_surname = db.Column(db.String(80), nullable=False)
    customer_email = db.Column(db.String(80), nullable=True)
    customer_phone_number = db.Column(db.String(80), nullable=True)
    customer_address = db.Column(db.String(80), nullable=True)

    def __init__(self, customer_name,customer_surname, customer_email, customer_phone_number, customer_address):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_email = customer_email
        self.customer_phone_number = customer_phone_number
        self.customer_address = customer_address


