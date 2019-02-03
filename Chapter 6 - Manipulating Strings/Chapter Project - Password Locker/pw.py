#! python 3

# pw.py - An insecure password locker program.
import sys
import pyperclip

passwords = {'email': 'email password', 'blog': 'blog password', 'luggage': 'luggage password'}

if len(sys.argv) < 2:   # If no input. argv automatically has program name as first index ([0]).
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()  # Exits loop once argument received.

account = sys.argv[1]   # account = first argument passed to cmd line

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no password for ' + account)
