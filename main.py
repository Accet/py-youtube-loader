from pytube import YouTube
import os, pytube

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(os.path.dirname(pytube.__file__))
    link = input("Enter the link: ")
    yt = YouTube(link)
    # Title of video
    print("Title :", yt.title)
    # Length of the video
    print("Length of video: ", yt.length, "seconds")
    # Description of video
    print("Description: ", yt.description)
    print(yt.streams.filter(progressive=True))
    ys = yt.streams.get_highest_resolution()
    # Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
