import pytest

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
	
