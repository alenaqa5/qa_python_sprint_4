import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_one_book_long_name_book_is_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Как питаться правильно, если есть доставка')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name, genre', [['Искусство просыпаться по понедельникам', 'Фантастика'], ['Дейлики в 9 утра', 'Ужасы']])
    def test_set_book_genre_set_genre_for_book_genre_set(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre == {name: genre}

    def test_get_book_genre_genre_got(self):
        collector = BooksCollector()
        collector.add_new_book('Не умереть во вторник')
        collector.set_book_genre('Не умереть во вторник', 'Комедии')
        genre = collector.get_book_genre('Не умереть во вторник')
        assert genre == 'Комедии'

    def test_get_books_with_specific_genre_get_book_comedy_genre_comedy_book_got(self):
        collector = BooksCollector()
        collector.add_new_book('Ретро в конце спринта')
        collector.set_book_genre('Ретро в конце спринта', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Ретро в конце спринта']

    def test_get_books_genre_got_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ретро в конце спринта')
        collector.set_book_genre('Ретро в конце спринта', 'Комедии')
        assert collector.get_book_genre('Ретро в конце спринта') == 'Комедии'

    def test_get_books_for_children_got_children_books(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения багули на проде')
        collector.set_book_genre('Приключения багули на проде', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Приключения багули на проде']

    def test_add_book_in_favorites_book_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('А давайте еще это в спринт возьмем')
        collector.add_book_in_favorites('А давайте еще это в спринт возьмем')
        assert collector.favorites == ['А давайте еще это в спринт возьмем']

    def test_delete_book_from_favorites_last_favorite_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('А давайте еще это в спринт возьмем')
        collector.add_book_in_favorites('А давайте еще это в спринт возьмем')
        collector.delete_book_from_favorites('А давайте еще это в спринт возьмем')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_not_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('На моей стороне не воспроизводится')
        collector.add_book_in_favorites('На моей стороне не воспроизводится')
        collector.add_new_book('Коллеги, микрофон забыл включить')
        collector.add_book_in_favorites('Коллеги, микрофон забыл включить')
        assert collector.favorites == ['На моей стороне не воспроизводится','Коллеги, микрофон забыл включить']
