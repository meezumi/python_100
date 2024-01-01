from pytube import YouTube
from sys import argv

# documentation: "https://pytube.io/en/latest/"

# sys.argv is the list of command line arguments passed to a Python script.
#             (takes all the inputs from command line)

# argv[0] is always going to be the program name.
print(argv[0])

# link = argv[1]
# this will be the first input that we give to the program, i.e. link of the video

# video to download: "https://www.youtube.com/watch?v=BBJa32lCaaY"


link = input("Link of the yt video(type 'exit' to end): ")

while link != "exit":
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views:", yt.views)

    yd = yt.streams.get_highest_resolution()
    yd.download("./downloads")
    print("downloaded in ./downloads")
