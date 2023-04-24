class Car:
   def __init__(self, engine):
      self.engine = engine
   def run(self):
       self.engine.start()

class Engine:
  def start(self):
    print("Engine started!")

trinity5_8 = Engine()
ford = Car(trinity5_8)

ford.run()