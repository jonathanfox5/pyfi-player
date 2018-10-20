import vlc
import eyed3
import os
import operator

class SongPlayer(object):

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

    def first_item_in_nested_list(self, nested_list):
        first_item_list = []
        for full_item in nested_list:
            first_item_list.append(full_item[0])
        
        return first_item_list

    def create_playlist_from_folder(self, root_directory):
        # Get list of songs in the directory and sort them by their metadata
        song_list = self.get_audio_files_in_directory(root_directory)
        metadata = self.get_metadata_sorted(song_list)
        sorted_songs = self.first_item_in_nested_list(metadata)

        # Debug
        print("~~~Song List~~~")
        print(song_list)
        print("~~~Metadata~~~")
        print(metadata)
        print("~~~Sorted Songs~~~")
        print(sorted_songs)

        # Build the playlist
        self.create_playlist(sorted_songs)

    def create_playlist(self, song_list):
        media_list = self.instance.media_list_new(song_list)

        self.player.set_media_list(media_list)

    def get_audio_files_in_directory(self, root_directory):
        valid_audio_types = ["mp3"]

        try:
            all_files = os.listdir(root_directory)
        except FileNotFoundError:
            print("Directory does not exist: " + root_directory)
            return

        audio_file_list = []

        for file_type in valid_audio_types:
            slice_len = -1 * len(file_type)

            for file_name in all_files:
                if file_name[slice_len:] == file_type:
                    audio_file_list.append(
                        os.path.join(root_directory, file_name))

        print(audio_file_list)
        return audio_file_list
    
    def change_album(self, album_path):
        p.stop_playback()
        p.create_playlist_from_folder(album_path)
        p.start_playback()

    def get_metadata_sorted(self, file_list):

        # Pull out the metadata
        all_files_metadata = []
        for file in file_list:
            metadata = eyed3.load(file)
            metadata_list = [file, metadata.tag.track_num[0], metadata.tag.disc_num[0], metadata.tag.album]
            all_files_metadata.append(metadata_list)
        
        # Sort it (Filename - track num - disk num - album name)
        all_files_metadata = sorted(all_files_metadata, key=operator.itemgetter(0,1,2,3))

        return all_files_metadata


        
if __name__ == "__main__":
    p = SongPlayer()
    p.change_album("C:\\Users\\Jonathan\\Music\\Amazon MP3\\Rammstein\\Mutter")

    #file_list = p.get_audio_files_in_directory("C:\\Users\\Jonathan\\Music\\Amazon MP3\\Rammstein\\Mutter")
    #file_list=p.get_audio_files_in_directory("C:\\Users\\Jonathan\\Music\\Amazon MP3\\Emerson, Lake & Palmer\\Pictures At An Exhibition")
    #file_list = p.get_audio_files_in_directory("C:\\Users\\Jonathan\\Music\\test")
    
