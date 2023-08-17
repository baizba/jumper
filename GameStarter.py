from KangarooJackGame import KangarooJackGame
from KangarooJackGame import quit_game

kangaroo_game = KangarooJackGame()

while not kangaroo_game.is_game_exit():
    kangaroo_game.step()
    print(kangaroo_game.blue_water.water_x - (kangaroo_game.kangaroo_jack.kangaroo_x + kangaroo_game.kangaroo_jack.kangaroo_width))
    kangaroo_game.render(5)
    if kangaroo_game.is_crash():
        kangaroo_game.reset_game()

quit_game()
quit()
