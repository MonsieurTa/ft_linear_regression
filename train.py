import collections

def read_data():
	data = open("data.csv")
	l = data.readlines()
	header = l[0].split(',')
	if len(header) != 2 and header[0] != "km" and header[1] != "price":
		return False
	dataset = collections.OrderedDict()
	for line in l[1:]:
		record = line.split(",")
		dataset[record[0]] = float(record[1].replace("\n", ""))
	return dataset

def main():
	dataset = read_data()
	# Display dataset entries
	# for km, price in dataset.items():
	# 	print("km: %s, price: %s" % (km, price))



if __name__ == '__main__':
	main()
