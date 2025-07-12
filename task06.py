emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

natija = list(filter(
    lambda n: n.endswith("@gmail.com"),
    emails
))

print(natija)