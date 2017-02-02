#!/usr/bin/python
from __future__ import absolute_import
import translate
import sys
import re
import os
sys.path.append('./')
import tokenpseudo as tk
def main():
  if len(sys.argv) > 2:
    print "pseudo: " + " ".join(sys.argv) + ". Too many arguments. Usage: pseudo file"
    exit()
  elif len(sys.argv) < 2:
    print "pseudo: Too few arguments. Usage: pseudo file"
    exit()

  filename = sys.argv[1]
  if re.match(r'(.*)\.psu$', filename) == None:
    print "pseudo: Not a '.psu' file. Usage: pseudo file"
    exit()
  f = open(filename, 'r')
  tokens = tk.tokenize(f)
  translation = translate.parse(tokens)
  f.close()
  code = open(filename[:-4] + '.py', 'w+')
  code.write(translation)
  code.close()
  print "PYTHON CODE:"
  print "\n"
  print translation
  print "_____________________________________________________________________"
  print "PROGRAM OUTPUT:"
  print "\n"
  exec(translation)
  print "_____________________________________________________________________"
  print "Code has been run and has successfully translated into " + filename[:-4] + ".py"

if __name__ == "__main__":
  main()