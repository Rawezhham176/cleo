import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database', 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "5e89c7d3b8f2491b8fdc7a0deabe3e98ed31e08c01a42d871579b045798217aa")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "7c03c9f6eaed4e298c8f760bfbed2a2334eebf9dc96c2c1f9e2dc6fa4b39f3c1")
