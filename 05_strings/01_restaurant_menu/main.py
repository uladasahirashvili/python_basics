user_menu = input("Today's menu: ")

menu_list = user_menu.split(';')
capitalized_menu = [dish.title() for dish in menu_list]
menu = ', '.join(capitalized_menu)

print('We currently have:', menu)
