import collections
import math
import matplotlib.pyplot as plt
import numpy as np


def read_data():
	data = open("data.csv")
	l = data.readlines()
	header = l[0].split(',')
	if len(header) != 2 and header[0] != "km" and header[1] != "price":
		return False
	dataset = collections.OrderedDict()
	for line in l[1:]:
		record = line.split(",")
		dataset[float(record[0])] = float(record[1].replace("\n", ""))
	return dataset

stepSize = 0.00000001

def main():
	global stepSize
	accepted_diff = 0.5
	constant = 1.0
	slope = 1.0

	dataset = read_data()
	mileages, prices = list(dataset.keys()), list(dataset.values())
	mileageMean = np.mean(mileages)
	priceMean = np.mean(prices)
	sumErrors = 0
	sumSquaredMileageErrors = 0
	for i in range (0, len(mileages)):
		m = mileages[i] - mileageMean
		sumSquaredMileageErrors += m ** 2
		sumErrors += m * (prices[i] - priceMean)
	slope = sumErrors / sumSquaredMileageErrors
	intercept = priceMean - slope * mileageMean
	print(slope, intercept)
	x = np.linspace(0, 300000, 10000)
	y = slope * x + intercept
	plt.plot(x, y, 'r')
	plt.plot(mileages, prices)
	plt.show()

if __name__ == '__main__':
	main()
