#Генерація перестановок
def gen(li):
	if len(li)==1:
		return [[li[0]]]
	res=gen(li[:(len(li)-1)])
	a=li[len(li)-1]
	arr=res.copy()
	for el in arr:
		for i in range(len(el)):
			temp=el.copy()
			temp.insert(i,a)
			res.append(temp)
		el.append(a)
	return res
f=open("Perestanovki.txt",'w')
a=gen(list(set(input().split())))
for i in range(len(a)):
	f.write(str(i+1)+': '+' '.join(a[i])+'\n')	
f.close()