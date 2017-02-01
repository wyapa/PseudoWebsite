#!/usr/bin/python

import token
import translate
import sys
import re

def main(args):
  args = args.split()
  if len(args) > 2:
    print "pseudo: " + " ".join(args) + ". Too many arguments. Usage: pseudo file"
    exit()
  elif len(args) < 2:
    print "pseudo: Too few arguments. Usage: pseudo file"
    exit()

  filename = args[1]
  if re.match(r'(.*)\.psu$', filename) == None:
    print "pseudo: Not a '.psu' file. Usage: pseudo file"
    exit()

  f = open(filename, 'r')
  tokens = token.tokenize(f)
  translation = translate.parse(tokens)
  f.close()
  code = open(filename[:-4] + '.py', 'w+')
  code.write(translation)
  code.close()
  exec(translation)
  print "Code has been run and has been translated into " + filename[:-4] + ".py"

if __name__ == "__main__":
  main()
