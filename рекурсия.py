def factorial(num):
    """ ПОИСК ФАКТОРИАЛА ЧИСЛА"""
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(3))



def find_element_in_html_code(tree, elem):
    """Функция обходит дерево из списка списков (например структуру DOM_HTML"""
    if elem in tree:
        return tree[elem]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            res = find_element_in_html_code(sub_tree, elem)
            if res:
                break
    else:
        res = None
    return res


html_code = {
    'html': {
        'head': {
            'title': "Заголовок страницы",
            'link': "ссылка на CSS"
        },
        'body': {
            'h1': "Главный заголовок",
            'h2': "Подзаголовок",
            'div': "Жили были кит и кот",
            'p': "Кот и кит - наоборот"
        }
    }
}

print(find_element_in_html_code(html_code, "div"))