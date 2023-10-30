import csv
import re

input_csv_file = 'Weather_Data.csv'

#открытие исходного файла и создание CSV-читателя
with open(input_csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #создание словаря, (ключ - это год, значение - это файл CSV)
    year_to_csv = {}

    for row in csv_reader:
        date = row[0]
        year = date[:4]

        #проверка на существование файла для этого года
        if year in year_to_csv:
            year_to_csv[year].append(row)
        else:
            year_to_csv[year] = [row]

    #создание и запись отдельных CSV-файлов для каждого года
    for year, rows in year_to_csv.items():
        start_date = rows[0][0]
        temp = re.findall(r'\d+', start_date)
        res_start = list(map(int, temp))
        end_date = rows[-1][0]
        temp = re.findall(r'\d+', end_date)
        res_end = list(map(int, temp))
        output_csv_file = f'{res_start[2]}{res_start[1]}{res_start[0]}_{res_end[2]}{res_end[1]}{res_end[0]}.csv'

        with open(output_csv_file, 'w', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerows(rows)  #запись строки данных

print("Разбиение исходного файла Weather_Data.csv. Файлы CSV созданы для каждого года.")
