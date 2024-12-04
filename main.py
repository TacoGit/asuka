## Discord presence
from pypresence import Presence, ActivityType ## Only works via the github version in requirements.txt

## Colors
from colorama import Fore, Back, init
init(autoreset=True)

## Discord time tracking
import time
import os

## Autofill
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML

## Self-explanatory
from loader import Loader ## Available in the same directory

## MyAnimeList provider
from jikanpy import Jikan
jikan = Jikan()
import json

#### Variables
activity_title = "HiAnime"
client_id = '1313618987980034188'
theme = Fore.LIGHTRED_EX
download_amount_pages = 5 ## Default 5, lower for faster but less smarter code

logo = theme + " [" + Fore.RESET + "================================" + theme + "] \n" + theme + """⠀ ⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠂⡻⠅⠈⠀⠀⠘⠒⢲⣼⣷⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣡⡪⠙⡁⠀⣼⢠⠀⠈⢄⠀⠀⠑⢄⠨⡙⠣⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠸⣑⣄⢎⠈⡀⣿⠀⣆⠘⡄⢣⡀⠰⡀⠱⡌⠳⠪⣆⠀⠀⠀⠀⠀
    ⡀⠈⠄⠀⠀⠰⠋⡏⣬⢠⣸⠻⣧⡟⢧⠸⡌⣙⣦⣵⣄⠹⡷⢷⢩⠄⠀⠀⠀⠀
    ⡈⢄⠈⡌⡀⠀⢠⠿⢹⢸⡟⠶⠹⠏⢁⠑⠏⠙⠛⠙⢸⣦⡏⠈⣿⠀⠀⠀⠀⠀
    ⢷⣄⣱⠔⠁⠀⠈⠸⡀⠻⠿⠀⠀⠀⢈⣄⠀⠀⠀⠀⡸⢩⡇⢰⢹⠀⠀⠀⠀⠀
    ⢦⠙⣯⠈⢣⠀⠀⠇⠀⡇⣷⢣⡀⠀⠸⣿⡇⠀⢀⠞⡞⠙⣷⠀⡎⡆⠀⠀⠀⠀
    ⠀⠍⣍⡺⡸⠀⢰⠀⢄⣿⠁⢸⢸⠑⣄⠉⣀⠔⡇⡘⡇⣠⠸⡀⠘⡰⠀⠀⠀⠀
    ⠸⢊⣡⡐⠃⢡⣶⠀⠸⡇⠸⡼⠈⣇⣕⠛⠛⠛⢣⠵⠧⡿⠤⠧⢀⠁⢃⠀⠀⠀
    ⠘⢄⠉⠑⡅⢼⡆⠀⠔⠓⢖⣩⡶⢉⠸⠀⣀⠠⠕⣖⠏⠀⠀⠀⠀⠑⢢⡆⠀⠀
    ⠀⢨⠀⠀⡌⡌⡷⠁⠀⠀⠀⢣⠃⠀⠁⠈⠁⠀⢰⡸⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀
    ⡠⠁⠀⡜⢀⡱⠁⠀⠀⣆⡸⢆⠀⠀⠀⠀⢀⠠⠃⡅⠀⢠⠜⢿⣄⠀⠀⠀⠀⠁
    ⠁⠀⡐⡠⠊⠀⠀⠀⡠⡿⠃⠀⠑⢄⣀⠔⠁⠀⠀⠀⠠⡸⢀⡆⠀⡗⠠⣀⠀⠀""" + theme + "\n [" + Fore.RESET + " ================================ " + theme + "] \n" + Fore.RESET

#### Set the RPC
def start_rpc(title):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    loader = Loader(theme + ">" + Fore.RESET + f" Getting necessary information for {title}", "keep_empty", 0.05).start()

    for i in range(3):
        time.sleep(0.25)

    response = jikan.search('anime', title)
    anime = response['data'][0]
    anime_info = {
        'title': anime['title'],
        'episodes': anime['episodes'],
        'large_image': anime['images']['jpg']['large_image_url'],
        'small_image': anime['images']['jpg']['small_image_url']
    }

    loader.stop()

    print(theme + "\n>" + Fore.RESET + f" Discord RPC set to the following")
    print(theme + f"- Activity" + Fore.RESET + f" Watching {activity_title}")
    print(theme + f"- Title" + Fore.RESET + f" {anime_info['title']}")
    print(theme + f"- Episode(s)" + Fore.RESET + f" 1/{anime_info['episodes']}\n")

    rpc.update(
        activity_type = ActivityType.WATCHING,
        state=f"Episode: 1/{anime_info['episodes']}",
        details=f"{anime_info['title']}",
        large_image=f"{anime_info['large_image']}",
        small_image=f"https://cdn-icons-png.flaticon.com/512/565/565259.png",
        end=time.time(),
        instance=False
    )

    input(f"{Fore.RESET}Press {theme}ENTER{Fore.RESET} to stop the RPC\n")
    exit()
    


#### Main
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    
    loader = Loader(theme + ">" + Fore.RESET + " Trying to create a connection with Discord", "keep_empty", 0.05).start()
    rpc = Presence(client_id)
    rpc.connect()
    loader.stop()

    loader = Loader(theme + ">" + Fore.RESET + " Downloading the top anime titles", "keep_empty", 0.05).start()
    full_anime_data = []

    if os.path.exists('anime_cache.json'):
        with open('anime_cache.json', 'r') as json_file:
            full_anime_data = json.load(json_file)
    else:
        for page in range(1, download_amount_pages):
            response = jikan.top(type='anime', page=page) ## Should be about 175 animes
            full_anime_data.extend(response['data'])
            time.sleep(1)

    anime_list = [anime['title'] for anime in full_anime_data]
    loader.stop()

    anime_completer = WordCompleter(anime_list, ignore_case=True)
    session = PromptSession()

    if not os.path.exists('anime_cache.json'):
        with open('anime_cache.json', 'w') as json_file:
            json.dump(full_anime_data, json_file, indent=4)

    try:
        prompt_text = HTML('<ansibrightred>></ansibrightred> Select anime: ')
        selected_anime = session.prompt(prompt_text, completer=anime_completer)

        response = jikan.search('anime', selected_anime)
        titles = [
            anime['title_english'] if anime['title_english'] else anime['title']
            for anime in response['data']
        ]
        titles = titles[:8]

        for i, title in enumerate(titles, start=1):
            print(theme + f"- {i}" + Fore.RESET + f" {title}")

        user_input = session.prompt(HTML('<ansibrightred>></ansibrightred> Choose a number [1/8]: '))
        selected_title = titles[int(user_input) - 1] if user_input.isdigit() and 1 <= int(user_input) <= 8 else None
        start_rpc(selected_title)
        # print(titles)
    except KeyboardInterrupt:
        print(Back.WHITE + theme + " ! " + Back.LIGHTRED_EX + Fore.BLACK + f" Cancelled{Fore.RESET} \n")

rpc.clear()
