def test_one(stlg):
    """ проверка что все цифры """
    assert stlg.isdigit() == True


def test_two(stlg):
    assert stlg.isalpha() == False


def test_three(stlg):
    assert stlg.isalnum() == True


def test_four(stlg_param):
    assert len(stlg_param) > 6


def test_five(stlg):
    """проверка что все значения в нижнем регистре"""
    assert stlg.islower() == True
