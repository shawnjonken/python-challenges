fruits= ["apple","banana","cherry"]
for fruit in fruits:
    print(f"I love {fruit}.So much")
numbers = [1,2,3,4,5,6]
for number in range (1,10):
    if number == 5:
      print("Breaking loop at 5")
    elif number % 2==0:
       print(f"Exit the loop because it is even")
  

for i in range (1,4):
   for j in range (1,4):
      print(f"outer loop:{i},inner loop:{j}")
