while True:
    age = int(input('Enter your age:'))

    if age>123:
            print('You are not that old \nTry Again')

    elif age >= 18:
        print('You are good to vote')

    elif age<18:
        print('You can\'t vote')

    elif age == 0:
        print('It is invalid age')

    else:
        print('Enter a valid age')


    ans = input('Do you want it again(y/n)').lower()
    if ans == 'y':
        continue
    else:
         break