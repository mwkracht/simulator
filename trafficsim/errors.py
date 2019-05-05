"""Module contains custom excpetions for trafficsim package."""

__all__ = (
    'IllegalSimulation',
    'SimulationTerminated'
)


class IllegalSimulation(Exception):
    """Raised when unable to run given simulation."""


class SimulationTerminated(Exception):
    """Raised when simulation is terminated."""
