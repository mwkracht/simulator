"""
Module contains collection of possible traffic light patterns.

Each pattern contains a state machine which determines color sequences and duration of the lights.
"""
import abc
import six


__all__ = (
    'SimplePattern',
    'State'
)


# State Machine Classes
# ================================

class Node(object):  # pylint: disable=too-few-public-methods
    """Base object for constructing Pattern state machines."""

    def __init__(self, state, duration, next_node):
        """Construct State Machine Node.

        Args:
            state (object): descriptor of node state
            duration (int): milliseconds that state will last
            next_node (Node): next Node to transition to
        """
        self.state = state
        self.duration = duration
        self.next_node = next_node


class State(object):  # pylint: disable=too-few-public-methods
    """Enum pattern states to avoid magic strings."""

    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'


# Pattern Classes
# ===============

class BasePattern(six.with_metaclass(abc.ABCMeta, object)):
    """Base class for all Pattern classes."""

    def __init__(self):
        """
        Initialize pattern object with fixed base attributes.

        _first_node (Node): initial state of the state machine
        _current_node (Node): current state of the state machine
        ms_ellapsed (int): milliseconds ellapsed for pattern
        ms_to_next_state (int): milliseconds until next state transition
        """
        self._first_node = Node(state=None, duration=0, next_node=None)
        self._current_node = self._first_node
        self.ms_to_next_state = self._first_node.duration
        self.ms_ellapsed = 0

    @abc.abstractmethod
    def increment_time(self, milliseconds):
        """
        Move the time of the pattern ahead the given milliseconds.

        Args:
            milliseconds (int): milliseconds to increment time
        """
        return

    @property
    def current_state(self):
        """Return current node state object."""
        return self._current_node.state

    def reset(self):
        """Reset pattern by setting current state to initial state and time to 0ms."""
        self._current_node = self._first_node
        self.ms_to_next_state = self._first_node.duration
        self.ms_ellapsed = 0


class SimplePattern(BasePattern):
    """Traffic light pattern that has fixed durations for green/yellow/red light states."""

    def __init__(self,
                 red_duration,
                 yellow_duration,
                 green_duration):
        """
        Create simple pattern object, using provided durations to describe light pattern.

        Note: All SimplePatterns will start from in green state that
        will last the full duration provided for the green light.

        Args:
            red_duration (int): duration of red light state in ms
            yellow_duration (int): duration of yellow light state in ms
            green_duration (int): duration of green light state in ms
        """
        super(SimplePattern, self).__init__()

        # Initialize all states for this pattern
        red = Node(state=State.RED, duration=red_duration, next_node=None)
        yellow = Node(state=State.YELLOW, duration=yellow_duration, next_node=red)
        green = Node(state=State.GREEN, duration=green_duration, next_node=yellow)
        red.next_node = green

        # Store period of state machine to speed time increments
        self._period = sum([red.duration, yellow.duration, green_duration])

        # Set point to first state of state machine and reset pattern
        self._first_node = green
        self.reset()

    def increment_time(self, milliseconds):
        """
        Move the time of the pattern ahead by the given milliseconds.

        Args:
            milliseconds (int): milliseconds to increment time
        """
        # Get modulus of time increment with period because an increment in time of
        # one period of the pattern will not change state or ms until next state
        phase = milliseconds % self._period

        # Cycle through states until new current state is found
        while phase >= self.ms_to_next_state:
            phase -= self.ms_to_next_state
            self._current_node = self._current_node.next_node
            self.ms_to_next_state = self._current_node.duration

        # Current state is found so decrement remaining phase from duration to next state
        self.ms_to_next_state -= phase

        # Increment patterns time
        self.ms_ellapsed += milliseconds
