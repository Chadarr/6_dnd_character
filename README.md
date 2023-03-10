# Генератор персонажей для D&D по шаблону

Скрипт для генерации листов персонажа для настольной игры D&D по заданному заранее шаблону.

### Как установить

Python3 должен быть уже установлен. 
Затем установите зависимости из файла requirements.
```
pip3 install -r requirements.txt
```

### Как запустить
Скрипт запускается из консоли и использует в качестве аргумента число необходимых для генерации листов персонажей. По умолчанию, генерируется 1.
```shell
foo@bar ~ % python main.py 3
```

### Как использовать
После запуска, в папке templates появится несколько новых файлов вида:
```
1_filled..
2_filled..
```
Чтобы изменить шаблон или набор способностей, в файле main.py необходимо поправить соответствующие переменные:
```
TEMPLATES_FOLDER = 'templates'
TEMPLATE_NAME = 'charsheet.svg'
RESULT_NAME = 'filled_charsheet.svg'

SKILLS_LIST = [
    'Стремительный прыжок'...
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
