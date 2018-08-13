import sys
import subprocess

ticket_line1 = "Drink ticket"
ticket_line2 = "Beer, Wine, non alcoholic"
names = [ ticket_line1, ticket_line2 ]

number_of_pages = 3
tickets_per_page = 10

currentNumber = 1

all_output_paths = [ ]

def replaceName(ff, number, val):
    global currentNumber
    nombre = "%s - %s" % (val[0], str(currentNumber))
    ff=ff.replace('nombre'+number, nombre, 1)
    ff=ff.replace('organizacion'+number, val[1], 1)
    currentNumber = currentNumber + 1
    return ff

for i in range(0, number_of_pages):
    idx = i * tickets_per_page

    f = open('akademy_ticket.svg')
    ff = f.read()
    ff = replaceName(ff, "1", names)
    ff = replaceName(ff, "2", names)
    ff = replaceName(ff, "3", names)
    ff = replaceName(ff, "4", names)
    ff = replaceName(ff, "5", names)
    ff = replaceName(ff, "6", names)
    ff = replaceName(ff, "7", names)
    ff = replaceName(ff, "8", names)
    ff = replaceName(ff, "9", names)
    ff = replaceName(ff, "10", names)
    print('--')

    outputpath = 'output/tickets%d.svg' % i
    towrite=open(outputpath, 'w')
    towrite.write(ff)
    towrite.close()

    subprocess.call(["inkscape", outputpath, "--export-pdf=output/tickets%d.pdf" % i])
    all_output_paths.append("output/tickets%d.pdf" % i)

pdfunite_call_args = all_output_paths
pdfunite_call_args.insert(0, "pdfunite")
pdfunite_call_args.append("output/all_tickets.pdf")
subprocess.call(pdfunite_call_args)
