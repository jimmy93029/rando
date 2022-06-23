import random 
r = random.randint(1,100)
while True: 
  test = input('請輸入1~100')
  test = int(test)
  if test == r :
  	print('終於猜對了')
  	break
  elif test > r:
    print('比答案大')
  else:
    print('比答案小')  