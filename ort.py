#Ортогоналізація Грама-Шмідта

def scal_mult(a,b):
	res=0
	for i in range(len(a)):
		res+=a[i]*b[i]
	if res==0:
		res=0.00000000000000001
	return res

def plus_vect(li):
	res=[0 for x in range(len(li[0]))]
	for j in range(len(li)):	
		for i in range(len(li[0])):			
			res[i]+=li[j][i]
	return res

def num_mult_vect(num,vect):
	res=[num*vect[i] for i in range(len(vect))]
	return res

def ortog(a):
	b=[]
	m=[]
	for i in range(len(a)):
		for j in range(i):
			k=-scal_mult(a[i],b[j])/scal_mult(b[j],b[j])
			m.append(num_mult_vect(k,b[j]))
		m.append(a[i])
		b.append(plus_vect(m))
		m=[]
	return b

print("\t\tОртогоналізація Грама-Шмідта")

print("Введіть кількість векторів >>",end=' ')
n=int(input())
a=[]
for i in range(n):
	print("Введіть вектор",i+1,">>",end=' ')
	q=input().split()
	q=[int(x) for x in q]
	a.append(q)
print()
b=ortog(a)
i=0
for el in b:
	i+=1
	print("b",i,"=( ",sep='',end='')
	for e in el:
		print("%.2f" %float(e),end=" ")
	print(")")