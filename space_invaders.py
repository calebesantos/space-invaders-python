import config
from game.game_controller import GameController

if __name__ == '__main__':
	game = GameController(config.ORIGINAL_CAPTION)
	game.main()