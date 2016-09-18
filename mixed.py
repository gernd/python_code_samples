# command line arguments can be handled via sys.argv
import sys

print("The following arguments where given:")

# as in c, the first argument contains the filename 
for arg in sys.argv:
    print arg
