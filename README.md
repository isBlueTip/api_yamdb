# YaMDb API


### Описание

Учебный проект создания API для базы данных произведений с отзывами и комментариями. Позволяет делать запросы к ресурсам БД с любого устройства.


### Установка

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/isBlueTip/yatube_yamdb.git
```

```
cd yatube_yamdb
```

Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 yatube_yamdb/manage.py migrate
```

Запустить проект:

```
python3 yatube_yamdb/manage.py runserver
```
