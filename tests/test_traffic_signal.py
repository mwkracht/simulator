"""
Module contains unit tests for TrafficSignal class. Note,
the tests will only cover methods that are distinct to
this class and are not simple wrapper methods around light
pattern.
"""
import mock

from trafficsim import display
from trafficsim import patterns
from trafficsim import traffic_signal


@mock.patch('trafficsim.traffic_signal.TrafficSignal.current_light')
def test_display_ascii(mock_color):
    """Assert signal correctly displays for each possible state"""
    pattern = patterns.SimplePattern(50, 20, 30)
    t_signal = traffic_signal.TrafficSignal(pattern)

    # Assert red displays correctly
    mock_color.return_value = patterns.State.RED
    assert t_signal.display_ascii() == display.RED_LIGHT

    # Assert yellow displays correctly
    mock_color.return_value = patterns.State.YELLOW
    assert t_signal.display_ascii() == display.YELLOW_LIGHT

    # Assert green displays correctly
    mock_color.return_value = patterns.State.GREEN
    assert t_signal.display_ascii() == display.GREEN_LIGHT

    # Assert unknown color displays as red
    mock_color.return_value = 'unknown'
    assert t_signal.display_ascii() == display.RED_LIGHT
