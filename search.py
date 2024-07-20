from pytube import Search
import sys

def get_url(video_name):
    return f"https://www.youtube.com/watch?v={Search(video_name).results[0].video_id}"

def main():
    print(get_url(' '.join(sys.argv[1:])))

if __name__ == "__main__":
    main()