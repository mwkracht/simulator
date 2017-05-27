"""
Module contains trafficsim custom excpetions
"""

__all__ = (
	'IllegalSimulation',
)

class IllegalSimulation(Exception):
	"""Unable to run given simulation"""
	pass 