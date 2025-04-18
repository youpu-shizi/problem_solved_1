x = 0
y = 0
while True:
    a = input('>>> ')
    if a == 'done':
        if y < 2 :
            print('please provide at least two numbers')
        else:
            print("the total is", x)
            print("your count is", y)
            z = x / y
            print("the average is", z)
            continue
    else:
        try:
            x = int(a) + x
        except:
            print('Please only enter a integer number no text unless you are done, and you wanna get the result then you can write "done"')
        y += 1