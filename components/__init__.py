
from traitlets.config.configurable import Configurable
from traitlets import (
    Bool, Unicode, Int
)


class Foo(Configurable):
    """A class that has configurable, typed attributes.

    """

    i = Int(0, help="The integer i.").tag(config=True)
    j = Int(1, help="The integer j.").tag(config=True)
    name = Unicode(u'Brian', help="First name.").tag(config=True)


class Bar(Configurable):

    enabled = Bool(True, help="Enable bar.").tag(config=True)
