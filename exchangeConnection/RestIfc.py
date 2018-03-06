"""REST Interface base class."""
import abc
# Import Built-Ins
import logging

# Init Logging Facilities
from exchangeConnection.BaseIfc import BaseIfc

log = logging.getLogger(__name__)


class RestIfc(BaseIfc):
    """REST Interface base class."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, rest_api):
        """Initialize class instance."""
        super(RestIfc, self).__init__(name=name, rest_api=rest_api)
