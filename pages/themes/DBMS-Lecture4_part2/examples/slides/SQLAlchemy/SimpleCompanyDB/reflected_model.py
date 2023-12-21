from base import Session, engine, Base, Metadata
from sqlalchemy import MetaData, Table


# print table names:
# print( engine.table_names() )

#Reflect each database table we need to use, using Metadata


# employee = Table('employee', Metadata, autoload=True, autoload_with=engine)
class Employee(Base):
    __table__ = Table('employee', Metadata, autoload=True)

    def __init__(self, employee_name):
        self.employee_name = employee_name

# company = Table('company', Metadata, autoload=True, autoload_with=engine)
class Company(Base):
    __table__ = Table('company', Metadata, autoload=True)

    def __init__(self, company_name):
        self.company_name = company_name



# for c in Employee.__table__.columns:
#   print(c)







# insert a record:
# ins = employee.insert().values(employee_name='Pesho')
# print(ins)

# Session = sessionmaker(bind=engine)
