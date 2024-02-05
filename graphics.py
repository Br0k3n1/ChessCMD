letterColors = {'p': "\033[92m"+"P"+"\033[0m", 'r': "\033[92m"+"R"+"\033[0m", 'n': "\033[92m"+"N"+"\033[0m", 'b': "\033[92m"+"B"+"\033[0m", 'q': "\033[92m"+"Q"+"\033[0m", 'k': "\033[92m"+"K"+"\033[0m"}

class LittleGameBoard():
    def __init__(self) -> None:
        pass
    
    def EmptyGameBoard():
        print("""[ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ]""")

    def LoadFEN(fen):
        gameBoard = ""
        for i in fen:
            if i.isnumeric():
                gameBoard = f"{gameBoard}{('[ ]' * int(i))}"
            elif i == '/':
                gameBoard = f"{gameBoard}\n"
            else:
                if i.islower():
                    gameBoard = f"{gameBoard}[{letterColors[i]}]"
                else:
                    gameBoard = f"{gameBoard}[{i}]"

        return gameBoard