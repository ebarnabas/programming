import random
zsak=[]
while len(zsak)<5:
	num=random.randrange(1,91)
	if num not in zsak:
		zsak.append(num)
print(zsak)
