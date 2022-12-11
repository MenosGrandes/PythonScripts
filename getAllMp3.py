import os
import ffmpeg
import random
import os
import sys
import subprocess
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
import time
import datetime
allMusic = []
dir = "CONVERTED"
extensions = ('.mp3','.flac','.wav')
for path, subdirs, files in os.walk("."):
    if subdirs!=dir:
        for name in files:
            if name.endswith(extensions):
                allMusic.append(os.path.join(path, name))
try:
    os.mkdir(dir)
except OSError as error:
    print(error)

cummulative_size = 0
MAX_SIZE_GB = 3.5
MP3_COUNT = 50

def convertMp3(concreteName):
    #element = random.choice(allMusic)
    #allMusic.remove(element)
    print(f"STARTING {concreteName}")

    (
        ffmpeg
        .input(element)
        #.output('out.mp3', **{'b:a': '192k'}, ac=2, ar=44100)
        .output(concreteName, **{'codec:a':'libmp3lame'}, **{'qscale:a' : 5}, loglevel='quiet', hide_banner='-y')
        .run()
    )
    print(f"FINISHED {concreteName}")

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


with ThreadPool(cpu_count())as p:
    while(True):
        allElems = []
        for _ in range(cpu_count()):
           element = random.choice(allMusic)
           allMusic.remove(element)
           name = os.path.splitext(element)[0].split('/')[-1] + '.mp3'
           concreteName = os.path.join(dir,name)
           allElems.append(concreteName)
            
        JOBS = p.map(convertMp3, allElems)
        print(f"GET SIZE OF {dir}")
        size_GB = get_size(dir)/ (1024 * 1024 * 1024)
        print(f"{size_GB}")

        if size_GB > MAX_SIZE_GB:
            break

print("END")
        
