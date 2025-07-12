text = ["apple", "34", "banana", "100", "abc", "75"]

natija = list(filter(
    lambda n: n.isdigit() == True,
    text
))
print(natija)
