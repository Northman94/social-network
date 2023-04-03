import os
from dotenv import load_dotenv
from sqlalchemy import URL



# load environment variables from .env
load_dotenv()


class Config:
    """
    Base configuration class
    """

    # read from .env file
    SECRET_KEY = os.getenv("SECRET_KEY")
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///network.db'

    SQLALCHEMY_DATABASE_URI = URL.create(
    "postgresql",
    username="postgres",
    password="postgres",  # plain (unescaped) text
    host="localhost",
    port="54321",
    database="postgres",
)
