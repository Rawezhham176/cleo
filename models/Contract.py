from datetime import datetime
from utils.extensions import db
from sqlalchemy import ForeignKey

class Contract(db.Model):
    __tablename__ = "contract"

    contract_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    contract_name = db.Column(db.String(80), nullable=False)
    customer_id = db.Column(db.String(36), ForeignKey("customer.customer_id"), nullable=False)
    date_created = db.Column(db.String(36), nullable=False)

    def __init__(self,contract_name, customer_id):
        self.contract_name = contract_name
        self.customer_id = customer_id
        self.date_created = datetime.now().strftime("%Y-%m-%d")

