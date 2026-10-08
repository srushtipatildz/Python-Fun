# for i in range(1,5):
#  print("\n")
#  for j in range(1,(4-i)+1):
#   print(" ",end=" ")
#  for k in range(1,(i*2-1)+1):
#   print("*",end=" ")


# count
# n = 1234
# count = 0

# while n > 0:
#     n = n//10
#     count += 1

# print(count)

# reverse digits 
a=1234
rev=0

while a>0:
    digit=a%10
    rev = rev * 10 + digit
    a=a//10
print(rev)
