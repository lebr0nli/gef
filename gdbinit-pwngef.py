import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import gef as gef_mod

# we load gef as a module, so it won't pollute the global namespace of pwndbg
gef_mod.main()
