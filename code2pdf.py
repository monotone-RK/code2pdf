#!/usr/bin/env python
# -*- coding: utf-8 -*-
#***************************************************************************************/
# Code to PDF Written in Python             Ver:1.0 Last updated 2013.01.07  monotone-RK/
#***************************************************************************************/
import sys
import os
import datetime
import commands
from optparse import OptionParser

DEFAULT = "code" # Default PDF name
current_str = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def showUsage():
    print "## Code to PDF Written in Python"
    print "## Date:2013.03.18"
    print "## Usage: python code2pdf.py [options] src_code0 src_code1 ...\n"
    print """Options:
  -h, --help     show this help message and exit
  -v, --version  Show the version
  -o             specify output file name (default:code.pdf)"""

def showVersion():
    print "Code to PDF Written in Python v1.1.1  last upated:2013.03.18"

def code2pdf():
    print "The number of codes: %d" % len(codelist)
    print "\ncodelist:"
    print "----------------------------------------"
    for src in codelist:
        print "%s" % src
        commands.getoutput("env LC_ALL=ja._JP.EUCJP a2ps -A fill --medium=a4 -f 6.5 --line-numbers=1 -o %s.ps %s" % (src, src))
        commands.getoutput("cat %s.ps >> merge.ps" % src)
        commands.getoutput("rm %s.ps" % src)
    commands.getoutput("ps2pdf14 -sPAPERSIZE=a4 merge.ps %s.pdf" % (pdf_name))
    commands.getoutput("rm merge.ps")
    print "----------------------------------------"
    print "\n## output pdf file successfully!" 
    print "## PDF NAME: %s.pdf" % pdf_name
    print "## Date:",current_str

optparser = OptionParser() 
optparser.add_option("-v","--version",action="store_true",dest="showversion",
                     default=False,help="Show the version")
optparser.add_option("-o",action="store_true",dest="output",
                     default=False,help="specify output file name (default:code.pdf)")
(options, args) = optparser.parse_args()

if options.showversion:
    showVersion()
    sys.exit()

if len(args) == 0:
    showUsage()
    sys.exit()

if options.output:
    pdf_name = args[0]
    del args[0]
    codelist = args
    if len(codelist) == 0: 
        print "## Error! No source code exists!"
        sys.exit()
else:
    pdf_name = DEFAULT
    codelist = args

for src in codelist:
    if not os.path.isfile(src):
        print "## Error! No such file: " + src
        print "## Usage: python code2pdf.py [options] src_code0 src_code1 ..."
        sys.exit()

if __name__ == "__main__":
    code2pdf()
