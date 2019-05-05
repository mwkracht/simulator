"""Module contains classes for running time base simulations."""
import abc
import six

from trafficsim import errors

__all__ = (
    'BaseSimClass',
    'Simulator'
)


MS_IN_SEC = 1000.0


class BaseSimClass(six.with_metaclass(abc.ABCMeta, object)):
    """Base class defining interface of objects used in Simulator."""

    @abc.abstractmethod
    def ms_to_transition(self):
        """Return milliseconds until next state transition."""
        return

    @abc.abstractmethod
    def increment_time(self, milliseconds):
        """
        Increment internal time of simulated object as Simulator time passes.

        Args:
            milliseconds (int): milliseconds of time that has passed in simulation
        """
        return

    @abc.abstractmethod
    def display_ascii(self):
        """Return ascii display value of simulated object."""
        return


class Simulator(object):
    """Simulator that runs time based simulations on a provided set of BaseSimClass objects."""

    def __init__(self, simulated_objects):
        """
        Check if all objects have proper type and store objects to be simulated.

        Args:
            simulated_objects (BaseSimClass): objects to be simulated

        Raises:
            TypeError
        """
        if not all(isinstance(sim_object, BaseSimClass) for sim_object in simulated_objects):
            raise errors.IllegalSimulation('Invalid objects passed to Simulator constructor')

        self._simulated_objects = simulated_objects

    def step(self, milliseconds=None):
        """
        Run indefinite simulation.

        Args:
            milliseconds (int, optional): milliseconds to step through simulation, if not
                provided the step will be minimum time until next state transition

        Returns:
            int - number of milliseconds stepped
        """
        # Determine time to next step in simulation
        step_time = milliseconds or min(
            sim_object.ms_to_transition()
            for sim_object in self._simulated_objects
        )

        # Update simulated objects with step in simulation
        for sim_object in self._simulated_objects:
            sim_object.increment_time(step_time)

        return step_time

    def display(self):
        """Return dispaly string for current simulation state."""
        return '\n'.join([
            sim_object.display_ascii()
            for sim_object in self._simulated_objects
        ])
