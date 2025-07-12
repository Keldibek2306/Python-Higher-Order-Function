sentence = "Functional programming in Python is very powerful and elegant"

soz = sentence.split()

uzun_sozlar = sorted(
    soz, key = lambda u: len(u), reverse = True)[:3]
print(uzun_sozlar)