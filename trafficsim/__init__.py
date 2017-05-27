"""
Import submodules and expose __all__ members on base of simulator package
"""

# Import submodules and packages
from trafficsim import errors
from trafficsim import patterns
from trafficsim import simulator
from trafficsim import traffic_signal


# Expose __all__ attributes of submodules
from trafficsim.errors import *
from trafficsim.patterns import *
from trafficsim.simulator import *
from trafficsim.traffic_signal import *


# Build package-wide __all__ attribute
__all__ = (
	list(errors.__all__) +
    list(patterns.__all__) +
    list(simulator.__all__) +
    list(traffic_signal.__all__)
)


# Versioning
__version__ = '0.0.1'