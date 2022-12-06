import argparse
import os
import sys
import zipfile
from utils.manifest import Manifest
import utils.api
import subprocess
import shutil

# os.chdir(os.path.dirname(sys.argv[0]))

#i stole this from sunst0rm uwu (maybe)
def dependencies():
    if not os.path.exists('/usr/local/bin/futurerestore'):
        print('[!] futurerestore not found, please install it')
        sys.exit(1)

    if not os.path.exists('/usr/local/bin/img4tool'):
        print('[!] img4tool not found, please install it')
        sys.exit(1)

    if not os.path.exists('/usr/local/bin/img4'):
        print('[!] img4 not found, please install it')
        sys.exit(1)

    if not os.path.exists('/usr/local/bin/Kernel64Patcher'):
        print('[!] Kernel64Patcher not found, please install it')
        sys.exit(1)

    if not os.path.exists('/usr/local/bin/iBoot64Patcher'):
        print('[!] iBoot64Patcher not found, please install it')
        sys.exit(1)

    if not os.path.exists('/usr/local/bin/ldid'):
        print('[!] ldid not found, please install it')
        sys.exit(1)

    if not os.path.exists('/usr/local/bin/asr64_patcher'):
        print('[!] asr64_patcher not found, please install it')
        sys.exit(1)

    if not os.path.exists('/usr/local/bin/restored_external64_patcher'):
        print('[!] restored_external64_patcher not found, please install it')
        sys.exit(1)

