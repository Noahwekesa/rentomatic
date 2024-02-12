from rentomatic.responses import responseSuccess


def test_response_success_is_true():
    assert bool(responseSuccess()) is True
