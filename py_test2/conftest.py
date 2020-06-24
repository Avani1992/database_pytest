import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="basic", help="my option: basic or FullFunction"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

#2.

# def pytest_addoption(parser):
#     parser.addoption(
#         "--runbasic ", action="store_true", default=False, help="run basic tests"
#     )
#
#
# def pytest_configure(config):
#     config.addinivalue_line("markers", "basic: mark test as basic to run")
#
#
# def pytest_collection_modifyitems(config, items):
#     if config.getoption("--runbasic"):
#         # --runbasic given in cli: do not skip basic tests
#         return
#     skip_basic = pytest.mark.skip(reason="need --runbasic option to run")
#     for item in items:
#         if "basic" in item.keywords:
#             item.add_marker(skip_basic)
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--runFulFunction", action="store_true", default=False, help="run FulFunction tests"
#     )
#
#
# def pytest_configure(config):
#     config.addinivalue_line("markers", "FulFunction: mark test as FulFunction to run")
#
#
# def pytest_collection_modifyitems(config, items):
#     if config.getoption("--runFulFunction"):
#         # --runFulFunction given in cli: do not skip FulFunction tests
#         return
#     skip_FulFunction = pytest.mark.skip(reason="need --runFulFunction option to run")
#     for item in items:
#         if "FulFunction" in item.keywords:
#             item.add_marker(skip_FulFunction)