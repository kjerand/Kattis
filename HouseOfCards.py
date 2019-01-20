minHeight = int(input())
x = minHeight
while True:  
    cards = x*(3*x + 1)//2
 
    if cards % 4 == 0:
        print(x)
        break
    x += 1
