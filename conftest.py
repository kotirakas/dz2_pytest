import pytest


@pytest.fixture()
def dctnr():
    """ фикстуры для теста dict"""
    return {t: t + (t * 3) for t in range(4)}


@pytest.fixture(
    params=[{t: t + (t * 3) for t in range(4)}, {t: t + 5 for t in range(6)}, {t: t + (t * 2) for t in range(5)}])
def dict_param(request):
    return request.param


@pytest.fixture()
def lst():
    """ фикстуры для теста list"""
    return [1, 3, 5, 6, 3, 8]


@pytest.fixture(params=[[1, 2, 4, 5, 8, 1], [1, 2, 3, 5, 2, 7], [5, 6, 9, 4, 7], [5, 7, 3, 9, 6, 1]])
def lst_with_params(request):
    return request.param


@pytest.fixture(params=[{'2', '3', '4', 'e', '5'}, {'3', '5', 'f', 't', '7'}, {'3', '5', 'h', '4', 's'}])
def set_param(request):
    """фикстура для теста set"""
    return request.param


@pytest.fixture()
def stlg():
    """ фикстуры для теста string"""
    return 'happy new 2020 year'


@pytest.fixture(params=['summer202', 'river', '34antrekot'])
def stlg_param(request):
    return request.param
