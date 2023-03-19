#!/usr/bin/python3
import base64
import urllib.parse
from argparse import ArgumentParser

def main():

    ap = ArgumentParser()
    ap.add_argument('instring')
    ap.add_argument('-t', '--type')
    ap.add_argument('-d', '--decode', action="store_true")
    args = ap.parse_args()

    print(f"DEBUG: {args}")

    try:
        f = open(args.instring, 'r')
        instring = f.read()
    except:
        instring = args.instring

    if args.type.upper() == 'URL':
        print(url_format(instring, args.decode))

    elif args.type.upper() == 'B64':
        print(b64_format(instring, args.decode))

def url_format(instring, d):

    if d:
        print('DECODING URL....')
        outstring = urllib.parse.unquote(instring)
        return outstring
    else:
        print('ENCODING URL....')
        outstring = urllib.parse.quote(instring, safe='')
        outstring = outstring.replace('.', '%2E')
        outstring = outstring.replace('-','%2D')
        return outstring

def b64_format(instring, d):

    instring_bytes = instring.encode('ascii')

    if d:
        print('DECODING B64....')
        outstring_bytes = base64.b64decode(instring_bytes)
        outstring = outstring_bytes.decode('ascii')
        return outstring
    else:
        print('ENCODING B64....')
        outstring_bytes = base64.b64encode(instring_bytes)
        outstring = outstring_bytes.decode('ascii')
        return outstring

if __name__ == '__main__':
    main()