from app.players.player import Player

from app.players.elves.elf import Elf

from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = 0
    for player in players:
        player.get_rating()
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dvarf in dwarves:
        dvarf.eat_favourite_dish()
