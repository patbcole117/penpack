import urllib.parse
from argparse import ArgumentParser

def main():

    ap = ArgumentParser()
    ap.add_argument('instring')
    ap.add_argument('-t', '--type')
    ap.add_argument('-d', '--decode', action="store_true")
    args = ap.parse_args()

    print(f"DEBUG: {args}")

    if args.type.upper() == 'URL':
        print(url_format(args.instring, args.decode))

def url_format(instring, d):

    if d:
        print('DECODING URL....')
        return urllib.parse.unquote(instring)
    else:
        print('ENCODING URL....')
        instring = urllib.parse.quote(instring, safe='')
        instring = instring.replace('.', '%2E')
        instring = instring.replace('-','%2D')
        return instring
    
if __name__ == '__main__':
    main()