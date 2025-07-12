data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

text = list(filter(
    lambda x: isinstance(x, str) and x.isalpha(),
    data
))
print(text)
