import random
r = random.randint(1, 100)
n = 1
while True:
    guess = input(' 猜一個1-100內的數字 ')
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