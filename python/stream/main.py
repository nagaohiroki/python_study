import yt_dlp
import typing
import os

def open_urls(text_file: str = "url.txt"):
    urls = []
    with open(text_file, "r") as f:
        urls = f.read().splitlines()
        urls = [url for url in urls if url and not url.startswith("#")]
        return urls


def download_youtube_video(url: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        code = ydl.download([url])
        if code == 0:
            print(f"Downloaded {url}")
        else:
            print(f"Failed to download {url}")


def download_youtube_videos():
    urls = open_urls()
    for url in urls:
        download_youtube_video(url, "videos")


def find_urls(keyword: str, output_path: str):
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        extra_info: dict[str, typing.Any] | None = ydl.extract_info(
            f"ytsearch:{keyword}", download=False
        )
        if extra_info is None or "entries" not in extra_info:
            return
        for entry in extra_info["entries"]:
            title = entry["title"]
            if not title:
                continue
            print(str(title))


def main():
    find_urls("neovim", "videos")
    # download_youtube_videos()


if __name__ == "__main__":
    main()
