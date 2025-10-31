test = [1,2,3,4,5,6,7,8,9,10]

print(test[-2])


# extends
num = [1,2,3]

num.extend([4,5,6])

print(num)

# map
num2 = [1,2,3,4,5]

hasil2 = list(map(lambda x: x * 2, num2))

print(hasil2)

# filter
num3 = [1,2,3,4,5]

hasil3 = list(filter(lambda x: x % 2 == 0, num3))

print(hasil3)