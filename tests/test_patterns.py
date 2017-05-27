"""
Module contains unit tests for BasePattern class and
all other sublcassed Pattern classes
"""
import pytest


from trafficsim import patterns


# BasePattern Tests
# =================

def test_base_constructor_base_attrs():
    """Assert base set of attributes applied to object"""
    pattern = patterns.BasePattern()

    # Assert attributes are found
    assert hasattr(pattern, '_first_node')
    assert hasattr(pattern, '_current_node')
    assert hasattr(pattern, 'ms_to_next_state')
    assert hasattr(pattern, 'ms_ellapsed')

    # Assert initial states are as expected
    assert pattern._first_node == pattern._current_node
    assert pattern.ms_to_next_state == 0
    assert pattern.ms_ellapsed == 0


def test_base_increment_time():
    """Assert incrementing time on base class raises not implemented exception"""
    pattern = patterns.BasePattern()

    with pytest.raises(NotImplementedError):
        pattern.increment_time(1000)


def test_base_current_state():
    """Assert current state returns the state object of the current node attribute"""
    pattern = patterns.BasePattern()

    # Initially the current state is None
    assert not pattern.current_state

    # Update state attribute of current node and verify current state
    pattern._current_node.state = 'Test object'
    assert pattern.current_state == 'Test object'


def test_base_reset():
    """Assert reset restores current to first state and resets time"""
    pattern = patterns.BasePattern()

    # Set pattern attributes to state other than initial
    pattern._current_node = 'Some other object'
    pattern._first_node.duration = 40 #ms
    pattern.ms_ellapsed = 1000 #ms

    pattern.reset()

    assert pattern._current_node == pattern._first_node
    assert pattern.ms_ellapsed == 0
    assert pattern.ms_to_next_state == 40


# SimplePattern Tests
# ===================

def test_simple_constructor():
    """Assert constructor correctly creates state machine from inputs"""
    pattern = patterns.SimplePattern(100, 200, 300)

    # First state should be green
    assert pattern._current_node == pattern._first_node
    assert pattern._current_node.state == patterns.State.GREEN
    assert pattern._current_node.duration == 300

    # Increment to second node, which should be yellow
    pattern._current_node = pattern._current_node.next
    assert pattern._current_node.state == patterns.State.YELLOW
    assert pattern._current_node.duration == 200

    # Increment to third node, which should be red
    pattern._current_node = pattern._current_node.next
    assert pattern._current_node.state == patterns.State.RED
    assert pattern._current_node.duration == 100

    # Node after the third should go back to first
    pattern._current_node = pattern._current_node.next
    assert pattern._current_node == pattern._first_node

    # Lastly assert period is the sum of all durations
    assert pattern._period == 600


def test_simple_increment_time():
    """Assert increment time properly transitions states"""
    pattern = patterns.SimplePattern(100, 200, 300)

    # Assert incrementing to 1ms less than next transition does not change state
    assert pattern.ms_to_next_state == 300
    pattern.increment_time(pattern.ms_to_next_state - 1)
    assert pattern.ms_to_next_state == 1
    assert pattern._current_node.state == patterns.State.GREEN

    # Assert incrementing by exactly ms_to_next_state transitions state
    assert pattern.ms_to_next_state == 1
    pattern.increment_time(pattern.ms_to_next_state)
    assert pattern.ms_to_next_state == 200
    assert pattern._current_node.state == patterns.State.YELLOW

    # Assert incrementing by 1ms less than the period reverses state
    assert pattern._period == 600
    pattern.increment_time(pattern._period - 1)
    assert pattern.ms_to_next_state == 1
    assert pattern._current_node.state == patterns.State.GREEN

    # Assert incrementing by exactly the period, no state changes
    pattern.increment_time(pattern._period)
    assert pattern.ms_to_next_state == 1
    assert pattern._current_node.state == patterns.State.GREEN

