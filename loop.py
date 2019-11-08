x = "abcdef"
i = "a"

while i in x[:-1]
	print(i,end= " ")


x = "abcdef"
for i in x[:-1]:
	print(i,end= " ")

x = "abcdef"
for i in x[::-1]:
	print(i,end= " ")
