def Goldbach(num):
    lists = [x for x in range(2, num) if not [y for y in range(2, x) if x % y == 0]]
    for num1 in lists:
        num2=num-num1
        if num2 in lists:
            return (num1,num2)
            break
			
print (Goldbach(20))