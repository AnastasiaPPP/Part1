import file_writer as fw
import datetime
import commands as c


def menu():
    number_of_line = c.check_file()
    while True:
        print('1. Show all notes')
        print('2. Add new note')
        print('3. Show one note')
        print('4. Delete note')
        print('5. Edit note')
        print('6. Sort by date')
        print('7. Exit')
        print()

        try:
            n = int(input('Your input: '))
        except:
            print('Please, enter the number')
            continue

        if n == 1:
            if c.file_is_empty():
                print('File is empty')
                continue
            fw.show_file()
        elif n == 2:
            title = input('Title: ')
            text = input('Text: ')
            date = datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S")
            fw.write_file(title, text, number_of_line, date)
            number_of_line += 1
        elif n == 3:
            if c.file_is_empty():
                print('File is empty')
                continue
            fw.show_file()
            position = int(input('Select a note: '))
            try:
                c.show_one_note(position)
            except:
                print('Wrong input')
        elif n == 4:
            if c.file_is_empty():
                print('File is empty')
                continue
            fw.show_file()
            num = input('Select a note to delete: ')
            try:
                c.delete_note(num)
                number_of_line -= 1
            except:
                print('Wrong input')
        elif n == 5:
            if c.file_is_empty():
                print('File is empty')
                continue
            fw.show_file()
            num = input('Select a note: ')
            if int(num) <= number_of_line:
                c.change_note(num)
            else:
                print('Wrong input')
        elif n == 6:
            if c.file_is_empty():
                print('File is empty')
                continue
            date = input('Enter the date dd.mm.yyyy: ')
            c.search_note(date)
        elif n == 7:
            break
        else:
            print('Wrong command!')