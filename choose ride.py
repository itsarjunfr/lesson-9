print('Select mode of transport: ')
print('1. Bike')
print('2. Car')
choice = int(input())
if choice == 1:
    print('Select bike type: ')
    print('1. Scooter')
    print('2. Motorcycle')
    c1 = int(input())
    if c1==1:
        print('You have selected the scooter.')
    elif c1==2:
        print('You have selected the motorcycle.')
    else:
        print('Invalid.')
elif choice == 2:
    print('Select car type: ')
    print('1. Sedan')
    print('2. SUV')
    c2 = int(input())
    if c2==1:
        print('You have selected the sedan.')
    elif c2==2:
        print('You have selected the SUV.')
    else:
        print('Invalid.')
else:
    print('Invalid.')