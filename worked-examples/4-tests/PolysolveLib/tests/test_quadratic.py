import cmath

import pytest

from polysolve.solver import quadratic


def quad(a, b, c, x):
    return a * x**2 + b * x + c


def test_roots():
    """Tests that quadratic finds the root for a known problem."""
    params = (3.0, 0.0, -1.0)
    roots = quadratic(*params)

    assert all(cmath.isclose(quad(*params, root), 0.0) for root in roots)


@pytest.mark.parametrize(
    "params, expected",
    [
        ([1.0, 0.0, 0.0], [0.0, 0.0]),
        ([1.0, 14.0, 49.0], [-7.0, -7.0]),
        ([3.0, 2.0, -1.0], [1 / 3, -1.0]),
    ],
)
def test_quadratic(params, expected):
    """Test quadratic meets expectations."""
    assert all(map(cmath.isclose, quadratic(*params), expected))


def test_quadratic_fails():
    """Check bad quadratic raises error."""
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        # There are infinite roots on this flat line.
        quadratic(0.0, 0.0, 0.0)
