from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float


Base = declarative_base()

class Salaries(Base):
  """docstring for Salaries"""
  __tablename__ = "salaries"

  id = Column(Integer, primary_key=True)
  employee_id = Column(Integer)
  salary = Column(Float)

  def __repr__(self):
    return "employee_id: {}; salary: {}".format(self.employee_id, self.salary)


print(Salaries.__table__)