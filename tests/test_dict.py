def test_one(dctnr):
    dctnr.popitem()
    assert len(dctnr) <= 3


def test_two(dctnr):
    assert (dctnr.get(3)) > 7


def test_three(dctnr):
    dctnr[5] = 34
    assert len(dctnr) == 5


def test_four(dict_param):
    assert dict_param.setdefault(5) == None


def test_five(dctnr):
    assert dctnr.copy() == dctnr
