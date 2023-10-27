'''
#1
n = 185
res = 0
for i in range(3):
    res += n%10
    n = n//10
print(res)

#2
n = 123
res = n%10+(n//10)%10+(n//100)%10
print(f'res = {res} ({(n//100)%10} + {(n//10)%10} + {n%10})')
'''
#3
n = 130
res = 0
while n!=0:
    res += n%10
    n = n//10
print(res)