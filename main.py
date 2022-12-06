#!/usr/bin/env python3
# main.py

"""
TODO:
  - `from pyimg4 import IM4P`, use pyimg4 lib instead of calling the bin version
  - Use RemoteZip to speed up having to download the full IPSW
"""
#a bunch of this is stolen from sunst0rm and palera1n

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

def main():
    # Arg-parser:
    credit = """
    some code by mineek, some code by m1n1exploit
    """

    parser = argparse.ArgumentParser(description='iOS Tethered IPSW Restore', epilog=credit)
    conflict = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument('-i', '--ipsw', help='IPSW to restore', required=True)
    parser.add_argument('-t', '--blob', help='Blob (shsh2) to use', required=True)
    parser.add_argument('-d', '--boardconfig', help='BoardConfig to use', required=True)
    parser.add_argument('-kpp', '--kpp', help='Use Kernel Patch Protection (KPP) (Required on devices lower than A9)', required=False, action='store_true')
    parser.add_argument('-id', '--identifier', help='Identifier to use (ex. iPhoneX,X)', required=False)
    # These options cannot be used together:
    conflict.add_argument('-b', '--boot', help='Create Boot files', action='store_true')
    conflict.add_argument('-r', '--restore', help='Create Restore files', action='store_true')
    # Finally, parse:
    args = parser.parse_args()
    # Arg-parser will exit for us if there's a argument error
    check_for_dependencies()

    # Cast/modify arguments here before passing
    restore = bool(args.restore)
    boot = bool(args.boot)
    ipsw  = os.path.realpath(args.ipsw)
    blob = os.path.realpath(args.blob)
    boardconfig = str(args.boardconfig).lower() # lowercase board to avoid missing errors
    kpp = bool(args.kpp)
    identifier = args.identifier

    if not os.path.exists(ipsw):
      print_error(f'IPSW "{ipsw}" doesn\'t exist')
      sys.exit(1)

    if not os.path.exists(blob):
      print_error(f'Blob "{blob}" doesn\'t exist')
      sys.exit(1)

    if boot and not identifier:
      print_error('You need to specify an identifier (--identifier)')
      sys.exit(1)

    if restore:
      prep_restore(ipsw, blob, boardconfig, kpp)
    elif boot:
      prep_boot(ipsw, blob, boardconfig, kpp, identifier)
    else:
      print_error('No mode selected (this is a bug)')
      print(args)
      sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
  main()
