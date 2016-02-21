#! /usr/bin/python

import os
import itertools

# Settings for brute force search
INFILE = 'encrypted'
OUTFILE = 'decrypted.txt';
PREFIXES = [ '', 'passphrase' ]
WORDS = [ 'correct', 'horse', 'battery', 'staple', 'xkcd' ]
SEPARATORS = [ '', ' ' ]
DEPTH = 4

# Perform permutations until this word depth
for i in xrange(DEPTH):
  print "DEPTH", i + 1
  # Loop all given prefixes
  for w in PREFIXES:
    # Create all combinations of words including repetitions
    for x in (itertools.product(WORDS, repeat=i + 1)):
      # Create all combinations of separators including repetitions
      for y in (itertools.product(SEPARATORS, repeat=i)):
        # Build passphrase with words and separators
        passphrase = w
        for z in itertools.izip_longest(x, y, fillvalue=''):
          passphrase += z[0] + z[1]
        # Bruteforce decryption
        print passphrase
        status = os.system('echo "%s" | gpg --passphrase-fd 0 --no-tty --output %s --decrypt %s 2>/dev/null' % (passphrase, OUTFILE, INFILE));
        if status == 0:
          print "SUCCESS! Passphrase:", passphrase
          exit()
#FAIL
print "DONE, no results..."

