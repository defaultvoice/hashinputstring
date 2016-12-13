import hashlib
import codecs
import sys


def main():
    try:
        with open('hashed.txt', 'w') as outfile, codecs.open(sys.argv[1], 'r', encoding='utf-8') as infile:
            for line in infile:
                md = hashlib.md5()
                md.update(line.encode('utf-8'))
                line = md.hexdigest() + '\n'
                outfile.write(line)
    except IndexError:
        print 'Expected an input file'

if __name__ == '__main__':
    main()
