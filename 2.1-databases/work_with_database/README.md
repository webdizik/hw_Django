# Выгрузка каталога товаров из csv-файла с сохранением всех позиций в базе данных

## Задание

Есть некоторый [csv-файл](./phones.csv), который выгружается с сайта-партнера. Этот сайт занимается продажей телефонов.

Мы же являемся их региональными представителями, поэтому нам необходимо взять данные из этого файла и отобразить их на нашем сайте на странице каталога, с их предварительным сохранением в базу данных.

## Реализация

Что необходимо сделать

- В файле `models.py` нашего приложения создаём модель Phone с полями  
- Написать скрипт для переноса данных из csv-файла в модель `Phone`.
  Скрипт необходимо разместить в файле `import_phones.py` в методе `handle(self, *args, **options)`.
  Подробнее про подобные скрипты (django command) можно почитать [здесь](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/) и [здесь](https://habr.com/ru/post/415049/).
- При запросе `<имя_сайта>/catalog` должна открываться страница с отображением всех телефонов.
- При запросе `<имя_сайта>/catalog/iphone-x` должна открываться страница с отображением информации по телефону. `iphone-x` — это для примера, это значение берётся из `slug`.
- В каталоге необходимо добавить возможность менять порядок отображения товаров: по названию в алфавитном порядке и по цене по убыванию и по возрастанию.

Шаблоны подготовлены, ваша задача — ознакомиться с ними и корректно написать логику.

## Ожидаемый результат

![Каталог с телефонами](res/catalog.png)

## Подсказка

Для переноса данных из файла в модель можно выбрать один из способов:

- воспользоваться стандартной библиотекой языка Python: `csv` (рекомендуется).
- построчно пройтись по файлу и для каждой строки сделать соответствующую запись в БД.

Для реализации сортировки можно брать параметр `sort` из `request.GET`.

Пример запросов:

- `<имя_сайта>/catalog?sort=name` — сортировка по названию;
- `<имя_сайта>/catalog?sort=min_price` — сначала отображать дешёвые.

## Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

- Команда для создания миграций приложения для базы данных

```bash
python manage.py migrate
```

- Команда для загрузки данных из csv в БД

```bash
python manage.py import_phones
```

- Команда для запуска приложения

```bash
python manage.py runserver
```

- При создании моделей или их изменении необходимо выполнить следующие команды:

```bash
python manage.py makemigrations
python manage.py migrate
```
