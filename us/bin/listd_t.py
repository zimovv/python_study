
import os
import sys
import stat
#import pwd
#import grp
import datetime



def date_string(created_time):
    d    = datetime.datetime.fromtimestamp(created_time)
    return d.strftime("%b %d")

def time_string(created_time):
    d    = datetime.datetime.fromtimestamp(created_time)
    return d.strftime("%H:%M")


#TODO: please implement it
def main(folder):

    pass

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: listd dir")
        sys.exit(1)
        
    main(sys.argv[1])

    
