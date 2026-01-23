age = int(input('Enter your age: '))
if age>=10 and age<=20:
    print('You are permitted to join the class.')
elif age<0:
    print('Enter a valid age.')
else:
    print('You are not allowed to join the class.')