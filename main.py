from seasons import *
from time import sleep
Askseason = input('What season do you want(spring/ summer/ autumn/ winter)')
if Askseason == 'spring':
    print('generating...')
    sleep(1)
    spring()
    print('Here is a picture of a spring urban')
elif Askseason == 'summer':
    print('generating...')
    sleep(1)
    summer()
    print('Here is a picture of a summer urban')
elif Askseason == 'autumn':
    print('generating...')
    sleep(1)
    autumn()
    print('Here is a picture of an autumn urban')
elif Askseason == 'winter':
    print('generating...')
    sleep(1)
    winter()
    print('Here is a picture of a winter urban')
else:
    print('Not Available')
exitonclick()
hideturtle()
