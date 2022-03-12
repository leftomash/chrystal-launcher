def main() -> None:
    import os

    system: str = __import__("sys").platform

    if system == 'linux':
        from mega import Mega

        mega = Mega()

        mega.login()
        mega.download_url("https://mega.nz/file/XjRX2aKR#II1QmbxzTzcYJ1Qhi5sXUwt0_a4wrilC7CoF96QgJKo", "gods_call.zip")

    elif system == 'win32':
        pass
    elif system == 'darwin':
        pass
    else:
        print("bro wut kind of dum os are you using?")
        input("press any key to exit")

def get_latest_version(dl_link: str):
    pass


def get_file(id: str, destination: str) -> None:
    import requests


if __name__ == "__main__":
    main()