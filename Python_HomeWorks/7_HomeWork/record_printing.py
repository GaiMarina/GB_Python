

def log_import():
    with open('phone_book.csv', 'r', encoding='UTF-8') as record:
        recording = record.readlines()
        print([i for i in enumerate(recording, 1)])