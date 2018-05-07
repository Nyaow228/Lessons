import sys

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite')
#Анонимная функция.

def action_add():
	"""Добавить URL-адрес"""
	url = input('\nВведите URL-адрес: ')

	with get_connection() as conn:
		short_url = storage.add_url(conn, url)

def action_find():
	"""Найти оригинальный URL-адрес"""


def action_find_all():
	"""Вывести все URL-адреса"""
	with get_connection() as conn:
		urls = storage.find_all(conn)

		template = '{url[short_url]} - {url[original_url]} - {url[created]}'

		for url in urls:
			template.format(url['short_url'], url['original_url']

def action_show_menu():
    """Показать меню"""
    print('''
    1. Добавить URL-адрес
    2. Найти оригинальный URL-адрес
    3. Вывести все URL-адреса
    m. Показать меню
    q. Выйти
''')

def action_exit():
	"""Выйти"""
	sys.exit(0)
	


def main():
	with get_connection() as conn:
		storage.initialize(conn)
	
	action_show_menu()
	
	actions = {
		'1': action_add,
		'2': action_find,
		'3': action_find_all,
		'm': action_show_menu,
		'q': action_exit,
	}
	
	while 1:
		cmd = input('\nВведите команду: ')
		action = actions.get(cmd)
		
		if action:
			action()
		else:
			print('Неизвестная команда')
			
