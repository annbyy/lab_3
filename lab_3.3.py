import csv
from datetime import datetime, timedelta

input_csv_file = 'Weather_Data.csv'

#открытие исходного файла и создание CSV-читателя
with open(input_csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #создание словаря, (ключ - это год, значение - это файл CSV)
    week_to_csv = {}

    for row in csv_reader:
        date_str = row[0]
        date = datetime.strptime(date_str, '%d.%m.%Y')
        week_number = date.isocalendar()[1]  #номер недели

        #проверка на существование файла для этой недели
        if week_number in week_to_csv:
            week_to_csv[week_number].append(row)
        else:
            week_to_csv[week_number] = [row]

    #создание и запись отдельных CSV-файлов для каждой недели
    for week_number, rows in week_to_csv.items():
        start_date = datetime.strptime(rows[0][0], '%d.%m.%Y')
        end_date = datetime.strptime(rows[-1][0], '%d.%m.%Y')
        start_date_str = start_date.strftime('%Y%m%d')
        end_date_str = end_date.strftime('%Y%m%d')
        output_csv_file = f'{start_date_str}_{end_date_str}.csv'

        with open(output_csv_file, 'w', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerows(rows)  #запись строки данных

print("Разбиение исходного файла Weather_Data.csv. Файлы CSV созданы для каждой недели.")
