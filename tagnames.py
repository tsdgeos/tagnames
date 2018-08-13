import sys
import subprocess

names = sys.stdin.read().split('\n')
currentNumber = 1

page = 10
blank = [ "____________________", "", "____________________" ]

def replaceName(ff, number, val):
    global currentNumber
    nombre = "%s - %s" % (val[0], str(currentNumber))
    ff=ff.replace('nombre'+number, nombre, 1)
    ff=ff.replace('organizacion'+number, "Beer, Wine, non alcoholic", 1)
    currentNumber = currentNumber + 1
    return ff

for i in range(0,len(names)//page+1):
    idx = i * page

    f = open('akademy_ticket.svg')
    ff = f.read()
    if idx<len(names):
        ff = replaceName(ff, "1", names[idx].split('|'))
    else:
        ff = replaceName(ff, "1", blank)
    if idx+1<len(names) and names[idx+1] != "":
        ff = replaceName(ff, "2", names[idx+1].split('|'))
    else:
        ff = replaceName(ff, "2", blank)
    if idx+2<len(names) and names[idx+2] != "":
        ff = replaceName(ff, "3", names[idx+2].split('|'))
    else:
        ff = replaceName(ff, "3", blank)
    if idx+3<len(names) and names[idx+3] != "":
        ff = replaceName(ff, "4", names[idx+3].split('|'))
    else:
        ff = replaceName(ff, "4", blank)
    if idx+4<len(names) and names[idx+4] != "":
        ff = replaceName(ff, "5", names[idx+4].split('|'))
    else:
        ff = replaceName(ff, "5", blank)
    if idx+5<len(names) and names[idx+5] != "":
        ff = replaceName(ff, "6", names[idx+5].split('|'))
    else:
        ff = replaceName(ff, "6", blank)
    if idx+6<len(names) and names[idx+6] != "":
        ff = replaceName(ff, "7", names[idx+6].split('|'))
    else:
        ff = replaceName(ff, "7", blank)
    if idx+7<len(names) and names[idx+7] != "":
        ff = replaceName(ff, "8", names[idx+7].split('|'))
    else:
        ff = replaceName(ff, "8", blank)
    if idx+8<len(names) and names[idx+8] != "":
        ff = replaceName(ff, "9", names[idx+8].split('|'))
    else:
        ff = replaceName(ff, "9", blank)
    if idx+9<len(names) and names[idx+9] != "":
        ff = replaceName(ff, "10", names[idx+9].split('|'))
    else:
        ff = replaceName(ff, "10", blank)
    print('--')

    outputpath = 'akaes/tags%d.svg' % i
    towrite=open(outputpath, 'w')
    towrite.write(ff)
    towrite.close()

    subprocess.call(["inkscape", outputpath, "--export-pdf=akaes/tags%d.pdf" % i])

