import csv
import matplotlib.pyplot as plt

with open('mpg.csv') as csvfile:
	mpg = list(csv.DictReader(csvfile))

print(mpg[0].keys())
cyl = set(x['cylinders'] for x in mpg)

#an empty list to store calculations
horsepower_cyl = []

for c in cyl:
	sum_horsepower = 0
	cyltypecount = 0
	for x in mpg:
		if x['cylinders'] == c:
			try:
				sum_horsepower += int(x['horsepower'])
				cyltypecount += 1
			except ValueError:
				print('Invalid horsepower value')
	avg = sum_horsepower/cyltypecount
	avg = "%.2f" % avg
	horsepower_cyl.append((c, avg)) # append the tuple

horsepower_cyl.sort(key=lambda x: x[0])

a = 0
i = 0
while (i != len(mpg)):
	try:
		a=a+int(mpg[i]['horsepower'])
	except ValueError:
		print('Invalid value: ' + mpg[i]['horsepower'])
	i=i+1

avg=a/len(mpg)
avg = "%.2f" % avg
print('avg horsepower: ' + str(avg))
print(horsepower_cyl)
