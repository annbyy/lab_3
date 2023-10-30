import csv
from datetime import datetime

input_csv_file = 'Weather_Data.csv'

def data_returner(date_user):
    with open(input_csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = datetime.strptime(row[0], '%d.%m.%Y')
            date1 = datetime.strptime(date_user, '%d.%m.%Y')
            if date == date1:
                print(f'{row[1]},{row[2]},{row[3]}')
                return
    print('None')

date_user = input('Enter date: ')
data_returner(date_user)
