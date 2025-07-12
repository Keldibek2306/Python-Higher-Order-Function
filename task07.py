prices = ["$120", "$340", "$50", "$90"]

natija = map(
    lambda n: float(n.replace("$", "")),
    prices 
)
print(list(natija))