def test_one():
    """проверка что длина объединенного множества будет равна 3 """
    a = {'a', 'v', 'x', 'a', 'v'}
    b = {'s', 'd', 's'}
    assert len(a | b) == 3


def test_two():
    """проверка что удаленный элемент был не единичный"""
    a = {'a', 'v', 'x', 'a', 'z', 'w'}
    a.pop()
    assert len(a) == 5


def test_three():
    """проверка что копия верна"""
    a = {'a', 'v', 'x', 'a', 'v', 'w'}
    assert (a.copy()) == a


def test_four(set_param):
    """проверка что 4 уже есть во множестве"""
    set_param.add('4')
    assert len(set_param) == 5


def test_five():
    """проверка что есть общие значения"""
    a = {'s', '4', 'e', 'q'}
    b = {'q', 'a', 'w', 'k'}
    assert (a.isdisjoint(b)) == False
