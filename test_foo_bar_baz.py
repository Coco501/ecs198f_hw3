import pytest
from foo_bar_baz import foo_bar_baz

expected_outputs = [ # 1 - 15
    "",
    "1",  
    "1 2",  
    "1 2 Foo",  
    "1 2 Foo 4",  
    "1 2 Foo 4 Bar",  
    "1 2 Foo 4 Bar Foo",  
    "1 2 Foo 4 Bar Foo 7",  
    "1 2 Foo 4 Bar Foo 7 8",  
    "1 2 Foo 4 Bar Foo 7 8 Foo",  
    "1 2 Foo 4 Bar Foo 7 8 Foo Bar", 
    "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11",  
    "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo",  
    "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13",  
    "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14",  
    "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz",  
]

#Add testcases Here
def test_regular_numbers():
    # positive tests

    for i in range(0, len(expected_outputs)):
        assert foo_bar_baz(i) == expected_outputs[i], f"foo_bar_baz({i}) failed"

def test_negative_numbers():
    assert foo_bar_baz(-1253) == ""
    assert foo_bar_baz(-5) == ""
    assert foo_bar_baz(-0) == ""

def test_wrong_types():
    with pytest.raises(TypeError):
        foo_bar_baz("string type")
    with pytest.raises(TypeError):
        foo_bar_baz(3.14)
    with pytest.raises(TypeError):
        foo_bar_baz()

def test_large_numbers_return():
    assert isinstance(foo_bar_baz(608106), str)
    assert isinstance(foo_bar_baz(360916), str)
    assert isinstance(foo_bar_baz(461980), str)
