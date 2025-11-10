import numpy as np

#create a simple array 
my_array=np.array([1,2,3,4,5])
print("Array:", my_array)

#perform basic operations
print("Mean:", np.mean(my_array))

#creating a 50 array
range_array = np.arange(10,51)

# find max/min values
print("my_array max:", my_array.max())
print("my_array min:", my_array.min())

print("range_array max:", range_array.max())
print("range_array min:", range_array.min())

#mulltiplying all elements by 3
multiplied_array = my_array * 3
print("Multiplied Array:", multiplied_array)

import pandas as pd
# create a dataframe(table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
#accessing specific columns
print("Names:", df['Name'])

#filtering rows where Age > 25
filtered_df = df[df['Age'] > 25]
print("Filtered DataFrame (Age > 25):")
print(filtered_df)


import matplotlib.pyplot as plt
#simple line plot   
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()  
#simple bar chart
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]
plt.bar(categories, values)
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

import pandas as pd

# Create a DataFrame
data = {
    'Year': [2021, 2022, 2023],
    'Users': [1500, 3000, 5000]
}

df = pd.DataFrame(data)

# Plot using pandas + matplotlib
plt.plot(df['Year'], df['Users'], marker='o')
plt.title("User Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
countries = ['USA', 'colombus', 'Germany', 'France','ethiopia']
populations = [331, 50, 83, 67, 120]  # in millions
plt.bar(countries, populations, color='green')
plt.title("Population by Country")
plt.xlabel("Countries") 
plt.ylabel("Population (in millions)")
plt.show()

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
plt.figure()  # Create a new figure
spending = [2,6,7,7,9] #in hours per day
plt.pie(spending, labels=students, autopct='%1.1f%%', startangle=140)
plt.title("Daily Study Time of Students")
plt.show()

# Line chart of temperatures (weekly example)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures_c = [22, 21, 23, 24, 26, 25, 23]  # Celsius

plt.figure(figsize=(8,4))
plt.plot(days, temperatures_c, marker='o', linestyle='-', color='tomato')
plt.title("Weekly Temperatures")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

