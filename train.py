import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def stepGradient(learning_rate, b, m, x_data, y_data):
	sum_intercept = 0
	sum_slope = 0
	N = len(x_data)
	for i in range(0, N):
		estimation = m * x_data[i] + b
		error = estimation - y_data[i]
		sum_intercept += error
		sum_slope += error * x_data[i]
	theta0 = learning_rate * (sum_intercept / N)
	theta1 = learning_rate * (sum_slope / N)
	return [b - theta0, m - theta1]

def normalize_array(array):
	return (array - min(array)) / (max(array) - min(array))

def denormalize(value, array):
	return value * (max(array) - min(array)) + min(array)

def main():
	try:
		data_train = pd.read_csv("data.csv")
		x_data = np.array(data_train['km'])
		y_data = np.array(data_train['price'])
	except ValueError:
		print("error: invalid datas")
	x_normalized = normalize_array(x_data)
	y_normalized = normalize_array(y_data)

	learning_rate = 1

	b = 0
	m = 0
	x = np.array([0, 1])
	for i in range(0, 1000):
		b, m = stepGradient(learning_rate, b, m, x_normalized, y_normalized)
		x = np.array([0, 1])
		y = m * x + b
		plt.plot(x_normalized, y_normalized, 'ro')
		plt.plot(x, y, 'b')
		plt.draw()
		plt.pause(0.0000001)
		plt.cla()
	m = m * (max(y_data) - min(y_data)) / (max(x_data) - min(x_data))
	b = denormalize(b, y_data) + min(x_data) * -m
	print(b, m)

if __name__ == '__main__':
	main()
