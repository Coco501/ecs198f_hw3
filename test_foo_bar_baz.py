import pytest

def testAgainstCorrect():
	from foo_bar_baz import foo_bar_baz
	def correct_foo_bar_baz(n: int) -> str:
			return_str = ""
			for i in range(1, n + 1, 1):
				if (i % 3 == 0) and (i % 5 == 0):
					return_str += "Baz"
				elif i % 3 == 0:
					return_str += "Foo"
				elif i % 5 == 0:
					return_str += "Bar"
				else:
					return_str += str(i)
				if i < n:
					return_str += " "
			return return_str

	for i in range(-100, 1000):
		assert correct_foo_bar_baz(i) == foo_bar_baz(i)

	for i in range (1, 1000):
		assert not foo_bar_baz(i).endswith(" "), f"foo_bar_baz({i}) ended with ' '."

def test_negative_numbers():
	from foo_bar_baz import foo_bar_baz
	assert foo_bar_baz(-1253) == ""
	assert foo_bar_baz(-5) == ""
	assert foo_bar_baz(-0) == ""

def test_wrong_types():
    from foo_bar_baz import foo_bar_baz
    with pytest.raises(TypeError):
        foo_bar_baz("string type")
    with pytest.raises(TypeError):
        foo_bar_baz(3.14)
    with pytest.raises(TypeError):
        foo_bar_baz()

def test_large_numbers_return():
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(608106).split()[-1] == "Foo"
    assert foo_bar_baz(360916).split()[-1] == "360916"
    assert foo_bar_baz(461980).split()[-1] == "Bar"
    assert foo_bar_baz(461985).split()[-1] == "Baz"
	
