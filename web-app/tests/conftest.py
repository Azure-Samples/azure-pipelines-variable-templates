from pytest import fixture


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store"
    )

@fixture()
def url(request):
    return request.config.getoption("--url")