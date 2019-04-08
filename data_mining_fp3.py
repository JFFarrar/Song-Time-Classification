def main():
	check = open("ids.csv","r")
	checker = check.readlines()
	empty = []
	for line in checker:
		temp = line.split(" ")
		if(len(temp) > 12):
			empty.append(int(temp[12]))
	for x in range(len(checker)/2):
		if x in empty:
			continue
		else:
			print(x)
			
main()