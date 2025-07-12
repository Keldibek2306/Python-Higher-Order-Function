nums = list(range(1, 21))

juft_sonlar = list(filter(
    lambda n: n % 2 == 0,
    nums
))
kvadratlar = list(map(
    lambda k: k **2,
    juft_sonlar
))
print("juft sonlar ==>", juft_sonlar)
print("kvadrat ==>", kvadratlar)