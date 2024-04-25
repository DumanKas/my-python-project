from library import Library
from book import Book


def main():
    library = Library()

    while True:
        print("1. Добавление книги")
        print("2. Прочитать книгу")
        print("3. Обновить книгу")
        print("4. Удалить книгу")
        print("5 Выйти")


        choise = input('Выберите действие от 1 до 5: ')


        if choise == '1':
            title = input('Введите название: ')
            year = int(input("Введите год книги: "))
            author = input('Введите автора книги: ')
            library.create(title, year, author)
            print("Книга была добавлена")

        elif choise == '2':
            book_id = int(input("Введите id книги "))
            book = library.read(book_id)
            if book:
                print('Книга была найдена')
                print("Год", book.year)
                print('Название', book.title)
                print("Автор", book.author)
            else:
                print("id не был найден")

        elif choise == '3':
            book_id = int(input('Введите id '))
            new_title = input('Введите новое имя книги: ')
            new_year = int(input('Введите новый год книги: '))
            new_author = input('Введите нового автора книги: ')
            new_book = Book(new_title, new_year, new_author)
            library.update(book_id, new_book)
            print("Книга обновлена")

        elif choise == '4':
            book_id = int(input("Введите id для удаление книги "))
            library.delete(book_id)
            print('Книга удалена ')

        elif choise == '5':
            print("Выходим с программы")
            break

        else:
            print("Выберите правильную команду")

if __name__ == "__main__":
    main()
