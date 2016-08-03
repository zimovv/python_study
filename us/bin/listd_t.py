
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
    file_list = os.listdir(folder)
    print("Directory of " + folder)

    def file_info(file):
        f = folder + '\\' + file
        created_time = os.stat(f).st_ctime
        data = date_string(created_time)
        time = time_string(created_time)
        if os.path.isdir(f):
            return data + ' ' + time + '\t' + r"<DIR>" + '\t\t' + file
        else:
            size = os.stat(f).st_size
            return data + ' ' + time + '\t\t' + str(size) + '\t' + file

    files_infos = map(file_info, file_list)
    for file_infos in files_infos:
        print(file_infos)

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: listd dir")
        sys.exit(1)
        
    main(sys.argv[1])

# Firstly, cd to the folder of listd_t.py.
# Then excute "python listd_t.py <path>" in CMD.
