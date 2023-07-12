"""
"""

import shimport  # noqa


def test_shimport():
    os = shimport.lazy("os")
    assert os.path
