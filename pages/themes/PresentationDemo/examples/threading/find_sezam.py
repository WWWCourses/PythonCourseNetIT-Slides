import os
import threading
import time

def count_sezam(files):
  for file in files:
    global sezam_count
    time.sleep(0.2)
    with open(path+file) as fh:
      file_text = fh.read()

    if "sezam" in file_text:
      sezam_count += 1

    threadID = threading.currentThread().name;
    print("Processing {} by {}".format(file, threadID))


def single_thred():
  count_sezam(files)
  print("sezam in files: {}".format(sezam_count))

def multithreaded(tc):
  # split list into parts:
  parts = len(files)/tc
  start = 0.0

  while start < len(files):
    files_partion = files[int(start):int(start + parts)]
    start += parts
    # print("files_partion: ",files_partion)

    # start a thread for each part
    tr = threading.Thread(target=count_sezam, args=(files_partion,))
    tr.start()
    tr.join()

  print("sezam in files: {}".format(sezam_count))

path = os.getcwd()+"/test_files/"
files = os.listdir(path);

# single-thread processing:
sezam_count = 0
tsingle = time.time()
single_thred()
print("single-thread time:",time.time() - tsingle,"\n")

# multithreaded processing:
sezam_count = 0
tmulti = time.time()
multithreaded(2)
print("multi-thread time:",time.time() - tmulti)


