class Animal:
  def __init__(self):
    self.num_eyes = 2
   
  def breathe(self):
       print("inhale, exhale.")
       

class Fish(Animal):
  
  def __init__(self):   
     super().__init__() 
    #  this helps to inherit all the stuff from the super class Animal, into the fish class
  
  def swim(self):
    print("moving in water.")
    
  def breathe(self):
      super().breathe() 
      print("doing this underwater.") 
      # we can update the existing method inside the child class Fish too
    
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)