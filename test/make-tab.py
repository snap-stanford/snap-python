#
#   convert input to TSV format, remove final '.'
#

import sys

if __name__ == '__main__':

    for nline in sys.stdin:
        line = nline.splitlines()[0]

        line = line.replace("> <", ">\t<")
        line = line.replace("> \"", ">\t\"")

        if line[-2:] == " .":
            line = line[:-2]

        print(line)
