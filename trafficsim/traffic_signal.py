"""
Module contains class that implements a traffic signal.

Traffic lights are initialized with a given pattern
for light transitions and provide methods for determining
time until light change and for visual display.
"""
from trafficsim.simulator import BaseSimClass
from trafficsim.patterns import State
from trafficsim import display

__all__ = (
    'TrafficSignal',
)


class TrafficSignal(BaseSimClass):
    """Simple class that wraps a given state machine with interface
    to be used in simulation"""

    def __init__(self, pattern):
        """Initialize traffic signal object, automatically resets provided
        pattern to initial state.

        Args:
            pattern (BasePattern): pattern that describes light transitions
        """
        # Store pattern object and reset pattern to initial state
        self._pattern = pattern
        self._pattern.reset()

    # Overloaded methods
    # ==================

    def ms_to_transition(self):
        """Returns milliseconds until next light"""
        return self._pattern.ms_to_next_state

    def increment_time(self, milliseconds):
        """Increment internal time of simulated object as Simulator time passes

        Args:
            milliseconds (int): milliseconds of time that has passed in simulation
        """
        self._pattern.increment_time(milliseconds)

    def display_ascii(self):
        """Display traffic signal

        Returns:
            str - ascii art display string
        """
        if self.current_light() == State.GREEN:
            return display.GREEN_LIGHT
        elif self.current_light() == State.YELLOW:
            return display.YELLOW_LIGHT

        # Default to displaying red light. Seems safer that way...
        return display.RED_LIGHT

    # TrafficSignal specific methods
    # ==============================

    def current_light(self):
        """Returns current light color"""
        return self._pattern.current_state

