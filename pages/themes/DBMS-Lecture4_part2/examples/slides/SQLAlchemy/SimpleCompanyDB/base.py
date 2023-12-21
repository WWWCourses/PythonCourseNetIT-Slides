# from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




#Create engine with MySQL dialect:
engine = create_engine(
    'mysql+pymysql://demo:123@localhost/SimpleCompanyDB?charset=utf8',
    connect_args = {
        # 'port': 3306
    },
    # echo='debug',
    echo_pool=True
)

# test the connection - get tables names:
print("Tables in SimpleCompanyDB: ",engine.table_names())
# Tables in SimpleCompanyDB:  ['company', 'company_employee', 'employee']

# print( dir(engine) )


Base = declarative_base()
Metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine)