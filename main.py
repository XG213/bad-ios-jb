#!/usr/bin/env python3
# Sunstorm.py

"""
TODO:
  - `from pyimg4 import IM4P`, use pyimg4 lib instead of calling the bin version
  - Use RemoteZip to speed up having to download the full IPSW
"""

import sys
import os
import argparse
import zipfile
import subprocess
import shutil
import atexit
import tempfile
import glob

# Global variables
ROOT = os.path.dirname(__file__)
DEBUG = 0
LINUX = (sys.platform == 'linux')

# Append PATH
sys.path.append(ROOT + '/src')
os.environ['PATH'] = ((ROOT + '/bin') + ':' + os.environ.get('PATH'))

# Custom util in /src
from manifest import Manifest
import api

program_list = [
  'futurerestore',
  'img4tool',
  'Kernel64Patcher',
  'iBoot64Patcher',
  'ldid',
  'asr64_patcher',
  'restored_external64_patcher',
  # `hfsplus` comes from libdmg-hfsplus
  'hfsplus' if LINUX else 'hdiutil'
]
