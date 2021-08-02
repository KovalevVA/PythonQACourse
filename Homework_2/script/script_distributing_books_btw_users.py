import json, csv

books_file = '../data_files/books.csv'
users_file = '../data_files/users.json'
script_result = '../data_files/script_result.json'

def read_books_file():

    '''
    Данная функция читает файл books.csv, составвляет словарь, ключи которого представляют собой строки заголовков
    колонок csv файла: 'Title', 'Author' и 'Height', а значения соответсвуют данным, записанным в эти колонки
    на пересечении с каждой строкой, прочитанной на каждой итерации. При вызове функция возвращает объект генератор,
    который содержит словарь с необходимым для дальнейшей работы набором данных
    '''

    with open(books_file, 'r') as books_csv:
        csv_reader = csv.DictReader(books_csv)
        books_dict = {}
        for row in csv_reader:
            books_dict['Title'] = row['Title']
            books_dict['Author'] = row['Author']
            books_dict['Height'] = row['Height']
            yield books_dict

def read_users_file():

    '''
    Данная функция читает файл users.json и формирует словарь с необходимым набором данных для пользователя.
    Далее для каждого пользователя вызывает генератор функции read_books_file, чтобы получить словарь с книгой,
    которую получит пользователь. Соответственно, если пользователей меньше чем книг, то книги между пользователями будут
    распределяться равномерно до тех пор, пока список книг не будет исчерпан.
    Если пользователей больше чем книг, то книгу получит каждый пользователь в диапазоне от первого до пользователя,
    номер которго в списке пользователей соответствует номеру последней в списке книг. Остальные пользователи не получат книгу и
    не будут добавлены в результирующий файл.
    '''

    with open(users_file, 'r') as text_file:
        text_str = text_file.read()

    with open(books_file, 'r') as books:
        books_csv = csv.reader(books)
        books_number = len(list(books_csv)) - 1

    dictionary_from_json = json.loads(text_str)
    books_gen = read_books_file()

    amount_of_users = dictionary_from_json[-1]['index'] + 1
    result_list = []

    while books_number > 0:
        books_counter = books_number

        for id in dictionary_from_json:

            if books_counter == 0:
                break

            user = {
                'name' : id['name'], 'gender' :  id['gender'], 'address' : id['address'], 'books':[]
            }

            books = books_gen.__next__()
            user['books'] = books
            result_list.append(user)

            books_counter -= 1

        books_number = books_number - amount_of_users
    write_result_file(result_list)

def write_result_file(result_list):

    '''
    Данная функция записывает результирующий по каждому пользователю словарь в файл
    example.json. Принимает на вход две переменных users и books. В случае, если в качестве books передан пустой список, то
    и в элемент books результирующего словаря для пользователя из словаря user запишется пустой список. В случае, если
    в качестве books передан словарь, то данный словрь будет записан в качестве значения элемента books
    '''

    with open(script_result, 'w') as example_file:
        json.dump(result_list, example_file, indent=4)

read_users_file()