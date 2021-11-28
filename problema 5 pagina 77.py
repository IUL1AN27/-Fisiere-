vocale='a A e E i I o O u U'
x=0
with open ('C:/Users/user/Desktop/Text.txt' , 'r') as f:
    a=f.read()
with open ('Text2.txt' , 'w') as f:
    for i in a:
        if i in vocale:
            f.write(i)
            x+=1
print('Vocalele sunt' ,x)
