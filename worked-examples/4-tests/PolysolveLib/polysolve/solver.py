from __future__ import annotations

import math
from cmath import sqrt

from cowsay import cow

CBRT_UNITY_IM = sqrt(3) / 2 * 1j


def quadratic(a: float, b: float, c: float) -> tuple[complex, complex]:
    """Solve for roots using the quadratic formula.

    Parameters
    ----------
    a : float
        :math: `x**2` coefficient.
    b : float
        :math: `x` coefficient.
    c : float
        Constant coefficient.

    Returns
    -------
    tuple[complex, complex]
        Quadratic roots.

    Examples
    --------
    >>> quadratic(3., 0., -1.)
    ((0.5773502691896257+0j), (-0.5773502691896257+0j))
    >>> quadratic(1, 2, 0)
    (0j, (-2+0j))
    >>> quadratic(1, 11, 28)
    ((-4+0j), (-7+0j))

    """
    det = b**2 - (4 * a * c)
    print(det)
    if math.isclose(det, 0):
        cow("Degenerate MOOoo-ts")

    return ((-b + sqrt(det)) / (2 * a), (-b - sqrt(det)) / (2 * a))


def cubic(a: float, b: float, c: float, d: float) -> tuple[complex, complex, complex]:
    r"""Solve for roots using the cubic formula.

    Parameters
    ----------
    a : float
        :math: `x**3` coefficient.
    b : float
        :math: `x**2` coefficient.
    c : float
        :math: `x` coefficient.
    d : float
        Constant coefficient.

    Returns
    -------
    tuple[complex, complex, complex]
        Cubic roots.

    Examples
    --------
    >>> cubic(1, 0, 0, 0)
      ___________________
    | Degenerate MOOoo-ts |
      ===================
                       \\
                        \\
                          ^__^
                          (oo)\\_______
                          (__)\\       )\\/\\
                              ||----w |
                              ||     ||
    (0j, 0j, (-0+0j))

    """
    q = (3 * a * c - b**2) / (9 * a**2)
    r = (9 * a * b * c - 27 * a**2 * d - 2 * b**3) / (54 * a**3)

    s = (r + sqrt(q**3 + r**2)) ** (1 / 3)
    t = (r - sqrt(q**3 + r**2)) ** (1 / 3)

    x1 = s + t - (b / 3 * a)
    x2 = -(s + t) / 2 - (b / 3 * a) + CBRT_UNITY_IM * (s - t)
    x3 = -(s + t) / 2 - (b / 3 * a) - CBRT_UNITY_IM * (s - t)

    out = (x1, x2, x3)

    if any(x == x1 for x in (x2, x3)):
        cow("Degenerate MOOoo-ts")

    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
