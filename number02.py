import random
start = input('請選擇最小直')
end = input('請選擇最大值')
start= int(start)
end = int(end)
r = random.randint(start, end)
n = 1
while True:
    guess = input('猜一個數字')
    guess = int(guess)
    if guess > r:
        print('再小一點')
    elif guess < r:
	    print('再大一點')
    else:
	    print('恭喜你答對了')
	    print('你已經猜了',n,'次了')
	    break
    print('你已經猜了',n,'次了')
    n += 1 # n = n + 1