import random
r = random.randint(1, 100)
while True:
    guess = input(' 猜一個1-100內的數字 ')
    guess = int(guess)
    if guess > r:
        print('再小一點')
    elif guess < r:
	    print('再大一點')
    else:
	    print('恭喜你答對了')
	    break