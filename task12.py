students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

natija = list(sorted(students, key = lambda n: n['grade']
))

print(natija)