# Bitly url shorterer

This project allows you to convert long URLs to significantly shorter links (no more than 30 characters). The resulting shortened links work just like a regular URL, but since they are shortened, they are much easier to share, manage, and analyze. The project is a console application and takes in the command line the name of the interpreter (python or python3), the file name (here it is main.py) and the URL. The user can either simply receive shortened links, or (if a previously shortened link was submitted to the input) - information on the number of clicks on this shortened link.

### How to install

Links are trimmed by Bitly through the appropriate application programming interface. To interact with the company, it is necessary to obtain the corresponding key (token). Read more about this [here](https://dev.bitly.com/get_started.html). Next, in the same directory with the main.py file, you need to create an .env file and specify the values of three variables in it: 
* TOKEN==key (token you received), 
* DB_USERNAME==login you created when registering and, 
* DB_PASSWORD==the password you created when registering.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers 
[dvmn.org](https://dvmn.org/).


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