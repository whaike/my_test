import os
#print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#print os.path.dirname(os.path.realpath(__file__))
localpath = os.path.dirname(os.path.realpath(__file__))

filename = os.path.join(localpath,'hello.log')

with open(filename,'ab') as f:
    for i in range(10):
        f.write(str(i)+os.linesep)

