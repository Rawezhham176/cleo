from utils.extensions import db
import uuid

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.String(36), primary_key=True, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self,username, password):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.password = password

