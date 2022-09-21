def main():
    
    codes = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'1', 'c':'2', 'D':'3', 'd':'4', \
             'E':'5', 'e':'6', 'F':'7', 'f':'8', 'G':'0', 'g':'}', 'H':'{', 'h':']', 'I':'[', 'i':'Y', \
             'J':'Z', 'j':'>', 'K':'<', 'k':'/', 'L':'j', 'l':'_', 'M':'"', 'm':'i', 'N':';', \
             'n':'A', 'O':'h', 'o':'-', 'Q':'$', 'q':'V', 'R':'^', 'r':'&', 'S':'^', \
             's':'(','T':')', 't':'~', 'U':'`', 'u':'g', 'V':'==', 'v':'+', 'W':'=', 'w':'!', \
             'X':'f', 'x':'e', 'Y':'d', 'y':'c', 'Z':'b', 'z':'a'}
    encryption(codes)

def encryption(codes):

    fileopen = open('info_security.txt', 'r')
    fileopenreader = fileopen.read()


    encrypted = open('encrypted.txt', 'w')


    for ch in fileopenreader:

        if ch in codes:
            encrypted.write(codes[ch])
        else:
            encrypted.write(ch)

    encrypted.close()

main()