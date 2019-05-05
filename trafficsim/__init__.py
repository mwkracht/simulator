# pylint: skip-file
"""
Import submodule __all__ members so that they can be accessed directly through main package import.
This creates an import pattern where all "public" methods will be available through import of main package
so that downstream consumers do not have any dependencies on internal structure of this package. Of course
all methods are importable/public but if objects are not available through base import (i.e. import simple_app)
they should be treated as "private" and they can be moved within the package potentially breaking downstream imports.
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


import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

# Avoid 'no handlers could be found for logger' warnings if logging not configured for application
logging.getLogger(__name__).addHandler(NullHandler())


__version__ = '0.0.2'
__author__ = 'Matt Kracht'
__email__ = 'mwkracht@gmail.com'
__license__ = 'MIT'
