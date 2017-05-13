import calendar
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_input = raw_input('Enter Your Birthday: ')
year_input = raw_input('How Long Do You Want To Check? ')

int_year_input = int(year_input)

year_list = list()

date_input_datetime = datetime.strptime(date_input, '%Y-%m-%d')

date_input_day_name = calendar.day_name[date_input_datetime.weekday()]

count = 1

while count <= int_year_input:
	check_date = date_input_datetime + relativedelta(years=+count)
	if calendar.day_name[check_date.weekday()] == date_input_day_name:
		year_list.append(check_date.year)
	count = count + 1

print year_list
