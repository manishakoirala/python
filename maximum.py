print("Enter the input :")
N=input()
mylist=[]
lista=[]
listb=[]
for x in range(N):
	mylist.append(input())
for i in range(N):
	lista.append(input())
for k in range(N):
	listb.append(input())
print("data:")
for i in range(N):
	print(mylist[i] , lista[i],listb[i])


print("the output : ")
for j in range(N):
	if mylist[j] < lista[j] and mylist[j]<listb[j] :
		print(mylist[j])
	elif lista[j] < mylist[j] and lista[j] < listb[j] :
		print(lista[j])
	else :
		print(listb[j])
  