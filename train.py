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

	learning_rate = 0.1

	b = 0
	m = 1
	x = np.array([0, 1])
	for i in range(0, 1000):
		b, m = stepGradient(learning_rate, b, m, x_normalized, y_normalized)
	m = m * (max(y_data) - min(y_data)) / (max(x_data) - min(x_data))
	b = denormalize(b, y_data) + min(x_data) * -m
	print(b, m)

if __name__ == '__main__':
	main()
