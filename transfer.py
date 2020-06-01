import os
import shutil
import subprocess
import logging

logging.basicConfig(filename='/tmp/logtransfer.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logging.info("Transfer Started")
#Directory Exclusions (whole)
exclusion = ['test1','test2', 'test3']
#Directory wildcard exclusion (example test1, test2, test3 = wildcard(test))
wildcard = "test"
#src path
root_src_dir = os.path.join('.','/src_path')
#dst path
root_target_dir = os.path.join('.','/src_path')
for src_dir, dirs, files in os.walk(root_src_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclusion]
        dst_dir = src_dir.replace(root_src_dir, root_target_dir)
        if not os.path.exists(dst_dir):
                if wildcard not in src_dir:
                        try:
                                os.mkdir(dst_dir)
                                subprocess.call(["chmod","--reference",src_dir,dst_dir])
                                subprocess.call(["chown","--reference",src_dir,dst_dir])
                        except:
                                logging.error("Cant create directory for"+dst_dir, exc_info=True)
                                print "!!!!!!!!!!!!!!!!!!!Can't create directory for"+dst_dir
        for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file) and os.stat(dst_file).st_size == os.stat(src_file).st_size:
                        print "Already exist: "+dst_file
                        logging.info("Already exist: "+dst_file)
                elif not os.path.exists(dst_file) or not os.stat(dst_file).st_size == os.stat(src_file).st_size:
                        if wildcard not in src_dir:
                                try:
                                        print dst_file
                                        #shutil.copy2(src_file, dst_dir)
                                        process = subprocess.Popen(['cp','-p',src_file,dst_dir])
                                        process.wait()
                                        print "Copied: "+src_file+" "+dst_dir
                                        logging.info("Copied: "+src_file+" "+dst_dir)
                                except:
                                        logging.error("Cant copy"+src_file+" "+dst_dir, exc_info=True)
                                        print"!!!!!!!!!!!!!!!!Cant copy"+src_file+" "+dst_dir
                                        if os.path.exists(dst_file):
                                                os.remove(dst_file)
                                                print"Remove unfinished file "+dst_file
                                        exit(1)
