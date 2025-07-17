# Software Name: Music_Playlist_Mixer
# Category: Entertainment
# Description: The Music Playlist Mixer is an entertainment software application that allows users to create unique and personalized music playlists by combining songs from different genres. Users can select their favorite genres and set the desired mood of the playlist (such as relaxing, energetic, or romantic). The software will then analyze the selected genres and create a playlist that seamlessly transitions between the chosen genres, providing a dynamic and enjoyable listening experience. Users can save and export their playlists to share with friends or listen to them anytime.

import random

class MusicPlaylistMixer:
    def __init__(self, songs):
        """
        Initializes the MusicPlaylistMixer with a list of songs.
        Each song should be a dictionary with 'title', 'artist', 'genre', and 'mood' keys.
        """
        self.songs = songs

    def filter_songs(self, genres, mood):
        """
        Filters the songs based on the selected genres and mood.
        """
        filtered_songs = [
            song for song in self.songs
            if song['genre'] in genres and song['mood'] == mood
        ]
        return filtered_songs

    def create_playlist(self, genres, mood, playlist_length=10):
        """
        Creates a playlist of a specified length by selecting songs from the filtered list.
        """
        filtered_songs = self.filter_songs(genres, mood)

        if not filtered_songs:
            return "No songs found matching the selected criteria."

        playlist = random.sample(filtered_songs, min(playlist_length, len(filtered_songs)))
        return playlist

    def display_playlist(self, playlist):
        """
        Displays the playlist in a user-friendly format.
        """
        if isinstance(playlist, str):
            return playlist  # Return the error message

        if not playlist:
            return "Playlist is empty."

        playlist_string = "Playlist:\n"
        for i, song in enumerate(playlist):
            playlist_string += f"{i+1}. {song['title']} - {song['artist']} ({song['genre']}, {song['mood']})\n"
        return playlist_string

    def save_playlist(self, playlist, filename="my_playlist.txt"):
        """
        Saves the playlist to a text file.
        """

        if isinstance(playlist, str): # Error message check
            return playlist

        if not playlist:
            return "Playlist is empty, cannot save."
        try:
            with open(filename, "w") as f:
                for song in playlist:
                    f.write(f"{song['title']} - {song['artist']} ({song['genre']}, {song['mood']})\n")
            return f"Playlist saved to {filename}"
        except Exception as e:
            return f"Error saving playlist: {e}"


if __name__ == '__main__':
    # Example Usage:
    songs = [
        {'title': 'Song 1', 'artist': 'Artist A', 'genre': 'Pop', 'mood': 'energetic'},
        {'title': 'Song 2', 'artist': 'Artist B', 'genre': 'Rock', 'mood': 'energetic'},
        {'title': 'Song 3', 'artist': 'Artist C', 'genre': 'Jazz', 'mood': 'relaxing'},
        {'title': 'Song 4', 'artist': 'Artist D', 'genre': 'Pop', 'mood': 'romantic'},
        {'title': 'Song 5', 'artist': 'Artist E', 'genre': 'Rock', 'mood': 'relaxing'},
        {'title': 'Song 6', 'artist': 'Artist F', 'genre': 'Jazz', 'mood': 'energetic'},
        {'title': 'Song 7', 'artist': 'Artist G', 'genre': 'Pop', 'mood': 'energetic'},
        {'title': 'Song 8', 'artist': 'Artist H', 'genre': 'Rock', 'mood': 'romantic'},
        {'title': 'Song 9', 'artist': 'Artist I', 'genre': 'Jazz', 'mood': 'relaxing'},
    ]

    mixer = MusicPlaylistMixer(songs)

    # Create a playlist with Pop and Rock songs for an energetic mood
    genres = ['Pop', 'Rock']
    mood = 'energetic'
    playlist = mixer.create_playlist(genres, mood)
    print(mixer.display_playlist(playlist))

    # Save the playlist to a file
    save_result = mixer.save_playlist(playlist)
    print(save_result)

    # Example of no matching songs
    genres = ['Classical']
    mood = 'energetic'
    playlist = mixer.create_playlist(genres, mood)
    print(mixer.display_playlist(playlist))

    save_result = mixer.save_playlist(playlist, "classical_playlist.txt")
    print(save_result)