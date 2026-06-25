import yt_dlp
import pathlib
import static_ffmpeg
import typing
import time


def download_youtube_video_from_url(url: str, output_dir: pathlib.Path):
    file_name = (
        "%(playlist_title)s/%(upload_date)s_%(channel)s_%(title)s [%(id)s].%(ext)s"
    )
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": str(output_dir / file_name),
        "windowsfilename": True,
        "quiet": False,
        "no_warnings": True,
        "sleep_interval": 3,
        "max_sleep_interval": 8,
        "sleep_interval_requests": 1,
        "retries": 5,
        "fragment_retries": 5,
        "download_archive": str(output_dir / "downloaded.txt"),
        "cookiefile": "cookies.txt",
    }
    with yt_dlp.YoutubeDL(typing.cast(typing.Any, ydl_opts)) as ydl:  # pyright: ignore[reportAny]
        _ = ydl.download([url])


def download_list_file(url_file: pathlib.Path, output_dir: pathlib.Path):
    with url_file.open() as f:
        index = 0
        for url in f:
            url = url.strip()
            if not url:
                continue
            try:
                download_youtube_video_from_url(url, output_dir)
                time.sleep(1)
            except Exception as e:
                print(f"error:{url}:\n{e}")
                continue
            index += 1
            print("download " + url)


def main():
    if not static_ffmpeg.add_paths():  # pyright: ignore[reportUnknownMemberType]
        print("ffmpeg not found")
        return
    current_dir = pathlib.Path(__file__).parent
    dir_path = current_dir / pathlib.Path("videos")
    url_file = current_dir / "urls.txt"
    download_list_file(url_file, dir_path)


if __name__ == "__main__":
    main()
