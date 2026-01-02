med = input('Medical reason: ')
med.lower()
print(med)
if med != 'y' and med != 'n':
    print('Invalid input.')
att = int(input('Attendance rate: '))
if att>100 and att<0:
    print('Enter valid attendance rate.')
if med == 'y':
    print('Allowed.')
else:
    if att>=0 and att<75:
        print('Not Allowed.')
    else:
        print('Allowed.')