from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String



#Create engine with MySQL dialect:
engine = create_engine(
    'mysql+pymysql://pythontest:123@localhost/SimpleCompanyDB?charset=utf8'
)

# test the connection - get tables names:
print("Tables in SimpleCompanyDB: ",engine.table_names())
# Tables in SimpleCompanyDB:  ['company', 'company_employee', 'employee']


Base = declarative_base()
# Metadata = MetaData(bind=engine)
# Session = sessionmaker(bind=engine)