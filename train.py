import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def stepGradient(learning_rate, b, m, x_data, y_data):
	b_gradient = 0
	m_gradient = 0
	N = len(x_data)
	for i in range(0, N):
		guess = m * x_data[i] + b
		error = y_data[i] - guess
		b_gradient += -(2 / N) * error
		m_gradient += -(2 / N) * x_data[i] * error
	new_b = b - (learning_rate * b_gradient)
	new_m = m - (learning_rate * m_gradient)
	return [new_b, new_m]

def normalize_array(array):
	return (array - min(array)) / (max(array) - min(array))

def denormalize(value, array):
	return value * (max(array) - min(array)) + min(array)

def main():
	data_train = pd.read_csv("data.csv")
	x_data = np.array(data_train['km'])
	y_data = np.array(data_train['price'])
	x_normalized = normalize_array(x_data)
	y_normalized = normalize_array(y_data)

	learning_rate = 0.0001
	epsilon = 0.0001

	b = 1
	m = 1
	while True:
		new_b, new_m = stepGradient(learning_rate, b, m, x_normalized, y_normalized)
		if (-epsilon <= abs(b - new_b) <= epsilon and -epsilon <= abs(m - new_m) <= epsilon):
			print(new_b, new_m)
			return
		else:
			b = new_b
			m = new_m

	# mileages, prices = list(dataset.keys()), list(dataset.values())

	# mileageMean = np.mean(mileages)
	# priceMean = np.mean(prices)
	# sumErrors = 0
	# sumSquaredMileageErrors = 0
	# for i in range (0, len(mileages)):
	# 	m = mileages[i] - mileageMean
	# 	sumSquaredMileageErrors += m ** 2
	# 	sumErrors += m * (prices[i] - priceMean)
	# slope = sumErrors / sumSquaredMileageErrors
	# intercept = priceMean - slope * mileageMean
	# print(slope, intercept)
	# x = np.linspace(0, 300000, 10000)
	# y = slope * x + intercept
	# plt.plot(x, y, 'r')
	# plt.plot(mileages, prices)
	# plt.show()

if __name__ == '__main__':
	main()
