from hooks import templates
from hooks.helpers import ResponseProcess


def test_response_process():
    response_one = ResponseProcess('algos-resources').make_response()
    response_two = ResponseProcess('hitchhikers-zen').make_response()

    assert (response_one, response_two) == (templates.ALGOS_RESOURCES,
                                            templates.HITCHHIKERS_ZEN)


def test_failde_response_process():
    response = ResponseProcess('').make_response()
    assert response is None
