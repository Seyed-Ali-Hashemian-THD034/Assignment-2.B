#SUM
sum = 0
while True:
    x = input('Type the number or type the - end - word.')
    if x == 'end':
        print ('You have closed the application.')
        break

    else:
        sum = int(x) + sum
        print('answer is' , sum)