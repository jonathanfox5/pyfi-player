import operator
import os

import eyed3
import vlc

import crawler
import utilities as u


class SongPlayer():
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_list_player_new()

    def stop_playback(self):
        self.player.stop()

    def start_playback(self):
        self.player.play()

    def pause_playback(self):
        self.player.pause()

    def play_next_track(self):
        self.player.next()

    def play_previous_track(self):
        self.player.previous()

    def create_playlist_from_folder(self, root_directory):
        # Get list of songs in the directory and sort them by their metadata
        song_list = crawler.get_audio_files_in_directory(root_directory)
        metadata = self.get_metadata_sorted(song_list)
        sorted_songs = u.first_item_in_nested_list(metadata)

        # Debug
        print("~~~Folder~~~")
        print(root_directory)
        print("~~~Song List~~~")
        print(song_list)
        print("~~~Metadata~~~")
        print(metadata)
        print("~~~Sorted Songs~~~")
        print(sorted_songs)

        # Build the playlist
        self.set_playlist(sorted_songs)

    def set_playlist(self, song_list):
        media_list = self.instance.media_list_new(song_list)

        self.player.set_media_list(media_list)

    def change_album(self, album_path):
        self.stop_playback()
        self.create_playlist_from_folder(album_path)
        self.start_playback()

    def get_metadata_sorted(self, file_list):

        # Pull out the metadata
        all_files_metadata = []
        for file in file_list:
            metadata = eyed3.load(file)
            metadata_list = [
                file,
                u.nz(metadata.tag.track_num[0]),
                u.nz(metadata.tag.disc_num[0]),
                u.nz(metadata.tag.album, "")
            ]
            all_files_metadata.append(metadata_list)

        # Sort it (album name -> disk num -> track num -> filename)
        all_files_metadata = sorted(
            all_files_metadata, key=operator.itemgetter(3, 2, 1, 0))

        return all_files_metadata

    def play_boot_sound(self):
        file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "assets", "boot.mp3")

        self.stop_playback()
        self.set_playlist([file_path])
        self.start_playback()
