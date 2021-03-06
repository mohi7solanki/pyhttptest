from unittest.mock import patch

import pytest

from requests import Response

from pyhttptest import http
from pyhttptest.exceptions import HTTPMethodNotSupportedError


def test_method_dispatcher():
    with pytest.raises(HTTPMethodNotSupportedError) as exc:
        args = ('head', 'http://localhost:8080/users')
        http.method_dispatcher(*args)

    exception_message = "An HTTP method ('HEAD') is not supported by the application."

    assert exception_message == str(exc.value)


@patch('pyhttptest.http.requests.get', return_value=Response)
def test_get(mock):
    mock.return_value.status_code = 200
    args = ('get', 'http://localhost:8080/users')
    response = http.get(*args)

    assert response.status_code == 200


@patch('pyhttptest.http.requests.post', return_value=Response)
def test_post(mock):
    mock.return_value.status_code = 200
    args = ('post', 'http://localhost:8080/users')
    response = http.post(*args)

    assert response.status_code == 200


@patch('pyhttptest.http.requests.put', return_value=Response)
def test_put(mock):
    mock.return_value.status_code = 204
    args = ('put', 'http://localhost:8080/users/1')
    response = http.put(*args)

    assert response.status_code == 204


@patch('pyhttptest.http.requests.delete', return_value=Response)
def test_delete(mock):
    mock.return_value.status_code = 204
    args = ('delete', 'http://localhost:8080/users/1')
    response = http.delete(*args)

    assert response.status_code == 204
