from base import Session, engine, Base
from reflected_model import Company,Employee

# generate database schema
Base.metadata.create_all(engine)

# create a new session
session = Session()

# insert data
microsoft = Company("Microsoft")
btc = Company("BTC")

stoyan = Employee("Stoyan Vasilev")




# persists data
session.add(microsoft)
session.add(stoyan)
session.add(btc)

# commit and close session
session.commit()
session.close()