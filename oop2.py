class Car(object):
  def __init__(self, model=None, car_type=None, name=None):
    self.model = model
    self.car_type = car_type
    self.name = name
    
honda = Car("honda")
print(isinstance(honda, Car))