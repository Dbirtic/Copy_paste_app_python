import os
from pkgutil import extend_path
import sys
import re
import shutil
from pathlib import Path

# Define REGEX
SOUND_FILE = re.compile(r'(.*(mp3|m4a|wav))')
SONG = re.compile(r'(?!\d+)(?!(-|\s-\s)).*')

def search_folder(destination):
    main_root = "E:\Glazba"
    songs, artists, albums = parse_song_list("P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
    songs_list = songs_lower(songs)
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
                        
                            if "alice_in_chains-" in temp2:
                                temp3 = temp2.removeprefix("alice_in_chains-")
                                if "-h8me" in temp3:
                                    temp4 = temp3.split("-h8me")
                                    temp5 = temp4[0] + temp4[1]
                                    temp5 = temp5.split("_")
                                    temp6 = ' '.join(temp5)
                                    if temp7 := SOUND_FILE.search(temp6):
                                        # finally parse the song name and remove .mp3
                                        temp8 = temp7.group(0)
                                        temp8 = temp8.removesuffix('.mp3')
                                        if temp8 in songs_list:
                                            # add song to the list, create a path and copy to destination
                                            
                                            temp_path2 = Path(root2 + "/" + file).as_posix()
                                            path_to_song = check_ablum_in_path(albums, temp_path2)

                                            if path_to_song == None:
                                                continue
                                            else:
                                                shutil.copy(path_to_song, destination)
                                                song_name = temp8
                                                rename_songs(file, song_name, destination, "P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
                            elif temp2 := SOUND_FILE.search(file):
                                #print(f'temp2: {temp2.group(0)}')
                                temp3 = temp2.group(0)
                                if temp3.startswith("0") or temp3.startswith("1"):
                                    temp4 = temp3[2:].strip()
                                    print(f'temp4: {temp4}')
                                    if temp4.startswith(".") or temp4.startswith("- "):
                                        pass
                                        # continue tomorrow
                                if temp4.startswith("- "):
                                    temp5 = temp4[1:].strip()
                                    #print(f'temp5: {temp5}')
                                    temp6 = temp5.removesuffix(".mp3")
                                    if temp6 in songs_list:
                                        temp_path2 = Path(root2 + "/" + file).as_posix()
                                        path_to_song = check_ablum_in_path(albums, temp_path2)

                                        if path_to_song == None:
                                            continue
                                        else:
                                            shutil.copy(path_to_song, destination)
                                            song_name = temp6
                                            rename_songs(file, song_name, destination, "P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")

# TODO:
# napraviti popis_pjesama.txt +

# napraviti parser funkciju i spreminiti i vratiti popis pjesama i izvođača +
def parse_song_list(song_path):
    song_list = []
    artist_list = []
    album_list = []
    with open(song_path, 'r') as songs:
        for line in songs:
            song = line.split(' - ')
            
            # parse song names
            song_list.append(song[1])

            # parse artist names but take newline out of it
            artist_list.append(song[2])

            # parse album names
            temp_alb = song[3].split('\n')
            album_list.append(temp_alb[0])
    return song_list, artist_list, album_list

def songs_lower(songs):
    songs_list = []
    for i in songs:
        songs_list.append(i.lower())
    return songs_list

def check_ablum_in_path(albums, path):
    for album in albums:
        if "Ã¦nima" in album:
            album = "ænima"
        if album in path:
            return path
        else:
            pass
    
def rename_songs(old_name, song_name, destination, song_path):
    with open(song_path, 'r') as songs:
        for line in songs:
            if song_name in line.lower():
                new_name = line.removesuffix("\n")
                os.rename(destination + '\\' + old_name, destination + '\\' + new_name + ".mp3")
            else:
                continue

# u search_folder napraviti izmjenu da se traže pjesme iz liste i spremaju se putanje za kopiranje
# napraviti rename funkciju koja će na temelju liste preimenovati nazive pjesama


#search_folder("E:\Glazba\Audioslave\(2002) Audioslave","Like A Stone", "F:\\test_folder_py")
search_folder("F:\\test_folder_py")
#a, b, c, d = parse_song_list("P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
#print(f'song: {a}\nartist: {b}\nalbum: {c}\nnumbers: {d}')

#print(rename_songs([1, 22, 44, 5, 77, 101], "osha", "E:Glazba/"))