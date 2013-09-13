# converts all lowercase i's that should be capitalized to 'I'

errors = 0

def conv_i(line, delimeter):
    global errors
    nline = line.split(delimeter)
    for words in nline:
        if words == 'i':
            nline[nline.index(words)] = 'I'
            errors += 1
    return delimeter.join(nline)

o = open("greeneggs3.txt", "w")
for line in open('greeneggs.txt'):
    new_line = conv_i(line, ' ')
    new_line2 = conv_i(new_line, '-')       
    o.write(new_line2)
          
o.close()
print "There were %i errors corrected in this file." % errors