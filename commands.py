import file_writer
import datetime

def delete_note(number):
    l = []
    lines = 0
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            l.append(line.split(';'))
            lines += 1
        del l[int(number)-1]
        with open('data_file.csv', 'wb'):
            pass
        for i in range(lines-1):
            file_writer.write_file(l[i][1], l[i][2], i+1, l[i][3])

def change_note(number_of_line):
    l = []
    lines = 0
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            l.append(line.split(';'))
            lines += 1
        title = input('New title: ')
        text = input('New text: ')
        position = l[int(number_of_line) -1][0]
        date = datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S")
        l[int(number_of_line) -1][3] = date
        l[int(number_of_line) - 1] = [position, title, text, date]
        with open('data_file.csv', 'wb'):
            pass
        for i in range(lines):
            file_writer.write_file(l[i][1], l[i][2], l[i][0], l[i][3])

def show_one_note(number):
    l = []
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            l.append(line.split(';'))
        print(''.join(l[number - 1]))

def search_note(date):
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            if date in line:
                print(line)

def check_file():
    l = []
    lines = 0
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            l.append(line.split(';'))
            lines += 1
    if len(l) == 0:
        return 1
    else:
        return int(l[-1][0]) + 1

def file_is_empty():
    file_list = []
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            file_list.append(line)
    if len(file_list) >= 1:
        return False
    else:
        return True

