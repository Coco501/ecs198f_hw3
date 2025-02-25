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

A = list(range(500))

for i in range(1, len(A)):
	if i % 5 == 0 and i % 3 == 0:
		A[i] = "Baz"
	elif i % 3 == 0:
		A[i] = "Foo"
	elif i % 5 == 0:
		A[i] = "Bar"
	else:
		A[i] = str(i)

def test_list_500():
	for i in range(1, len(A)):
		assert foo_bar_baz(i).split()[-1] == A[i], f"foo_bar_baz({i}) failed"

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
    assert foo_bar_baz(608106).split()[-1] == "Foo"
    assert foo_bar_baz(360916).split()[-1] == "360916"
    assert foo_bar_baz(461980).split()[-1] == "Bar"
    assert foo_bar_baz(461985).split()[-1] == "Baz"
	
