import os
import random as rnd
import pygame

CONFIG_FILE = "musicli-config.txt"

def get_albums(path):
    albums = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".mp3") or file.endswith(".flac"):
                album = os.path.basename(root)
                if album not in albums:
                    albums[album] = []
                file_path = os.path.join(root, file)
                albums[album].append({"file": file, "path": file_path})
    return albums

def SequentialSearch(term,path):
    print("\nSearching for", term, ".....")

    album_dict = get_albums(path)
    album_names = list(album_dict.keys())
    
    matches = []
    for i in album_names:
        if term == i:
            matches.append(i)
    if len(matches) == 0:
        print("\nThere are no albums that match your search term. Try with a more specific term.\n")
    else:    
        print("Matching albums are: ", matches)
        return matches

def PlayRandomSong():
    album_dict = get_albums(path)
    all_songs = list(album_dict.items())
    
    total_albums = len(all_songs)
    random_album = rnd.randrange(0,total_albums)
    random_album = all_songs[random_album]
    album_songs = random_album[1]
    total_album_songs = len(album_songs)
    random_song_no = rnd.randrange(0,total_album_songs)
    random_song = album_songs[random_song_no]

    random_song_path = random_song['path']
    
    return random_song['file'],random_song_path

def Get_Album_Songs(album_name,path):
    all_albums = get_albums(path)
    return all_albums[album_name]

def search_songs(songs, query):
    results = []
    for song in songs:
        if query.lower() in song['file'].lower():
            results.append(song)
    return results

def setup():
    path = input("Enter the path to your music folder: ")
    with open(CONFIG_FILE, "w") as config_file:
        config_file.write(path)

class Player:
    def Play(path, file):
        print("Now Playing:", file)
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    
    def Pause(path,file):
        print("Paused song:", file)
        pygame.mixer.music.pause()

    def Unpause(path,file):
        print("Unpaused song:", file)
        pygame.mixer.music.unpause()
    
    def ChangeSong(path,file):
        print("Changing song")
        Player.Play(path,file)

    def Stop():
        pygame.mixer.music.stop()

def main():
    if not os.path.exists(CONFIG_FILE):
        setup()

    with open(CONFIG_FILE, "r") as config_file:
        path = config_file.read().strip()

    music_folder = path
    album_dict = get_albums(music_folder)

    print("""
                            ..                     :-=========--:               
                    .:-=+#%@@@%                    :+- .-==========.             
            -=+#%%@@@@@%#++-*@%                    -+=::========--=:             
            .@@#+=-:.....:-=+%@%                    :------:-====--=:             
            .@@=:=+*#%@@@@@%#%@%              :-====---------==-----.=%###*:      
            .@@@@%#*+=-:.    =@%            :+++=============------=.=@%%%@%-     
            .@@:             +@%            ==================------.*%%%%%%#     
            .@@:             =@%           .==========----:::::::::-*%%%%%%%%.    
            @@:       .+%@@%%@%           .========::+***********#%%%%%%%%%%:    
        :*#%#*@@:      -@@*--+@@%            =======:-%@@@@@@@@%%%%%%%%%%%%%%#     
    *@@*=*@@@:      *@%    *@%            :======.*@%%%%%%%%%%%%%%%%%%%%%%-     
    :@@:   :@@:      .%@@**%@%-             .----=.*@%%%%%%%#############*:      
    *@@*=+@@#         -+*#*-                      *%%%%%%%#+++**++-             
        -*%%%*-                                      *%%%%%%%%%%#==#%+             
                                                    =%%%%%%%%%%*..*%-             
                                                    :+*#%%%%%%%#*=.              
                                                        ..:::..                                   
    """)

    while True:
        print("\n\n=================================================================================================")
        print("======================= Welcome to SpotiPy - your python-cli music player =======================")
        print("=================================================================================================")

        print("\n1. Search for an album")
        print("2. Search for a song")
        print("3. Play a random song")
        print("9. Exit")
        opt = input("Enter your option: ")

        if opt == "1":
            print()
            searchTerm = input("Enter your search term: ")
            searched_albums = SequentialSearch(searchTerm, music_folder)

            if searched_albums:
                to_play_album = input("Do you want to play the Album? (Y/N): ")

                if to_play_album == "Y" or to_play_album == "y":

                    play_queue = Get_Album_Songs(searched_albums[0],music_folder)
                    
                    for i in play_queue:

                            path = i['path']
                            file = i['file']

                            Player.Play(path,file)
                            
                            while True:
                                player_option = int(input("\n(1)Pause (2)Play (3)Stop (4)Next Song: "))

                                if player_option == 1:
                                    Player.Pause(path,file)
                                
                                if player_option == 2:
                                    Player.Unpause(path,file)
                                
                                if player_option == 3:
                                    print("Stopping playback. Returning to Main Menu.")
                                    break

                                if player_option == 4:
                                    Player.Stop()
                                    break
                            if player_option == 3:
                                    break
        
        if opt == "2":
            albums = get_albums("/home/tushar/Documents/SoulSeek/SeekShare/Music")

            songs = []

            for i in albums:
                for j in albums[i]:
                    #print(j)
                    songs.append(j)


            #print(songs)
            print()
            query = input("Enter a song to search for: ")
            res = search_songs(songs=songs,query=query)
            #print(res)
            
            if len(res)>0:
                print('\nSongs that match your search term "'+query+'":')
                for i in range(len(res)):
                    print(str(i)+":",res[i]['file'])

                choice = int(input("What song to play? :"))
            
            else:
                print("No songs match your search term '"+query+"'")
                continue

            path = res[choice]['path'] 
            file = res[choice]['file']

            Player.Play(path,file)

            while True:
                player_option = int(input("\n(1)Pause (2)Play (3)Stop (4)Change Song: "))

                if player_option == 1:
                    Player.Pause(path,file)
                
                if player_option == 2:
                    Player.Unpause(path,file)
                
                if player_option == 3:
                    Player.Stop()
                    break

        if opt == "3":
            print()
            print("\nPlaying a random song..")
            file,path = PlayRandomSong()
            
            Player.Play(path,file)
            
            while True:
                player_option = int(input("\n(1)Pause (2)Play (3)Stop (4)Change Song: "))

                if player_option == 1:
                    Player.Pause(path,file)
                
                if player_option == 2:
                    Player.Unpause(path,file)
                
                if player_option == 3:
                    Player.Stop()
                    break

                if player_option == 4:
                    file,path = PlayRandomSong()
                    Player.ChangeSong(path,file)
            

        if opt == 'dict':
            print(album_dict)

        if opt == "9":
            break

if __name__ == "__main__":
    main()