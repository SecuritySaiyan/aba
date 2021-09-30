import sys
import signal

from session import SessionData
from auth import lin, lou, chp
from admin import adu, deu, dal
from nonadmin import adr, der, edr, rer, imd, exd
from misc import hlp

TIMEOUT = 300

def raise_timeout(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, raise_timeout)

def main(argv=None):
    print("Address Book")

    # add logout timeout

    session = SessionData()
    while(True):

        signal.alarm(TIMEOUT)
        try:
            user_input = input(">> ").strip()
        except TimeoutError:
            print("\nSession timeout")
            sys.exit()

        signal.alarm(0)

        command = None
        parameters = None
        try:
            command, parameters = user_input.split(' ', 1)
        except:
            command = user_input

        # Authentication Commands

        if command == "LIN":
            lin(parameters, session)

        elif command == "LOU":
            lou(parameters, session)

        elif command == "CHP":
            chp(parameters, session)

        # Admin-only Commands

        elif command == "ADU":
            adu(parameters, session)

        elif command == "DEU":
            deu(parameters, session)

        elif command == "DAL":
            dal(parameters, session)

        # Non-Admin Commands

        elif command == "ADR":
            adr(parameters, session)

        elif command == "DER":
            der(parameters, session)

        elif command == "EDR":
            edr(parameters, session)

        elif command == "RER":
            rer(parameters, session)

        elif command == "IMD":
            imd(parameters, session)

        elif command == "EXD":
            exd(parameters, session)

        # Misc Commands
        elif command == "HLP":
            hlp(parameters)

        elif command == "EXT":
            print("OK")
            sys.exit()

        else:
            print("Unrecognized command")

if __name__ == "__main__":
    sys.exit(main())
    
