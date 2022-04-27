import os
import sys
import re
import shutil
from pathlib import Path

# Define REGEX
SOUND_FILE = re.compile(r'(.*(mp3|m4a|wav))')

def search_folder(folder_path, destination):
    music_list = []
    if os.path.isdir(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if temp := SOUND_FILE.search(file):
                    music_list.append(temp.group(1))
                    temp_path = Path(folder_path + "/" + temp.group(1)).as_posix()
                    print(f'temp path: {temp_path}')
                    if "Like A Stone" in temp_path:
                        shutil.copy(temp_path, destination)
            #print(f'root: {root}\ndir: {dirs}\nfile: {files}')
            print(f'list of songs: {music_list}')


search_folder("E:\Glazba\Audioslave\(2002) Audioslave", "F:\\test_folder_py")
