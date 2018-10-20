import vlc, eyed3
import os


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

    def create_playlist_from_folder(self, root_directory):
        song_list = self.get_audio_files_in_directory(root_directory)
        self.create_playlist(song_list)

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


if __name__ == "__main__":
    p = SongPlayer()
    # p.change_album("/share/Rammstein/Mutter")
    file_list = p.get_audio_files_in_directory("/share/Rammstein/Mutter")
    audiofile = eyed3.load(file_list[0])
    print(audiofile.tag)
    print()
    #get_meta
