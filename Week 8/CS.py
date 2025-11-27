# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     'temperature': [23, 23, 21, 20, 19, 15, 12, 23, 25, 30],
#     'movement': [1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
# }

# df = pd.DataFrame(data)
# print(df)

# plt.figure(figsize=(10,5))
# plt.plot(df['temperature'], label="Temperature")
# plt.plot(df['movement'], label='Movement')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.title('Temperature and Movement Over Time')
# plt.legend()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     'temperature': [23, 23, 21, 20, 19, 15, 12, 23, 25, 30],
#     'movement': [1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
# }

# df = pd.DataFrame(data)
# print(df)

# plt.figure(figsize=(10, 6))

# # --- First subplot: Temperature ---
# plt.subplot(2, 1, 1)
# plt.plot(df['temperature'], color='red')
# plt.title('Temperature Over Time')
# plt.ylabel('Temperature')

# # --- Second subplot: Movement ---
# plt.subplot(2, 1, 2)
# plt.plot(df['movement'], color='blue')
# plt.title('Movement Over Time')
# plt.xlabel('Time')
# plt.ylabel('Movement')

# plt.tight_layout()  # Adjust spacing between subplots
# plt.show()

# import turtle

# sipi = turtle.Turtle() # creates a new object of a class
# sipi.shape('turtle') #method of the turtle class
# sipi.color('green')
# sipi.forward(100)

# turtle_screen = turtle.Screen() #an instance (or object / olio in finnish) of the screen class
# turtle_screen.exitonclick() # method

############################################################
class LABStudent:
    name: str #Attribute
    age: int #Attribute
    major: str #Attribute

    def introduce(self): #Method, ask the object to do something
        return (f"Hi, I'm {self,name}, {self.age} years old, majoring in {selfmajor}")
    
    def study(self)
        return f"Hi{self.name} is now studying {self.major}"
