import sys

LINUX='linux'
MACOS='darwin'

def linux():
    if sys.platform in LINUX:
        return True
    else:
        return False

IS_MACOS = sys.platform == MACOS
IS_LINUX = linux()

def platform():
    if IS_MACOS:
        return MACOS
    elif IS_LINUX:
        return LINUX
    else:
        return WINDOWS

if __name__=='__main__':
    platform()
