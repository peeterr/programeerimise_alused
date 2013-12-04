import random

min =int(raw_input('min='))
max =int(raw_input('max='))
n =int(raw_input('n='))

i = 0
while i<n:
	print random.randint(min, max)
	i = i+1
