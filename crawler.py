import os


def get_audio_files_in_directory(root_directory):
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
                audio_file_list.append(os.path.join(root_directory, file_name))

    print(audio_file_list)
    return audio_file_list
