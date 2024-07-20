from pytube import Search
import sys
# import pyperclip
import webbrowser


def get_url(video_name):
    return f"https://www.youtube.com/watch?v={Search(video_name).results[0].video_id}"

def main():
    url = get_url(' '.join(sys.argv[1:]))
    # print(url + ' copied into clipboard!' )
    # pyperclip.copy(url)
    webbrowser.open(url)

if __name__ == "__main__":
    main()