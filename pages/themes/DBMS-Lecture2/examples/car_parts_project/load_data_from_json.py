from mongoengine import connect
from mongoengine.errors import ValidationError

from lib.model import CarParts, Users, Orders
import json
import sys

connect(db='car_parts_shop')

def save_doc(obj):
	try:
		obj.save()
	except Exception as e:
		print('Error on', obj.to_json())
		print(e)
		# sys.exit()

car_parts = [
	{
	  "code": 1,
	  "product_name": "BRAKE DISC",
	  "category": "BRAKING SYSTEM",
	  "buying_price": 45.88,
	  "client_price": 65.5,
	  "application": "MITSUBISHI SPACE STAR 1.6, 2002",
	  "manufacturer": "ABE"
	},
	{
	  "code": 2,
	  "product_name": "FRONT BRAKE PADS SET",
	  "category": "BRAKING SYSTEM",
	  "buying_price": 24,
	  "client_price": 35.86,
	  "application": "AUDI A6 3.0D, 2015",
	  "manufacturer": "STARLINE"
	},
	{
	  "code": 3,
	  "product_name": "CRANKSHAFT POSITION SENSOR",
	  "category": "IGNITION SYSTEM",
	  "buying_price": 125.47,
	  "client_price": 184,
	  "application": "MERCEDES-BENZ CLK 220, 2007",
	  "manufacturer": "OE MERCEDES"
	},
	{
	  "code": 4,
	  "product_name": "FUEL PRESSURE REGULATOR",
	  "category": "FUEL SYSTEM",
	  "buying_price": 98.22,
	  "client_price": 132.22,
	  "application": "RENAULT MAGANE 1.9 DCI, 2008",
	  "manufacturer": "SENSATA"
	},
	{
	  "code": 5,
	  "product_name": "EXHAUST GAS RECIRCULATION(EGR) VALVE",
	  "category": "EXHAUST SYSTEM",
	  "buying_price": 217,
	  "client_price": 302.56,
	  "application": "VOLKSWAGEN BORA 1.9TDI, 2008",
	  "manufacturer": "NRF"
	},
	{
	  "code": 6,
	  "product_name": "END-SPRINDLE ROD",
	  "category": "STEERING SYSTEM",
	  "buying_price": 28.66,
	  "client_price": 37.11,
	  "application": "CITROEN C3 1.4HDI, 2009",
	  "manufacturer": "TRW"
	},
	{
	  "code": 7,
	  "product_name": "STABILIZER ROD CONNECTOR",
	  "category": "STABILITY SYSTEM",
	  "buying_price": 11.26,
	  "client_price": 18,
	  "application": "OPEL CORSA D 1.0 ECOTEC, 2012",
	  "manufacturer": "MOOG"
	},
	{
	  "code": 8,
	  "product_name": "FRONT BEARING",
	  "category": "DRIVE SHAFT",
	  "buying_price": 66.55,
	  "client_price": 81.35,
	  "application": "PEUGEOT 307 1.6HDI, 2009",
	  "manufacturer": "FAG"
	},
	{
	  "code": 9,
	  "product_name": "OIL PAN",
	  "category": "OIL SYSTEM",
	  "buying_price": "124.10",
	  "client_price": "171.25",
	  "application": "HONDA ACCORD 2.4 VTEC, 2010",
	  "manufacturer": "STAL"
	},
	{
	  "code": 10,
	  "product_name": "WATER PUMP",
	  "category": "COOLING SYSTEM",
	  "buying_price": 88.98,
	  "client_price": 135.68,
	  "application": "TOYOTA RAV4 2.2 D-CAT. 2002",
	  "manufacturer": "AISIN"
	},
	{
	  "code": 11,
	  "product_name": "SHORT BLOCK ASSEMBLY",
	  "category": "ENGINE",
	  "buying_price": "2259.65",
	  "client_price": "3098.58",
	  "application": "VOLKSWAGEN GOLF VII 1.8TFSI, 2017",
	  "manufacturer": "OE VW"
	},
	{
	  "code": 12,
	  "product_name": "AIR FILTER",
	  "category": "INTAKE SYSTEM",
	  "buying_price": 22.36,
	  "client_price": 32.75,
	  "application": "SUZUKI BALENO 1.3, 2000",
	  "manufacturer": "FILTRON"
	},
	{
	  "code": 13,
	  "product_name": "SPARK PLUG",
	  "category": "IGNITION SYSTEM",
	  "buying_price": 13.56,
	  "client_price": 27.2,
	  "application": "SEAT IBIZA 1.6SR, 2005",
	  "manufacturer": "NGK"
	},
	{
	  "code": 14,
	  "product_name": "IGNITION COIL",
	  "category": "IGNITION SYSTEM",
	  "buying_price": 100.05,
	  "client_price": 142,
	  "application": "OPEL ASTRA H 1.2, 2007",
	  "manufacturer": "BOSCH"
	},
	{
	  "code": 15,
	  "product_name": "FUEL INJECTOR",
	  "category": "FUEL SYSTEM",
	  "buying_price": 255.2,
	  "client_price": 326,
	  "application": "TOYOTA AVENSIS 2.0 D4D, 2006",
	  "manufacturer": "SIEMENS"
	},
	{
	  "code": 16,
	  "product_name": "TIMING BELT SET",
	  "category": "VALVE TIMING",
	  "buying_price": 332.25,
	  "client_price": 469.23,
	  "application": "PEUGEOT 206CC 1.4I, 2004",
	  "manufacturer": "CONTINENTAL"
	},
	{
	  "code": 17,
	  "product_name": "STEERING SERVO PUMP",
	  "category": "STEERING SYSTEM",
	  "buying_price": "1200.00",
	  "client_price": "1566.54",
	  "application": "DAIHATSU SIRION 1.3, 2009",
	  "manufacturer": "TRW"
	},
	{
	  "code": 18,
	  "product_name": "INTAKE MANIFOLD",
	  "category": "INTAKE SYSTEM",
	  "buying_price": 202.44,
	  "client_price": 293.16,
	  "application": "FORD FOCUS 1.8 DURATEC, 2001",
	  "manufacturer": "FoMoCo"
	},
	{
	  "code": 19,
	  "product_name": "CLUTCH SET",
	  "category": "CLUTCH SYSTEM",
	  "buying_price": "2155.25",
	  "client_price": "3000.00",
	  "application": "PORSCHE CAYENNE 3.0D, 2010",
	  "manufacturer": "VALEO"
	},
	{
	  "code": 20,
	  "product_name": "SHOCK ABBSORBER",
	  "category": "SUSPENSION",
	  "buying_price": 65.21,
	  "client_price": 92.88,
	  "application": "SKODA FABIA 1.9D, 2001",
	  "manufacturer": "MONROE"
	}
]

users = [
	{
	  "role": "admin",
	  "first_name": "dimitar",
	  "last_name": "hristov",
	  "email": "d@abv.bg",
	  "phone_number": "0884156033",
	  "password":  1234,
	  "created": "2021-05-24 21:30:37.397451"
	},
	{
	  "role": "user",
	  "first_name": "vladimir",
	  "last_name": "hristov",
	  "email": "v@mail.bg",
	  "phone_number": "8888889999",
	  "password":  "2222",
	  "created": "2021-05-24 21:38:40.624541"
	},
	{
	  "role": "admin",
	  "first_name": "sonya",
	  "last_name": "hristova",
	  "email": "sss@abv.bg",
	  "phone_number": "122222",
	  "password":  "666",
	  "created": "2021-05-24 21:42:55.790872"
	},
	{
	  "role": "user",
	  "first_name": "ivan",
	  "last_name": "simeonov",
	  "email": "i@abv.bg",
	  "phone_number": "4569876321",
	  "password":  "6395",
	  "created": "2021-05-24 21:44:59.797622"
	},
	{
	  "role": "user",
	  "first_name": "ilia",
	  "last_name": "petkov",
	  "email": "iiiid@abv.bg",
	  "phone_number": "0888888888",
	  "password":  "5558",
	  "created": "2021-06-14 13:32:11.157105"
	},
	{
	  "role": "user",
	  "first_name": "petranka",
	  "last_name": "pavlova",
	  "email": "aaa@abv.bg",
	  "phone_number": "123365874532.",
	  "password":  "9698",
	  "created": "2021-06-14 10:35:50.143717"
	},
	{
	  "role": "user",
	  "first_name": "lop",
	  "last_name": "hop",
	  "email": "kiro@awe.com",
	  "phone_number": "458955",
	  "password":  "4785",
	#   "created": "14/06/2021"
	},
	{
	  "role": "user",
	  "first_name": "mkii",
	  "last_name": "lnjkbgukn",
	  "email": "ijbyuikl",
	  "phone_number": "kkbiubujnlkl",
	  "password": "ihiohio",
	#   "created": "14.06.2021/Jun/06in"
	},
	{
	  "role": "knkl",
	  "first_name": "knbiyfyukjl",
	  "last_name": "byuhvvkuygkhl",
	  "email": "lkjiugyutcyg",
	  "phone_number": "huyjkl",
	  "password": "oinubihujkl;",
	  "created": "14.06.2021/13/47"
	},
	{
	  "role": "dsad",
	  "first_name": "ds",
	  "last_name": "a",
	  "email": "",
	  "phone_number": "saf",
	  "password": "s",
	  "created": "14.06.2021/13:48:30"
	}
]

orders = [
	{
	  "date": "2021-05-27 21:43:13.069922",
	  "user": "vladimir",
	  "ordered_parts": "BRAKE DISC",
	  "total_costs": 65.5,
	  "profit": 19.619999999999997
	},
	{
	  "date": "2021-05-27 21:44:04.966025",
	  "user": "dimitar",
	  "ordered_parts": "BRAKE DISC,FRONT BRAKE PADS SET,CRANKSHAFT POSITION SENSOR",
	  "total_costs": 285.36,
	  "profit": 90.00999999999999
	},
	{
	  "date": "2021-05-27 21:50:39.212503",
	  "user": "vladimir",
	  "ordered_parts": "SPARK PLUG",
	  "total_costs": 27.2,
	  "profit": 13.639999999999999
	}
]


# Load data
for cp in car_parts:
	cp['__auto_convert'] = True
	obj = CarParts(**cp)
	save_doc(obj)

for u in users:
	u['__auto_convert'] = True
	obj = Users(**u)
	save_doc(obj)

for o in orders:
	o['__auto_convert'] = True
	user_name = o['user']
	user_id=Users.objects(first_name=user_name).first().id
	# print( user_id )
	obj = Orders(**o)
	obj.user = user_id
	save_doc(obj)






