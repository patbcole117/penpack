import sys

charSet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ-abcdefghijklmnopqrstuvwxyz-123456789'.split('-')

def bytesToString(byteString):
    bs = byteString.replace('0x','')
    
    i = 0
    j = 1
    pat  = ''
    while j < len(bs):
        c = bs[i] + bs[j]
        pat += chr(int(c, 16))
        i+=2
        j+=2
    print(pat[::-1])
    return pat[::-1]

def generatePattern(size=1024):
    pattern = ''
    subPattern = ''

    for x in charSet[0]:
        subPattern += x
        for y in charSet[1]:
            subPattern += y
            for z in charSet[2]:
                subPattern += z
                pattern += subPattern
                subPattern = subPattern[:2]
            subPattern = subPattern[:1]
        subPattern = ''

    return pattern[:int(size)]

def findLength(pattern, delimiter):
    splitP = pattern.split(delimiter)
    return len(splitP[0])

if __name__ == '__main__':
    p = generatePattern(sys.argv[1])
    print(p)

    i = input('Enter delimiter: ')
    if '0x' in i:
        i = bytesToString(i)

    blen = findLength(p, i)
    print(blen)

