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
    """Wrapper class that combines a given state machine with interface required for simulation."""

    def __init__(self, pattern):
        """
        Initialize traffic signal object, automatically resetting provided pattern to initial state.

        Args:
            pattern (BasePattern): pattern that describes light transitions
        """
        self._pattern = pattern
        self._pattern.reset()

    # Overloaded methods
    # ==================

    def ms_to_transition(self):
        """Return milliseconds until next light transition."""
        return self._pattern.ms_to_next_state

    def increment_time(self, milliseconds):
        """
        Increment internal time of simulated object as Simulator time passes.

        Args:
            milliseconds (int): milliseconds of time that has passed in simulation
        """
        self._pattern.increment_time(milliseconds)

    def display_ascii(self):
        """
        Return current traffic signal state as ascii string image.

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
        """Return current light state."""
        return self._pattern.current_state
