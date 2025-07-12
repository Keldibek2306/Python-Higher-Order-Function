people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

tartiblash = sorted(people, key=lambda n: n["age"]

)

print(tartiblash)