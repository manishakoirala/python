print("Enter the input :")
N=input()
mylist=[]
lista=[]
for x in range(N):
	mylist.append(input())
for i in range(N):
	lista.append(input())
print("data:")
for i in range(N):
	print(mylist[i] , lista[i])


print("the output : ")
for j in range(N):
	if mylist[j] > lista[j]:
		print(lista[j])
	else :
		print(mylist[j])
  