from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import csv

def main():
	months = open("Month.csv","r")
	days = open("Weekday.csv","r")
	hours = open("Hours.csv","r")
	month_reader = csv.reader(months,delimiter = ',')
	day_reader = csv.reader(days,delimiter = ',')
	hour_reader = csv.reader(hours,delimiter = ',')
	month_attr = []
	month = []
	month_test = []
	month_testattr = []
	day_attr = []
	day = []
	day_test = []
	day_testattr = []
	hour_attr = []
	hour = []
	hour_test = []
	hour_testattr = []
	for e, x in enumerate(month_reader):
		if e > 17223:
			month_test.append(x[0])
			month_testattr.append(x[1:])
			continue
		month.append(x[0])
		month_attr.append(x[1:])
	#17223 is 2/3 of the docs.
	for e, x in enumerate(day_reader):
		if e > 17223:
			day_test.append(x[0])
			day_testattr.append(x[1:])
			continue
		day.append(x[0])
		day_attr.append(x[1:])
	for e, x in enumerate(hour_reader):
		if e > 17223:
			hour_test.append(x[0])
			hour_testattr.append(x[1:])
			continue
		hour.append(x[0])
		hour_attr.append(x[1:])
	month_tree = KNeighborsClassifier(n_neighbors = 7)
	day_tree = KNeighborsClassifier(n_neighbors = 7)
	hour_tree = KNeighborsClassifier(n_neighbors = 19)
	month_tree.fit(month_attr,month)
	day_tree.fit(day_attr,day)
	hour_tree.fit(hour_attr,hour)
	print month_tree.score(month_testattr,month_test)
	print day_tree.score(day_testattr,day_test)
	print hour_tree.score(hour_testattr,hour_test)
	
	
main()