#This scripts finds the value of pi using the monte carlo method. It isn't visual, although the result approximation of pi will be the same

#import necessary modules
from math import sqrt
from random import randint

incir = 0.0

for i in range(0, 100000):
	x = float(randint(-5000, 5001))
	y = float(randint(-5000, 5001))
	mag = float(sqrt((x ** 2.0) + (y ** 2.0)))
	if mag < 5000:
		incir += 1.0

outcome = ((incir / 100000) * 4)

print str(outcome)
