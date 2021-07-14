# Create VLC playlists at the root of the drive for easy access from the TV.
# For each playlist to generate, we walk the specified folders recursively and add 
# all media files to the list.

# Possibility: Don't use VLC's shuffle and simply create huge static playlists
# This would provide the benefit of being able to control the distribution of random content.
# We could also look into, E.G., inserting random soviet commercials between episodes, which is dope

import os


drive_root = u"F:\\"

out_file = "everything.vlc"

playlist = open(os.path.join(drive_root, out_file), 'a')

ext_filter = [
    ".mkv",
    ".avi",
    ".mp4",
    ".wmv",
    ".mpg",
]

os.chdir(drive_root)
for root, dirs, files in os.walk(u"./"):

    for file in files:
        path = os.path.join(root, file)

        if ".unwanted" in path:
            continue

        f, e = os.path.splitext(file)

        if e not in ext_filter:
            continue

        playlist.write(path)
        playlist.write("\n")

playlist.close()