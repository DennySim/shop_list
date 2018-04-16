def get_shop_list_by_dishes(order, person_count):
  with open('recipes_list.txt') as dishes:
      shop_list = {}
      for dish in dishes:
          dish_from_menu = dishes.readline().strip().lower()
          if dish_from_menu not in order:
              strings_to_skip = int(dishes.readline().strip())
              for i in range(0, strings_to_skip):
                  dishes.readline().strip()
          else:
              ing_quantity = int(dishes.readline().strip())
              for i in range(0, ing_quantity):
                  ing = dishes.readline().split('|')
                  new_shop_list_item = {'ingridient_name': ing[0].strip(), 'quantity': int(ing[1].strip()),
                                        'measure': ing[2].strip()}
                  new_shop_list_item['quantity'] *= person_count
                  if new_shop_list_item['ingridient_name'] not in shop_list:
                      shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                  else:
                      shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list


def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))


def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  order = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  print(order)
  shop_list = get_shop_list_by_dishes(order, person_count)
  print_shop_list(shop_list)


create_shop_list()