

def main():
	mileage = raw_input("Enter a mileage: ")
	try:
		value = int(mileage)
	except ValueError:
		print("error: input is not a number")
		return
	theta0 = 0.1
	theta1 = 0
	result = theta1 * value + theta0
	print("theta0 = %s, theta1 = %s" % (theta0, theta1))
	print("Function:\n\testimatePrice(mileage) = (theta1 * mileage) + theta0")
	print("Replacing:\n\testimatePrice(%s) = (%s * %s) + %s" % (mileage, theta1, mileage, theta0))
	print("Estimated price = %s" % result)


if __name__ == '__main__':
	main()
