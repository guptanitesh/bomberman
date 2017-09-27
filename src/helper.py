"""
    NOTE: In order to take single character input, this module
    is copied from internet with some minor changes in it for
    unbuffering. I could simply write in requirements.txt to
    install getch but is not compatible on all systems and it
    was a better way, hence I used it as a helper module.
"""
from board import gameArr


class _Getch:

    # Gets a single character from standard input.
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty
        import sys
        from select import select

    def __call__(self):
        import sys
        import tty
        import termios
        from select import select

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            [i, o, e] = select([sys.stdin.fileno()], [], [],
                               abs((5 - gameArr.level) / 4))
            if(i):
                ch = sys.stdin.read(1)
                # If a character is given as input return it immidiately
            else:
                ch = None

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    # Check if a character is waiting, otherwise this will block
    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
