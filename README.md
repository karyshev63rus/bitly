# Обрезка ссылок с помощью Битли

Настоящий Проект позволяет преобразовывать длинные URL-адреса в значительно более короткие ссылки (не более 30 символов). Полученные укороченные ссылки работают так же, как обычный URL-адрес, но, поскольку они укорочены, их гораздо проще делить, управлять и анализировать. Проект является консольным приложением и принимает в командной строке название интерпретатора (python или python3), имя файла (здесь это main.py) и собственно укорачиваемый URL-адрес. Пользователь может либо просто получать укороченные ссылки, либо (если на вход была подана уже укороченная ранее ссылка) - информацию о количествве переходов по данной укороченной ссылке.

### Как установить

Обрезка ссылок производится компанией Bitly через соответствующий прикладной программный интерфейс. Для осуществления взаимодействия с компанией необходимо получить соответствующий ключ (токен). Подробнее об этом [здесь](https://dev.bitly.com/get_started.html). Далее в одной директории с файлом main.py надо создать файл .env и указать в нем значения трех переменных:
* TOKEN==полученный вами ключ(токен),
* DB_USERNAME==придуманный при регистрации логин,
* DB_PASSWORD==придуманный вами при регистрации пароль.

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
