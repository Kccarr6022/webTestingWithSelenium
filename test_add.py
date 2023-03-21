def add(a, b):
    return a + b

class TestAdd:
    def test_add(self):
        assert add(1, 2) == 3

    def test_add2(self):
        assert add(1, 2) == 3
    