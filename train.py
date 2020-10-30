import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd

def main():
	try:
		data_train = pd.read_csv("data.csv")
		x_data = np.array(data_train['km'])
		y_data = np.array(data_train['price'])
	except ValueError:
		print("error: invalid datas")

	x = np.array([0, 1])
	y_result = np.empty((0, 2))
	x_normalized = normalize_array(x_data)
	y_normalized = normalize_array(y_data)
	learning_rate = 1
	b = 0
	m = 0

	for _ in range(1000):
		b, m = stepGradient(learning_rate, b, m, x_normalized, y_normalized)
		y = m * x + b
		y_result = np.append(y_result, [y], axis=0)

	m = m * (max(y_data) - min(y_data)) / (max(x_data) - min(x_data))
	b = denormalize(b, y_data) + min(x_data) * -m
	print(b, m)

	# PLOT
	fig, ax = plt.subplots()
	ax.plot(x_normalized, y_normalized, 'ro')
	line, = ax.plot([], [], 'b')

	def init():
		line.set_xdata(x)
		line.set_ydata([])
		return line,

	def update(i):
		line.set_ydata(y_result[i])
		return line,

	ani = animation.FuncAnimation(fig, update, init_func=init, frames=1000, interval=50, repeat=False, blit=True)
	plt.show()

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

if __name__ == '__main__':
	main()
