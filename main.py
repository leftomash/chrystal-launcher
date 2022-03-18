def main() -> None:
    import os
    from sys import platform
    from pathlib import Path

    def update() -> None:
        import requests

        with open("game_dir.txt", "r") as gd:
            game_dir = gd.read()

        get_file("", game_dir)


    def get_file(fid: str, _game_dir: str) -> None:
        from zdrive import Downloader

        dler = Downloader()
        dler.downloadFolder(fid, destinationFolder = Path.joinpath(_game_dir, "update"))

    def cgd(game_dir: str) -> None:
        with open("game_dir.txt", "r") as gd:
            current_game_dir = gd.read()
            
            if game_dir == current_game_dir:
                print("It is already the present game directory.")
                return
            else:
                gd.truncate()
                gd.write(game_dir)

    def install() -> None:
        with open("game_dir.txt", "r") as gd:
            game_dir = gd.read()

        if game_dir == '':
            print("Game directory not set yet. Please use cdg to set a default game directory.")    
        else:
            get_file("", game_dir)

    def help() -> None:
        print("cdg <path>  sets a default game directory")
        print("install     does a fresh installation of the latest version of the game")
        print("update      updates the game to the latest version")
        print("quit        quits the launcher")

    cmds: dict = {
        "update": update,
        "gd": cgd,
        "install": install,
        "help": help,
        "quit": quit
    }

    print("======CLI TOOL======\n")
    while True:
        cmd = input(">>> ").split(" ")

        try:
            cmds[cmd.pop(0)]()
        except KeyError:
            print("ERROR: Unknown Command")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nClosing the CLI Tool")