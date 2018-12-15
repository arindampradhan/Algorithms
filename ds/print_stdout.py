import sys

orig_stdout = sys.stdout
f = file('out.txt', 'w')
sys.stdout = f

# for i in range(2):
#     print 'i = ', i
# basically print any output here 
# it will get printed to a text file out.txt

sys.stdout = orig_stdout
f.close()