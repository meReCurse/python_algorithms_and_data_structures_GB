# -*- coding: utf-8 -*-

'''
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
import collections

# без коллекций.
def calc_profit():
	quantity_of_companies = int(input('Введите количество предприятий: '))
	dict_of_companies_n_quarter_profit = {}

	for i in range(1, quantity_of_companies + 1):
		name = input('Введите название предприятия: ')
		company_year_profit = []
		for quarter in range(1, 5):
			quarter_profit = int(input(f'Доход за {quarter} квартал: '))
			company_year_profit.append(quarter_profit)
		dict_of_companies_n_quarter_profit[name] = company_year_profit

	# создаем список сумм (хотя можно было в цикле аппендить уже общую сумму, но предположим,
	# что необходимо сохранять квартальные значения)
	list_of_all_profits = [item for sublist in dict_of_companies_n_quarter_profit.values() for item in [sum(sublist)]]
	average_profit = sum(list_of_all_profits) / len(list_of_all_profits)
	print(f'\nСредняя прибыль организаций за год: {average_profit} руб.\n')

	companies_year_profit = dict(zip(dict_of_companies_n_quarter_profit, list_of_all_profits))

	companies_with_less_than_av = {k: v for k, v in companies_year_profit.items() if v < average_profit}
	companies_with_more_than_av = {k: v for k, v in companies_year_profit.items() if v > average_profit}
	print(f'Прибыль ниже средней: {companies_with_less_than_av}\n')
	print(f'Прибыль выше средней: {companies_with_more_than_av}\n')

calc_profit()

# используя коллекции.
def calc_profit_with_col():
	quantity_of_companies = int(input('Введите количество предприятий: '))
	Company = collections.namedtuple('Company', ['name', 'profit'])
	lst_of_comps = []
	for i in range(1, quantity_of_companies + 1):
		name = input('Введите имя: ')
		profit = 0
		for quarter in range(1, 5):
			profit += int(input(f'Доход за {quarter} квартал: '))
		company = Company(name, profit)
		lst_of_comps.append(company)

	average_profit = sum([company.profit for company in lst_of_comps]) / len(lst_of_comps)
	print(f'\nСредняя прибыль организаций за год: {average_profit} руб.\n')

	comps_with_less_than_av = [company for company in lst_of_comps if company.profit < average_profit]
	comps_with_more_than_av = [company for company in lst_of_comps if company.profit > average_profit]
	print(f'Прибыль ниже средней: {comps_with_less_than_av}\n')
	print(f'Прибыль выше средней: {comps_with_more_than_av}\n')

calc_profit_with_col()
# Итого: использование именнованного кортежа позволило значительно упростить генераторные выражения.
# алгоритмы решений с DefaultDict и OrderedDict по сути не будет отличаться от первоначального и при этом не будут
# использованы их особенности, поэтому не буду простыню из кода присылать.
