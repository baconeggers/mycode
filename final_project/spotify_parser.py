""" 
             Spotify data parser | Charles M Eggers II 
    ___________________________________________________________
    Ideally, this program will be able to dig through the 13(?)
    files that Spotify provided for me when requesting my data.
    I'd like to be able to search for the first time I listened
    to a song or artist, or all songs by a specific artist, 
    stuff like that 

"""

import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def historical_pull():
    try:
        user_dir = input("Please enter the full path to historical .JSON files: ")
        os.chdir(user_dir)
        user_data = input("Please enter the file name you would like to export data from: ")
        if user_data == "quit" or user_data == "q":
            print("Thank you for trying this tool.")
            quit()
        else:
            with open(user_data,"r", encoding="utf-8") as data:
                med_data = data.read()
                clean_data = json.loads(med_data)
                for track in clean_data:
                    track_list = track['master_metadata_track_name']
                    artist_list = track['master_metadata_album_artist_name']
                    time_stamp = track['ts']
                    with open("export.csv","a", encoding="utf-8") as export:
                        export.write(f"{artist_list};{track_list};{time_stamp}\n")
            print("Your data has been exported to 'export.csv'\nThank you for using this tool!")
    except FileNotFoundError:
        print("That file was not found, please try again.")
        historical_pull()
    except Exception as err:
        print("We encountered an unexprected error:", err)


def current_pull():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    user_search = input("\nWould you like to search for a Song, an Album, or an Artist?\nOr type 'q' to quit\n").lower()
    search_result = ''
    if user_search == 'q':
        main()

    elif user_search == "song":
        song_search = input("What song would you like to search for?\n")
        search_str = song_search
        search_result = sp.search(search_str,limit=5,type='track')
        result_num = 1
        
        print("\nSEARCH RESULTS")
        for item in search_result['tracks']['items']:
            song_title = item['name'] 
            album_title = item['album']['name']
            link_to_song = item['external_urls']['spotify']
            artists= [] 
            for y in item["artists"]: 
                artists.append(y['name'])
        
            print(f"""\nSearch Result #{result_num}:
            {song_title} by {", ".join(artists)}
            Album Title: {album_title}
            {link_to_song}""")
            result_num += 1
    
    elif user_search == "album":
        artist_search = input("What album would you like to search for?\n")
        search_str = artist_search
        search_result = sp.search(search_str,limit=5,type='album')
        result_num = 1
        
        print("\nSEARCH RESULTS")
        for item in search_result['albums']['items']:
            album_title = item['name']
            link_to_album = item['external_urls']['spotify']
            artists= [] 
            for y in item["artists"]: 
                artists.append(y['name'])
         
            print(f"""\nSearch Result #{result_num}:
            Album Title: {album_title}
            By {", ".join(artists)}
            {link_to_album}""")
            result_num += 1

    elif user_search == "artist":
        album_search = input("What artist would you like to seach for?\n")
        search_str = album_search
        search_result = sp.search(search_str,limit=5,type='artist')

        result_num = 1
        print("\nSEARCH RESULTS")
        for item in search_result['artists']['items']:
            artist = item['name']
            followers = item['followers']['total']
            link_to_artist = item['external_urls']['spotify']
            
            print(f"""\nSearch Result #{result_num}:
            {artist}
            Followers: {followers}
            {link_to_artist}""")
            result_num += 1

    else:
        print("\nThat was not a valid search option, please try again.")
        current_pull()
    

def main():
    print("Welcome to the Spotify API Parser")
    choice = input("Would you like to pull historical account data, or current streaming information?\nPlease enter either 'Historical', 'Current', or 'Quit'\n")
    choice.lower()
    if choice == "quit" or choice == "q":
        print("Thank you for trying this tool.")
        quit()
    elif choice == "historical":
        historical_pull()
    elif choice == "current":
        current_pull()
    else:
        print("You did not enter a valid option.")
        main()


if __name__ == "__main__":
    main()