import shimport


def test_wrapper():
    namespace = shimport.wrapper("pathlib")


def test_wrap():
    namespace = shimport.wrap("pathlib")


def test_lazy():
    pathlib = shimport.lazy("pathlib")
    assert pathlib.Path(".").absolute() is not None
