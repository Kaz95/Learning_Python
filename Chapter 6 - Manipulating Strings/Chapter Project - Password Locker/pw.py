#! python 3
# TODO Make .bat file
# pw.py - An insecure password locker program.
import sys

passwords = {'email': 'email password', 'blog': 'blog password', 'luggage': 'luggage password'}

if len(sys.argv) < 2:   # If no input. argv automatically has program name as first index ([0]).
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()  # Exits loop once argument received.

account = sys.argv[1]
