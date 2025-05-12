import typing
import yt_dlp

class Entry(typing.TypedDict, total=False):
    url: str
    title: str
    duration: list[int] | None
    filesize: list[int] | None

def search_urls(search_word: str) -> list[tuple[str, str, int | None]]:
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "noplaylist": True,
        "extract_flat": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch10:{search_word}", download=False)
        if result and isinstance(result, dict) and "entries" in result:
            entries = result["entries"]
            if isinstance(entries, list):
                return [
                    (
                        entry.get("url", ""),
                        entry.get("title", ""),
                        int(entry.get("duration")) if entry.get("duration") else None,
                    )
                    for entry in entries
                    if isinstance(entry, dict)
                ]
        return []


def download_video(url: str, output_path: str):
    ydl_opts = {"outtmpl": f"{output_path}/%(title)s.%(ext)s", "format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        _ = ydl.download([url])


def main():
    search_word = input("Enter a search term: ")
    urls = search_urls(search_word)
    if not urls:
        print("No videos found.")
        return

    print("Found videos:")
    for i, (url, title, duration) in enumerate(urls, start=1):
        duration_str = f"{duration // 3600}:{duration // 60}:{duration % 60}" if duration else "Unknown duration"
        print(f"{i}: {title} ({url}) - {duration_str}")

    choice = int(input("Enter the number of the video to download: "))
    if 1 <= choice <= len(urls):
        output_path = input("Enter the output directory: ")
        download_video(urls[choice - 1][0], output_path)
        print("Download complete.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
