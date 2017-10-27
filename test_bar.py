from mock import patch

from bar import bar


@patch('foo.foo')
def test_patch_on_definition_does_not_work(mock_foo):
    mock_foo.return_value = 'foo'

    expected = 'foo'
    result = bar()

    assert expected == result


@patch('bar.foo', return_value='foo')
def test_patch_on_import_does_work(mock_foo):
    mock_foo.return_value = 'foo'

    expected = 'foo'
    result = bar()

    assert expected == result
