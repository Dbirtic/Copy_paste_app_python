import os
import argparse
from pkgutil import extend_path
import sys
import re
import shutil
from pathlib import Path

# Define REGEX
SOUND_FILE = re.compile(r'(.*(mp3|m4a|wav))')
SONG = re.compile(r'(?!\d+)(?!(-|\s-\s)).*')

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    "--destination", 
    type=str, 
    required=True, 
    help="destination to folder where the songs will be copied"
)
parser.add_argument(
    "-l",
    "--songlist",
    type=str,
    required=True,
    help="path to the song list"
)

def search_folder(destination, song_list):
    '''
    This function takes end folder where the music is stored and list of songs
     to be copied. It parses the song list and copies the songs to the folder
     which was given. After copying it renames the copied files to the names
     given in the song list.
    '''

    main_root = "E:\Glazba"
    songs, artists, albums = parse_song_list(song_list) #"P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt"
    songs_list = songs_lower(songs)
    if os.path.isdir(main_root):
        for root, dirs, files in os.walk("E:\Glazba"): #"E:\Glazba"
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
                                            path_to_song = check_album_in_path(albums, temp_path2)

                                            if path_to_song == None:
                                                continue
                                            else:
                                                shutil.copy(path_to_song, destination)
                                                song_name = temp8
                                                rename_songs(file, song_name, destination, "P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
                            elif temp2 := SOUND_FILE.search(file):
                                temp3 = temp2.group(0)
                                if temp3.startswith("0") or temp3.startswith("1"):
                                    temp4 = temp3[2:].strip()
                                    if temp4.startswith(".") or temp4.startswith("- "):
                                        temp6 = temp4[1:]
                                        temp7 = temp6.removesuffix(".mp3")
                                        if temp7.lower() in songs_list:
                                            temp_path2 = Path(root2 + "/" + file).as_posix()
                                            path_to_song = check_album_in_path(albums, temp_path2)

                                            if path_to_song == None:
                                                continue
                                            else:
                                                shutil.copy(path_to_song, destination)
                                                song_name = temp7
                                                rename_songs(file, song_name, destination, "P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
                                    else:
                                        temp5 = temp4.removesuffix(".mp3")
                                        if temp5.lower() in songs_list:
                                            temp_path2 = Path(root2 + "/" + file).as_posix()
                                            path_to_song = check_album_in_path(albums, temp_path2)
                                            if path_to_song == None or "Disk" in path_to_song:
                                                continue
                                            else:
                                                shutil.copy(path_to_song, destination)
                                                song_name = temp5.lower()
                                                rename_songs(file, song_name, destination, "P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
                                if temp4.startswith("- "):
                                    temp5 = temp4[1:].strip()
                                    temp6 = temp5.removesuffix(".mp3")
                                    if temp6.lower() in songs_list:
                                        temp_path2 = Path(root2 + "/" + file).as_posix()
                                        path_to_song = check_album_in_path(albums, temp_path2)

                                        if path_to_song == None:
                                            continue
                                        else:
                                            shutil.copy(path_to_song, destination)
                                            song_name = temp6.lower()
                                            rename_songs(file, song_name, destination, "P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")

def parse_song_list(song_path):
    '''
    Takes a path to the song list and parses the names of the songs, artists
    and albums and returns them.
    '''
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
    '''
    Takes a list of songs and makes every string in the list lowercase.
    '''
    songs_list = []
    for i in songs:
        songs_list.append(i.lower())
    return songs_list

def check_album_in_path(albums, path):
    '''
    This function takes list of albums and a path where the song was found.
    It returns the path if the album is found in the path.
    '''
    for album in albums:
        if "Ã¦nima" in album:
            album = "ænima"
        if album in path:
            return path
        else:
            pass
    
def rename_songs(old_name, song_name, destination, song_path):
    '''
    Takes the song name from the src, song names from the list, destination
    where the song will be copied and the song list. If the song name is found
    in the song list then it will be copied with the new name. If there is a
    song with the same name there then remove it since it'll be copied.
    '''
    with open(song_path, 'r') as songs:
        for line in songs:
            if song_name in line.lower():
                new_name = line.removesuffix("\n")
                if os.path.isfile(destination + '\\' + new_name + ".mp3"):
                    os.remove(destination + '\\' + old_name)
                else:
                    os.rename(destination + '\\' + old_name, destination + '\\' + new_name + ".mp3")
            else:
                continue

#napraviti još test setova koji će još više izuzetaka imati kako bi poboljšao skriptu

# dodati if __name__ = main
if __name__ == "__main__":
    # parse CLI args
    args = parser.parse_args()
    
    # run the search, copy and rename method
    search_folder(args.destination, args.songlist)

#search_folder("E:\Glazba\Audioslave\(2002) Audioslave","Like A Stone", "F:\\test_folder_py")
#search_folder("F:\\test_folder_py")
#a, b, c, d = parse_song_list("P:\Git\Copy_Paste_app_python\Copy_paste_app_python\song_list.txt")
#print(f'song: {a}\nartist: {b}\nalbum: {c}\nnumbers: {d}')

#print(rename_songs([1, 22, 44, 5, 77, 101], "osha", "E:Glazba/"))