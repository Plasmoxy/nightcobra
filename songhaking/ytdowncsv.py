import csv, sys, os
from shutil import which

filename = "songs.csv"
songnames = []

print("=== Youtube CSV query to MP3 downloader ===")

# check for youtube-dl
if which("youtube-dl") is None:
    raise Exception("You don't have youtube-dl program installed! (pip3 install youtube-dl)")

# if no arguments
if len(sys.argv) < 2:
    # if no default file
    if not os.path.exists(filename):
        raise ValueError("Create file songs.csv with song names or specify the csv file path as an argument!")
# if arguments
else:
    if os.path.exists(sys.argv[1]):
        filename = sys.argv[1]
    else:
        raise ValueError("Specified file doesn't exist!")


print("Reading csv file ....")
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        for item in row:
            if (item != ''):
                songnames.append(item)

print(f"Downloading songs : {songnames}")

print("=== DOWNLOADING SONGS ... ===")
for song in songnames:
    os.system(f"youtube-dl --add-metadata -x --audio-format mp3 -o \"songs/%(title)s.%(ext)s\" \"ytsearch1:{song}\"")