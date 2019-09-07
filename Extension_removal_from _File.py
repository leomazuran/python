#Author: Leonardo Mazuran

import os
extension_list = []
import string
drive_chooses = []
import glob
from ctypes import windll
import logging
logging.basicConfig(filename='logfile.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

    print ('Current Drives Installed:')
    print (get_drives())
    logger.info("Drive Letters find in Device"+str(get_drives()))



extension = []
ext = ''
def find_note(drive_letter_get):
    for drive_letter in drive_letter_get:

        print ("Scanning for Ransomware Note in the "+ drive_letter +" drive.")
        for root, dirs, files in os.walk(drive_letter+':\\', topdown=True):
            for file in files:
                if file.endswith("-readme.txt"):

                    file_catch =  str(os.path.join(root, file))

                    f1 =open(file_catch, 'r')
                    first_line = f1.readline()
                    f1.close()
                    #print (first_line)
                    sub_index = first_line.find('W')
                   # print (sub_index)
                    if sub_index == 14:

                        #print ('yes')
                        if file[:-11].isalnum():
                            if file[:-11] not in extension:
                                extension.append(file[:-11])

                                print ("New extension added "+file[:-11]+".")
                                logger.info("added "+str(file[:-11])+" to extension list")
                                try:
                                    print ("remove readme file")
                                   # print(file_catch)
                                    os.remove(file_catch)
                                except (PermissionError, OSError) as err:
                                    logger.error(err)
                            else:
                                try:
                                    print ("remove extra readme file")
                                   # print (file_catch)
                                    os.remove(file_catch)
                                except (PermissionError, OSError) as err:
                                    logger.error(err)

    print("Extension added:")
    print(extension)
    print("Searching and removing Listed Extensions")
    return extension


def remove(drive_letter_get2, extension2):
    count = 0
    err_count = 0
    for drive_letter_proc in drive_letter_get2:
        print ("Search and remove in " + drive_letter_proc + " drive.")

        for name in glob.glob(drive_letter_proc+":\\**\\*.*", recursive=True):
            for extension_fill in extension2:
                if name.endswith("."+extension_fill):
                    print (os.path.splitext(name))
                    base = os.path.splitext(name)[0]
                    print (base)
                    try:
                        os.rename(name, base)
                        count +=1
                    except (PermissionError, OSError) as err:
                        logger.error(err)
                        err_count+=1
    # for drive_letter_proc in get_drives():
    #     print ("Search and remove any missing files Folders for " + drive_letter_proc + " drive.")
    #
    #     for root, dirs, files in os.walk(drive_letter + ':\\', topdown=True):
    #         for file in files:
    #             for extension_fill in extension:
    #
    #                 if file.endswith("."+extension_fill):
    #                     print (os.path.splitext(file))
    #                     base = os.path.splitext(file)[0]
    #
    #                     try:
    #                         os.rename(root, base)
    #                         count +=1
    #                     except (PermissionError, OSError) as err:
    #                         logger.error(err)
    #                         err_count+=1
    print ("Successfully Remove Extensions with "+str(count)+" success and "+str(err_count)+" fails" )

while True:
    print ('\n\n\n')
    drive_choose = input("Would you like to AutoRun ['y', 'n', 'q']?")
    dl = drive_choose[0].lower()
    if drive_choose == '' or not dl in ['y', 'n', 'q']:
        print('Please answer with yes or no!')

    if dl == 'y':
        drive_choose = get_drives()
        find_note(drive_choose)
        extension_list = find_note(drive_choose)
        remove(drive_choose,extension_list)

        break
    if dl == 'q':
        break
    if dl == 'n':
        while True:
            drive_letter1 = list(input("Input Drive letter list. ex. CDE = C:, D:, E:"))
            print (drive_letter1)
            drive_choose = drive_letter1

            n_extension = int(input("Enter number of different extensions (1, 2 , 3, 4, 5) : "))
            extension_input = list(( input("\nEnter the extension name. (example: xy65rde ztg654) No periods in the begining.: ").strip().split()))[:n_extension]

            print (extension_input)

            for drive_letter_proc in drive_choose:

                print("Search and remove ransomware notes in the "+ drive_letter_proc + " drive.")

                for name in glob.glob(drive_letter_proc + ":\\**\\*.*", recursive=True):
                    for extension_fill in extension_input:
                        if name.endswith(extension_fill+"-readme.txt"):
                            try:
                                os.remove(name)

                            except (PermissionError, OSError) as err:
                                logger.error(err)
                remove(drive_choose, extension_input)
            break


    else:
        print ("Error, Try again")
