# Excercise 1 
students = ['Elroy','Ivan', 'Shamique', 'Mark']
print(students[-1], students[1])

# Excercise 2
foods = ('Chinese', 'Peruvian', 'Brazilian','Greek')
for i in foods:
    print(f"{i} is a good type of food")

# Excercise 3
for i in foods:
    break
print(f"{foods[-1]} is a good type of food and {foods[-2]}") 
    
# Excercise 4

home_town = {
  'city': 'Jackson Heights',
  'state': 'New york',
  'population': '8.419 million'
} 
print(f" I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Excercise 5

for key, val in home_town.items():
    print(f"{key} = {val}")

# Excercise 6

cohort = []
for index, student in enumerate(students):
  cohort.append({
    'student': student,
    'fav_food': foods[index]
  })

for student in cohort:
  print(student)

# Excercise 7

awesome_students = [ f"{name} is the awesomest!" for name in students ]

for students in awesome_students:
    print(students)

# Excercise 8

for food in [food for food in foods if 'a' in food]:
  print(food)

