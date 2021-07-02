from sqlalchemy import *
# from sqlalchemy import Session, engine, Base, Metadata
# from sqlalchemy import MetaData, Table


#Create engine with MySQL dialect:
engine = create_engine(
    'mysql+pymysql://demo:123@localhost/SimpleCompanyDB?charset=utf8',
    connect_args = {
        # 'port': 3306
    },
    # echo='debug',
    echo_pool=True
)

Base = Base.declarative_base()
Metadata = MetaData(bind=engine)

# test the connection - get tables names:
print("Tables in SimpleCompanyDB: ",engine.table_names())


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



for c in Employee.__table__.columns:
  print(c)







# insert a record:
# ins = employee.insert().values(employee_name='Pesho')
# print(ins)

# Session = sessionmaker(bind=engine)
