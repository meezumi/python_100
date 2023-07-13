class User: 
  # PascalCase naming 
  # camelCase naming 
  # snake_case naming
  
    # this is a constructor, init function 
  def __init__(self, user_id, username): 
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0
    # for every object the followers will be set to 0 initially 
    
  # when a function is attached to a class its called a method
  def follow(self, user):
    user.followers += 1
    self.following += 1
    
    

user1 = User("001", "Aaryan")
# user1.id = "001"
user2 = User("002", "Khyaati")

user1.follow(user2)

print(user1.following)
print(user2.followers)


  
  
