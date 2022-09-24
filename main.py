list1 = [12, 23, 45, 34]
list2 = [12, 23, 45, 34]
list3 = [45, 45, 56, 65]
x = 0
y = 0
z = 0
for single in list1:
  if single % 2 == 0:
    for lis in list2:
      for li in list3:
        z = z + li
      y = y + lis
  x = x + single

print(x+y+z)

prime = 19
count = 0
for i in range(1, prime):
  if prime % i == 0:
    count = count+1

print(count)

