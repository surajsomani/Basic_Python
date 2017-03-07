#system output and intput from cmd or shell


import sys
sys.stderr.write('This is stderr text\n') #prints the text in red color
sys.stderr.flush() 
sys.stdout.write('This is stdout text\n')
