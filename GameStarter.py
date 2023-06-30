from KangarooJackGame import KangarooJackGame
from KangarooJackGame import quit_game

kangaroo_game = KangarooJackGame()

while not kangaroo_game.is_game_exit():
    kangaroo_game.step()
    kangaroo_game.render(40)
    if kangaroo_game.is_crash():
        kangaroo_game.reset_game()

quit_game()
quit()
