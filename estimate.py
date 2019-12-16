theta0 = 8499.599649933216
theta1 = -0.0214489635917023


def main():
	global theta0, theta1
	mileage = input("Enter a mileage: ")
	try:
		value = int(mileage)
	except ValueError:
		print("error: input is not a number")
		return
	result = theta1 * value + theta0
	print("theta0 = %s, theta1 = %s" % (theta0, theta1))
	print("Function:\n\testimatePrice(mileage) = (theta1 * mileage) + theta0")
	print("Replacing:\n\testimatePrice(%s) = (%s * %s) + %s" % (mileage, theta1, mileage, theta0))
	print("Estimated price = %s" % result)


if __name__ == '__main__':
	main()
