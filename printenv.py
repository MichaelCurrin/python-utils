#!/usr/bin/env python
"""
Copied from PyCharm script at:
    /Applications/PyCharm CE.app/Contents/bin/

This script is similar to bash commands:

    The env command can be used to show the environment, if no command is provided.
        $ env > vars.txt

    See /usr/bin/printenv utility or builtin.
        $ printenv > vars.txt

        $ printenv SHELL
        /bin/bash

        $ echo $SHELL
        /bin/bash
"""
# Dumps environment variables into specified file.
# Format: zero-separated "name=value" pairs in platform encoding.

import os
import sys

if len(sys.argv) != 2:
    raise Exception('Exactly one argument expected')

f = open(sys.argv[1], 'w')
try:
    for key, value in os.environ.items():
        f.writelines([key, '=', value, '\0'])
finally:
    f.close()
