#!/usr/bin/env python
# encoding: utf-8
"""
spark.py
~~~~~~~~

A port of @holman's spark project for Python.
"""

import sys

#ticks = (u'▁', u'▂', u'▃', u'▅', u'▆', u'▇')
ticks = (u'▁', u'▂', u'▃',u'▄', u'▅',u'▆',u'▇')

def main(argv=None):

    """Main entry point"""
    if argv is None:
        argv = sys.argv

    # clip of 'python' from argv if its there
    if argv[0].find('ython') != -1:
        del argv[0]
   
    # handles interactive vs. piped input 
    args = ''
    if sys.stdin.isatty():
        args = argv[1]
    else:
        args = sys.stdin.read()
    #print args
    
    spark_print(args)

def spark_string(ints):
    global ticks

    """Returns a spark string from given iterable of ints."""
    step = ((max(ints) - min(ints)) / (len(ticks) - 1))
    if step == 0:
        step = 1
    return u' '.join([ticks[(i/step)] for i in ints])


def spark_print(ints, stream=None):
    """Prints spark to given stream."""
    if stream is None:
        stream = sys.stdout

    # ensure no trailing ','
    ints = ints.rstrip(',') 
    # parse strings to ints
    list2 = [int(x) for x in ints.split(',')]
    stream.write(spark_string(list2).encode('utf-8', 'replace'))
    print ''

if __name__ == "__main__":
        sys.exit(main())
