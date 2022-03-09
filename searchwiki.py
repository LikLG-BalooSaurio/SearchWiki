import wikipedia as wp
from colorama import Fore

print(Fore.GREEN + """
█████████████████████████████████████████████████████████████
█─▄▄▄▄█▄─▄▄─██▀▄─██▄─▄▄▀█─▄▄▄─█─█─███▄─█▀▀▀█─▄█▄─▄█▄─█─▄█▄─▄█
█▄▄▄▄─██─▄█▀██─▀─███─▄─▄█─███▀█─▄─████─█─█─█─███─███─▄▀███─██
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀
""")
print(Fore.RED + """
                                                    ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                                                    ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                                                    ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█
""")

wp.set_lang("es")

busqueda = input(Fore.GREEN + "    Que deseas buscar?  ")

resultado = wp.summary(busqueda)

print("""


""", Fore.CYAN + resultado)