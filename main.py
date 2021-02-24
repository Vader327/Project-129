import csv

original_data = []
brightest_stars_data = []



def update_data(array):
    for i in array:
        i[0] = i[0].lower()
        
        i[3] = i[3].replace(',', '')

        if i[2]:
            i[2] = float(i[2]) * 0.000954588

        if i[3]:
            i[3] = float(i[3]) * 0.000954588


    

with open('brown dwarfs.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        original_data.append(row)

with open('brightest stars.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        brightest_stars_data.append(row)

headers = original_data[0]
data = original_data[1:]

headers2 = brightest_stars_data[0]
data2 = brightest_stars_data[1:]

update_data(data)
update_data(data2)

final_data = data + data2
final_data.sort(key=lambda final_data: final_data[0])

with open("final.csv", "w", newline="", encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_data)
