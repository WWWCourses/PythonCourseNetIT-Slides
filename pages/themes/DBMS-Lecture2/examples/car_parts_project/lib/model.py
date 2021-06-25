from enum import Enum, unique
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, DecimalField, DynamicField, EmailField, EnumField, FloatField, IntField, ReferenceField, StringField
from datetime import datetime


class Role(Enum):
	ADMIN="admin"
	USER="user"

class CarParts(Document):
	meta={'collection':'car_parts'}

	code = IntField(unique=True)
	product_name = StringField(min_length=1, max_length=200)
	category = StringField(min_length=1, max_length=200)
	buying_price = DecimalField(min_value=0, precision=2)
	client_price = DecimalField(min_value=0, precision=2)
	application = StringField(min_length=1, max_length=200)
	manufacturer = StringField(min_length=1, max_length=100)

class Orders(Document):
	date = DateTimeField(required=True, default=datetime.utcnow)
	user =  ReferenceField('Users')
	ordered_parts =  StringField(min_length=1, max_length=200)
	total_costs =  DecimalField(min_value=0, precision=2)
	profit =  FloatField()

class Users(Document):
	role = EnumField(Role, default=Role.USER)
	first_name = StringField(min_length=1, max_length=200)
	last_name = StringField(min_length=1, max_length=200)
	email = EmailField(allow_utf8_user=True, unique = True)
	phone_number = StringField(regex=r"\d{3,}")
	password = DynamicField(max_length=100)
	created = DateTimeField(default=datetime.utcnow)
