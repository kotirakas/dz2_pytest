def test_append(lst):
    lst.append(5)
    assert len(lst) == 5


def test_insert(lst):
    lst.insert(2, 5)
    assert lst[2] == 5


def test_index(lst):
    lst.index(5)
    assert lst[5] == 8


def test_remove(lst):
    lst.remove(3)
    assert lst.count(3) == 2


def test_reverse(lst_with_params):
    lst_with_params.reverse()
    assert lst_with_params[0] == 1
