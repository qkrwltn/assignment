a , b = map(int, input().split())
if a>b:
    print('>')
elif a<b:
    print("<")
elif a==b:
    print("==")

q= int(input())
#print(q)

if q >= 90 and q<= 100:
  print('A')
elif q >= 80 and q<= 89:
  print('B')
elif q >= 70 and q<= 79:
  print('C')
elif q >= 60 and q<= 69:
  print('D')
else:
  print('F')

year = int(input())

if year % 4 == 0 and year % 100 !=0 or year %400 ==0:
  print(1)
else:
  print(0)

x=int(input())
y=int(input())
lst=[]
lst.append(x)
lst.append(y)

if lst[0]> 0 and lst[1]> 0:
  print(1)
elif lst[0]<0 and lst[1]>0:
  print(2)
elif lst[0]<0 and lst[1]<0:
  print(3)
elif lst[0]>0 and lst[1]<0:
  print(4)
  