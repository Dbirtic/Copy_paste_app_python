import os
import sys
import re
import shutil
from pathlib import Path

# Define REGEX
SOUND_FILE = re.compile(r'(.*(mp3|m4a|wav))')
SONG = re.compile(r'(?!\d+)(?!(-|\s-\s)).*')

def search_folder(destination):
    main_root = "E:\Glazba"
    songs, artists = parse_song_list("P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
    music_list = []
    if os.path.isdir(main_root):
        for root, dirs, files in os.walk("E:\Glazba"):
            for dir in dirs:
                if dir in artists:
                    # make temporary path for the artist
                    temp_path = Path(main_root + "/" + dir).as_posix()
                    print(temp_path)
                    for root2, dirs2, files2 in os.walk(temp_path):
                        # go into artist folder and find songs
                        for file in files2:
                            temp = SONG.search(file)
                            # parse the song name with extension
                            temp2 = temp.group(0)
                            # need to remove the whitespace at the end
                            temp2 = temp2.strip()
                            #print(f'temp2: {temp2}')
                            if temp := SOUND_FILE.search(file):
                                music_list.append(temp.group(1))
                                temp_path = Path(main_root + "/" + temp.group(1)).as_posix()
                                #print(f'temp path: {temp_path}')
                                if file in temp_path:
                                    shutil.copy(temp_path, destination)
            #print(f'root: {root}\ndir: {dirs}\nfile: {files}')
            print(f'list of songs: {music_list}')

# TODO:
# napraviti popis_pjesama.txt +

# napraviti parser funkciju i spreminiti i vratiti popis pjesama i izvođača +
def parse_song_list(song_path):
    song_list = []
    artist_list = []
    with open(song_path, 'r') as songs:
        for line in songs:
            # parse song names
            song = line.split(' - ')
            song_list.append(song[1])

            # parse artist names but take newline out of it
            temp_art = song[2].split('\n')
            artist_list.append(temp_art[0])
    return song_list, artist_list

# u search_folder napraviti izmjenu da se traže pjesme iz liste i spremaju se putanje za kopiranje
# napraviti rename funckiju koja će na temelju liste preimenovati nazive pjesama


#search_folder("E:\Glazba\Audioslave\(2002) Audioslave","Like A Stone", "F:\\test_folder_py")
search_folder("F:\\test_folder_py")
