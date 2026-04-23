
market =["Yam", "Tomato", "Onion"]
market.append("Fish")
print(market)

grades =[80, 90, 70]
grades.insert(1, 85)
print(grades)

gadgets = ["Laptop", "Phone", "Tablet", "Phone"]
gadgets.remove("Phone")
print(gadgets)

colors = ["Red", "Blue", "Green"]
colors.clear()
print(colors)

votes = ["Yes", "No", "Yes", "Yes", "No"]
votes.count("Yes")
print(votes)

alphabets = ["a", "b", "c", "d", "e", "f"]
alphabets[2:5]
print(alphabets)

students = ["Kofi", "Ama", "Yaw"]
students.reverse()
print(students)

list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list)

cities = ["Accra", "Kumasi", "Tamale"]
removed_city = cities.pop(2)
print(cities)

items = ["Pen", "Ruler", "Eraser"]
items.index("Ruler")
print(items)

student_info = ("Araba", 20)
print("11: original tuple =", student_info)

tup = (1, 2, 3)
temp = list(tup)
temp.append(4)
tup = tuple(temp)
print("12:", tup)

data = (10, 20, 10, 30, 10)
count_10 = data.count(10)
print("13:", count_10)

colors_tuple = ("Red", "Blue", "Green")
blue_index = colors_tuple.index("Blue")
print("14:", blue_index)

coords = (5.6, -0.1)
lat, lon = coords
print("15: lat =", lat, ", lon =", lon)

nest = []
nest.append((5, 10))
nest_length = len(nest)
print("16:", nest_length)

numbers = (10, 20, 30, 40, 50)
last_two = numbers[-2:]
print("17:", last_two)

my_list = [1, 2]
my_list.extend((3, 4))
print("18:", my_list)

my_tup = (1, 2, 3)
del my_tup
print("19: tuple deleted")

x = (5)
y = (5,)
print("20: type(x) =", type(x), "| type(y) =", type(y))                         
    
  