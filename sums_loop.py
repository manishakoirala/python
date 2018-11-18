print("input data :")
N=input()

listnum1 =[]
listnum2 =[]
for i in range(N) :

	listnum1.append(input())
for x in range(N):
	listnum2.append(input())
print("output data:")

for j in range(N):
	sumn=listnum1[j]+listnum2[j]
	print(sumn)
	


