from __future__ import annotations

from math import sqrt

def quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Solves the roots of a quadratic equation.

    Uses the quadratic formula. Result must be real.

    Parameters
    ----------
    a
       :math:`x^2` coefficient.
    b
       :math:`x` coefficient.
    c
       Constant value.

    Returns
    -------
    tuple[float, float]
        Positive and negative roots of quadratic.

    Raises
    ------
    ValueError
        Discriminant < 0 implying imaginary root.

    Notes
    -----
    Equation of the form:

    .. math::

        ax^{2} + bx + c

    Examples
    --------
    >>> quadratic(1, 2, 0)
    (0.0, -2.0)
    >>> quadratic(3., 0., -1.)
    (0.5773502691896257, -0.5773502691896257)

    See Also
    --------
    numpy.polyval : Evaluate polynomial at point.

    References
    ----------
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
           expert systems ...
    """

    det = b**2 - (4*a*c)

    return ((-b + sqrt(det)) / (2*a),
            (-b - sqrt(det)) / (2*a))
