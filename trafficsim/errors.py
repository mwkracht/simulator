"""
Module contains trafficsim custom excpetions
"""

__all__ = (
	'IllegalSimulation',
	'SimulationTerminated'
)

class IllegalSimulation(Exception):
	"""Unable to run given simulation"""
	pass


class SimulationTerminated(Exception):
	"""Simulation was terminated"""
	pass