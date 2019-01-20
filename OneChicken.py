a, b = [int(x) for x in input().split()]

if a - b == 1 or b - a == 1:
    print("Dr. Chaz will have 1 pieces of chicken left over!")
elif a > b:
    print("Dr. Chaz needs ",(a-b), "more pieces of chicken!")


elif b > a:
     print("Dr. Chaz will have ",(b-a) ,"pieces of chicken left over!")