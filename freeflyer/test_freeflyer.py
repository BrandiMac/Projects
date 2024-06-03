"""
The Starship problem - unit and case tests
Author: Brandi McPherson, brandimcpher@gmail.com
"""

from program import USSFreeFlyer


def test_case_one():
    """
    FreeFlyer thrusts in the positive x-direction, turns around and thrusts in
    the negative x-direction, causing it to stop.

    """
    # Expected
    expected_pos = (3, 0)
    expected_vel = (0, 0)
    expected_or = (-1, 0)

    # Actual
    actual = USSFreeFlyer("TLLT")

    # Test
    assert actual.position == expected_pos
    assert actual.velocity == expected_vel
    assert actual.orientation == expected_or


def test_case_two():
    """
    FreeFlyer moves in the positive x-direction 3 units and then in the
    positive y-direction by 6 units. Note that the FreeFlyer cruises towards
    the end of the maneuver plan before stopping.

    """
    # Expected
    expected_pos = (3, 6)
    expected_vel = (0, 0)
    expected_or = (0, -1)

    # Actual
    actual = USSFreeFlyer("TLLTRTRRCCCT")

    # Test
    assert actual.position == expected_pos
    assert actual.velocity == expected_vel
    assert actual.orientation == expected_or


def test_case_three():
    """
    FreeFlyer moves in the position y-direction, turns around, and returns to
    the origin

    """
    # Expected
    expected_pos = (0, 0)
    expected_vel = (0, 0)
    expected_or = (0, 1)

    # Actual
    actual = USSFreeFlyer("LTLLTTRRT")

    # Test
    assert actual.position == expected_pos
    assert actual.velocity == expected_vel
    assert actual.orientation == expected_or


def test_rotate_ccw():
    """
    Test a single CCW rotation
    """
    # Expected
    expected_or = (0, 1)

    # Actual
    actual = USSFreeFlyer("L")

    # Test
    assert actual.orientation == expected_or


def test_rotate_cw():
    """
    Test a single CW rotation
    """
    # Expected
    expected_or = (0, -1)

    # Actual
    actual = USSFreeFlyer("R")

    # Test
    assert actual.orientation == expected_or


def test_thrusters():
    """
    Test a single execution of the thrusters
    """
    # Expected
    expected_pos = (1, 0)
    expected_vel = (1, 0)

    # Actual
    actual = USSFreeFlyer("T")

    # Test
    assert actual.position == expected_pos
    assert actual.velocity == expected_vel


def test_cruise():
    """
    Test a single execution of cruise
    """
    # Expected
    expected_pos = (0, 0)
    expected_vel = (0, 0)

    # Actual
    actual = USSFreeFlyer("C")

    # Test
    assert actual.position == expected_pos
    assert actual.velocity == expected_vel


def test_neg_vel():
    """
    Test that thrust can occur in negative direction
    """
    # Expected
    expected_pos = (-2, 0)
    expected_vel = (-1, 0)
    expected_or = (-1, 0)

    # Actual
    actual = USSFreeFlyer("LLTC")

    # Test
    assert actual.position == expected_pos
    assert actual.velocity == expected_vel
    assert actual.orientation == expected_or
