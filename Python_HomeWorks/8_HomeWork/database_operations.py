import csv


def user_search():
    flag = True
    word = input("Input the person's surname for search: ")
    with open('data_base.csv', 'r', newline='') as csv_rec:
        csv_recording = csv.reader(csv_rec)
        for row in csv_recording:
            if row[0].find(word) >= 0:
                print(' '.join(row[0].split(';')))
                flag = False
    if flag:
        print()
        print('Null search result. Try again.')
