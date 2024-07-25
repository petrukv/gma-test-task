import os

from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField
from dotenv import load_dotenv


load_dotenv()

db = PostgresqlDatabase(
    os.getenv('DB_NAME'), 
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT'))
)

class BaseModel(Model):
    class Meta:
        database = db

class ApiUser(BaseModel):
    name = CharField()
    email = CharField()
    password = CharField()

class Location(BaseModel):
    name = CharField()

class Device(BaseModel):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref='devices')
    api_user = ForeignKeyField(ApiUser, backref='devices')
