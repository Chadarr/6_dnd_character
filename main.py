import os
import sys
from faker import Faker
from random import randint, sample
from file_operations import render_template

SKILLS_LIST = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]

RUNIC_ALPHABET = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}
TEMPLATES_FOLDER = 'templates'
TEMPLATE_NAME = 'charsheet.svg'
RESULT_NAME = 'filled_charsheet.svg'


def str_to_runic(skill: str):
    runic_skill = ''
    for index in range(len(skill)):
        runic_letter = RUNIC_ALPHABET[skill[index]]
        runic_skill += runic_letter
    return runic_skill


def generate_template():
    fake = Faker('ru_RU')
    skill_set = sample(SKILLS_LIST, 3)
    TEMPLATE = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'job': fake.job(),
        'town': fake.city(),
        'strength': randint(3, 18),
        'agility': randint(3, 18),
        'endurance': randint(3, 18),
        'intelligence': randint(3, 18),
        'luck': randint(3, 18),
        'skill_1': str_to_runic(skill_set[0]),
        'skill_2': str_to_runic(skill_set[1]),
        'skill_3': str_to_runic(skill_set[2])
    }
    return TEMPLATE


def main():
    amount = int(sys.argv[1]) if (sys.argv[1] is not None) else 1
    for i in range(amount):
        context = generate_template()
        template_path = os.path.join(TEMPLATES_FOLDER, TEMPLATE_NAME)
        result_path = os.path.join(TEMPLATES_FOLDER, f'{i+1}_{RESULT_NAME}')
        render_template(template_path, result_path, context)


if __name__ == '__main__':
    main()
