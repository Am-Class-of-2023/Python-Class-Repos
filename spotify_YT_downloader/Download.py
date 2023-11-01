import spotipy
import tkinter as tk
from yt_dlp import YoutubeDL
from pytube import Search
from spotipy.oauth2 import SpotifyClientCredentials
from secret import CID, Secret

cid = CID
secret = Secret
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(auth_manager = client_credentials_manager)

top_tracks = [] # Global list

def download_vid():
    URLS = url_entry.get()
    with YoutubeDL() as ydl:
        ydl.download([URLS])

def download_song():
    audio_downloader = YoutubeDL({'format':'bestaudio'})
    audio_downloader.extract_info(watch_link)

def search_artist():
    global artist_name
    artist_name = artist_entry.get()
    results = sp.search(q='artist:' + artist_name, type='artist')
    artist_URI = results["artists"]["items"][0]["uri"]
    top_tracks.extend([f"{i+1}. {track['name']}" for i, track in enumerate(sp.artist_top_tracks(artist_URI)['tracks'][:10])])
    top_tracks_list.delete(0, tk.END)  # Clear the list
    for track in top_tracks:
        top_tracks_list.insert(tk.END, track)

    with open('Info.txt', 'w') as info:
        info.write("Spotify API dictionary:")
        info.write('\n')
        info.write(str(results))
        info.write('\n')
        info.write('\n')
    
    
def pick_song_and_update_button():
    global selected_song  # Declare selected_song as global
    selected_index = top_tracks_list.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_song = top_tracks[selected_index] + ' by ' + artist_entry.get()
        song_label.config(text=f"You have chosen {selected_song} by {artist_entry.get()}")
        pick_button.config(text="Pick a Song", command=pick_song_and_update_button)
        search_yt()
    else:
        song_label.config(text="Please select a song from the list.")
        pick_button.config(text="Pick a Song", command=pick_song_and_update_button)

def search_yt():
    global selected_song, watch_link
    selected_song = selected_song.split(".")[1].strip()
    print(selected_song)
    s = Search(selected_song)  
    search_results = s.results[0]
    split_results = str(search_results).split(':')
    first_item_stripped = split_results[1].strip()
    first_item_split = first_item_stripped.split('=')
    watch_link = 'https://www.youtube.com/watch?v=' + first_item_split[1]

        # Write link to file
    with open('Info.txt', 'a') as info:
        info.write("Song with artist:")
        info.write('\n')
        info.write(str(selected_song))
        info.write('\n')
        info.write('\n')
        info.write("Youtube Link:")
        info.write('\n')
        info.write(watch_link)

    return watch_link



# Function calls
#---------------#

# To download a song:
#download_song(search_yt(get_artist_name()))

# To download a YouTube video:
#download_vid(ask_url())

# Test video link:
#https://www.youtube.com/watch?v=ycHVUvvOwzY

#***********************************************  MAIN WINDOW  ***********************************************#

# Main window name
window = tk.Tk()
window.title('YouTube Video and Song Downloader')


# Create entry and label fields
url_label = tk.Label(window, text="Enter YouTube Video URL:")
url_entry = tk.Entry(window, width=50)
artist_label = tk.Label(window, text="Enter Artist Name:")
artist_entry = tk.Entry(window, width=50)
top_ten_label = tk.Label(window,text="Top 10 Tracks:")
artist_label = tk.Label(window, text="Enter Artist Name:")
artist_entry = tk.Entry(window)
song_label = tk.Label(window, text="")
pick_button = tk.Button(window, text="Pick a Song", command= pick_song_and_update_button)

# Top ten list display
top_tracks_list = tk.Listbox(window, selectmode=tk.SINGLE)

# Create buttons
download_video_button = tk.Button(window, text="Download Video", command=download_vid)
search_button = tk.Button(window, text="Search", command=search_artist)
download_song_button = tk.Button(window, text="Download Song", command=download_song)

# Arrange widgets using the grid layout manager
url_label.grid(row=0, column=0, sticky='nsew')
url_entry.grid(row=0, column=1, sticky='nsew')
download_video_button.grid(row=0, column=2, sticky='nsew')
artist_label.grid(row=1, column=0, sticky='nsew')
artist_entry.grid(row=1, column=1, sticky='nsew')
search_button.grid(row=1, column=2, columnspan=2, sticky='nsew')
top_tracks_list.grid(row=2, column=0, columnspan=2, sticky='nsew')
pick_button.grid(row=2, column=2, columnspan=2, sticky='n')
download_song_button.grid(row=3, column=2, columnspan=2, sticky='n')
song_label.grid(row=3, column=0, sticky='n')

# Configure column weights to make them expand with the window
window.columnconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

window.mainloop()