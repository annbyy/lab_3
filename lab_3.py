import csv

input_csv_file = 'Weather_Data.csv'

output_x_csv_file = 'X.csv' #файл для дат
output_y_csv_file = 'Y.csv' #файл для данных

#считывание данных из исходного файла
data = []
with open(input_csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(row)

dates = [row[0] for row in data] #разбивание данных на даты
values = [[row[1], row[2], row[3]] for row in data] #разбивание данных на данные

#запись дат в файл X.csv
with open(output_x_csv_file, 'w', newline='') as x_csv_file:
    csv_writer = csv.writer(x_csv_file)
    for date in dates:
        csv_writer.writerow([date])

#запись данных в файл Y.csv
with open(output_y_csv_file, 'w', newline='') as y_csv_file:
    csv_writer = csv.writer(y_csv_file)
    for value in values:
        csv_writer.writerow(value)

print("Разбиение исходного файла Weather_Data.csv. Созданы файлы X.csv и Y.csv.")
