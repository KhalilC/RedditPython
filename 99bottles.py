#Objectives are to print each line of the song without using numbers in the lyrics.
#Include a blank line between each lyric.

for i in range(100,0,-1):
    if i == 1:
        print "%i bottle of beer on the wall, %i bottle of beer\n" % (i,i)
        print "Take one down, pass it all around.  No more bottles of beer on the wall\n"
    else:            
        print "%i bottles of beer on the wall, %i bottles of beer\n" % (i,i)
        print "Take one down.  Pass it all around. %i bottles of bear on the wall.\n" % (i-1)