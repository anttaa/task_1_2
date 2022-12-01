def make_cook_book():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            name = line.strip()
            cook_book[name] = []
            for i in range(int(f.readline())):
                arr = f.readline().strip().split('|')
                cook_book[name].append({'ingredient_name': arr[0].strip(),
                                        'quantity': int(arr[1]),
                                        'measure': arr[2].strip()})

            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = make_cook_book()
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for item in cook_book[dish]:
                if item['ingredient_name'] in result:
                    result[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
                else:
                    result[item['ingredient_name']] = {'measure': item['measure'],
                                                       'quantity': (item['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return result


if __name__ == '__main__':
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))
