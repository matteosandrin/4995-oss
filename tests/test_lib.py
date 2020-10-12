from structoscope import echo

def test_echo():
    assert echo('This is a test') == 'This is a test'

def test_echo_failing():
    assert echo('This will fail') == 'This will pass'