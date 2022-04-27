import os
import sys
import re
import shutil
from pathlib import Path

# Define REGEX
SOUND_FILE = re.compile(r'(.*(mp3|m4a|wav))')
SONG_NAME = re.compile(r'')
BAND_NAME = re.compile(r'')

def search_folder(folder_path, song_name, destination):
    music_list = []
    if os.path.isdir(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if temp := SOUND_FILE.search(file):
                    music_list.append(temp.group(1))
                    temp_path = Path(folder_path + "/" + temp.group(1)).as_posix()
                    #print(f'temp path: {temp_path}')
                    if song_name in temp_path:
                        shutil.copy(temp_path, destination)
            #print(f'root: {root}\ndir: {dirs}\nfile: {files}')
            print(f'list of songs: {music_list}')

# TODO:
# napraviti popis_pjesama.txt +

def parse_song_list(song_path):
    song_list = []
    artist_list = []
    with open(song_path, 'r') as songs:
        for line in songs:
            song = line.split(' - ')
            song_list.append(song[1])
            temp_art = song[2].split('\n')
            artist_list.append(temp_art[0])
            #print(f'{song}')
            #print(f'{song[1]}')
            #print(f'{song[2]}')
    #print(f'song list: {song_list}\nartist list: {artist_list}')
    return song_list, artist_list
# napraviti parser funkciju i spreminiti i vratiti popis pjesama
# u search_folder napraviti izmjenu da se traže pjesme iz liste i spremaju se putanje za kopiranje
# napraviti rename funckiju koja će na temelju liste preimenovati nazive pjesama


#search_folder("E:\Glazba\Audioslave\(2002) Audioslave","Like A Stone", "F:\\test_folder_py")
parse_song_list("P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")