rom __future__ import print_function

import importlib
import sys

from distutils.version import LooseVersion as Version


def import_version(pkg, min_ver):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        if Version(mod.__version__) < min_ver:
            print(FAIL, "%s version %s or higher required, but %s installed." % (lib, min_ver, mod.__version__))
        else:
            print(OK, '%s version %s' % (pkg, mod.__version__))
    except ImportError:
        print(FAIL, '%s not installed' % pkg)
    return mod

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

# first check the python version
print('Using python in', sys.prefix)
print(sys.version)
pyversion = Version(sys.version)
if pyversion >= "3":
    if pyversion < "3.4":
        print(FAIL, "Python version 3.4 (or 2.7) is required, but %s is installed." % sys.version)
elif pyversion >= "2":
    if pyversion < "2.7":
        print(FAIL, "Python version 2.7 is required, but %s is installed." % sys.version)
else:
    print(FAIL, "Unknown Python version: %s" % sys.version)

print()
requirements = {'numpy': "1.6.1", 'scipy': "0.9", 'matplotlib': "1.0",
                'IPython': "3.0", 'sklearn': "0.15"}

# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)
