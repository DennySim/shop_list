
# def create_menu_dict():
#    with open('recipes_list.txt') as dishes:
#        cook_book = {}
#        for dish in dishes:
#            dish = dish.strip().lower()
#            ing_quantity = int(dishes.readline().strip())
#            for i in range(ing_quantity):
#                ing = dishes.readline().split('|')
#                new_shop_list_item = {'ingridient_name': ing[0].strip(), 'quantity': int(ing[1].strip()),
#                                     'measure': ing[2].strip()}
#                cook_book[dish] = new_shop_list_item
#            dishes.readline().strip()
#    return cook_book

def create_menu_dict():
   with open('recipes_list.txt') as dishes:
       cook_book = {}
       for dish in dishes:
           dish = dish.strip().lower()
           ing_quantity = int(dishes.readline().strip())
           cook_book[dish] = {}
           for i in range(ing_quantity):
               ing = dishes.readline().split('|')
               new_shop_list_item = {'ingridient_name': ing[0].strip(), 'quantity': int(ing[1].strip()),
                                    'measure': ing[2].strip()}
               cook_book[dish][ing[0].strip()] = new_shop_list_item
           dishes.readline().strip()
   return cook_book


def create_shop_list_by_dishes(order, person_count):
  shop_list = {}
  new_shop_list_item = {}
  menu = create_menu_dict()
  for dish_from_menu in menu:
      if dish_from_menu in order:
          new_shop_list_item = menu.get(dish_from_menu)
          for i in new_shop_list_item:
              new_shop_list_item[i]['quantity'] *= person_count
              if i not in shop_list:
                  shop_list[i] = new_shop_list_item[i]
              else:
                  shop_list[new_shop_list_item[i]]['quantity'] += new_shop_list_item['quantity']

  return shop_list


# def get_shop_list_by_dishes(order, person_count):
#   with open('recipes_list.txt') as dishes:
#       shop_list = {}
#       for dish in dishes:
#           # dish_from_menu = dishes.readline().strip().lower() ##### Ниже исправленная строка
#           dish_from_menu = dish.strip().lower()
#           if dish_from_menu not in order:
#               strings_to_skip = int(dishes.readline().strip())
#               for i in range(strings_to_skip + 1): ##### Добавил "+1" для SKIP между рецептами
#                   dishes.readline().strip()
#           else:
#               ing_quantity = int(dishes.readline().strip())
#               print("кол-во", ing_quantity)
#               for i in range(ing_quantity):
#                   ing = dishes.readline().split('|')
#                   new_shop_list_item = {'ingridient_name': ing[0].strip(), 'quantity': int(ing[1].strip()),
#                                         'measure': ing[2].strip()}
#                   print('item=', new_shop_list_item)
#                   new_shop_list_item['quantity'] *= person_count
#                   if new_shop_list_item['ingridient_name'] not in shop_list:
#                       shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
#                   else:
#                       shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
#               dishes.readline().strip() ##### Добавил SKIP между рецептами
#   return shop_list


def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))


def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  order = input('Введите блюда в расчете на одного человека '
                '(через запятую): ') \
    .lower().split(', ')
  print(order)
  shop_list = create_shop_list_by_dishes(order, person_count)
  print_shop_list(shop_list)


create_shop_list()
