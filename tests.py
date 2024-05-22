import pytest

from main import BooksCollector

class TestBooksCollector:
    # 1. Тест на добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Тест на добавление новой книги
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Стальной алхимик')
        assert 'Стальной алхимик' in collector.books_genre

    # 3. Тест на установку жанра
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Стальной алхимик')
        collector.set_book_genre('Стальной алхимик', 'Фантастика')
        assert collector.books_genre['Стальной алхимик'] == 'Фантастика'

    # 4. Тест на получение жанра книги по имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    # 5. Тест на проверку правильности работы метода, возвращающего список книг определенного жанра из коллекции
    @pytest.mark.parametrize('genre, expected_result',
                             [("Фантастика", ["Стальной алхимик", "Атака титанов"]),
                              ("Ужасы", ["Оно"]),
                              ("Роман", [])])
    def test_get_books_with_specific_genre(self, genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Стальной алхимик')
        collector.add_new_book('Оно')
        collector.add_new_book('Атака титанов')

        collector.set_book_genre('Стальной алхимик', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Атака титанов', 'Фантастика')

        assert collector.get_books_with_specific_genre(genre) == expected_result

    # 6. Тест на проверку что метод get_books_genre возвращает ожидаемый словарь с соответствием книг и их жанров
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Стальной алхимик')
        collector.add_new_book('Оно')

        collector.set_book_genre('Стальной алхимик', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        expected_books_genre = {'Стальной алхимик': 'Фантастика', 'Оно': 'Ужасы'}

        assert collector.get_books_genre() == expected_books_genre

    # 7. Тест на проверку книги, которая подходит детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Огромный крокодил')
        collector.set_book_genre('Огромный крокодил', 'Комедии')
        assert 'Огромный крокодил' in collector.get_books_for_children()

    # 8. Тест на добавление книги в избранное:
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Стальной алхимик')
        collector.add_book_in_favorites('Стальной алхимик')
        assert 'Стальной алхимик' in collector.favorites

    # 9. Тест на удаление книги из избранного:
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Стальной алхимик')
        collector.add_book_in_favorites('Стальной алхимик')
        collector.delete_book_from_favorites('Стальной алхимик')
        assert 'Стальной алхимик' not in collector.favorites

    # 10. Тест на получение списка избранных книг:
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Стальной алхимик')
        collector.add_book_in_favorites('Стальной алхимик')
        assert 'Стальной алхимик' in collector.get_list_of_favorites_books()