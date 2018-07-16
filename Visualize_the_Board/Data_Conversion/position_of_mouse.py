'''
This function's main goal is to translate the coordinates of the mouse into what position of the chessboard the mouse is in
This was a repetative implementation, there might (most likely) another way to implement this that is more effecient both in the run time,
and the time it took to code

IF YOU DON'T KNOW THE CHESS POSITIONS: http://www.chess-poster.com/english/learn_chess/notation/images/coordinates_2.gif
'''

class find_position():
    def chess_position(self, pos):
        if pos[0] <= 102.5 and pos[1] <= 100:
            return "a1"
        elif pos[0] <= 205 and pos[1] <= 100:
            return "b1"
        elif pos[0] <= 307.5 and pos[1] <= 100:
            return "c1"
        elif pos[0] <= 410 and pos[1] <= 100:
            return "d1"
        elif pos[0] <= 512.5 and pos[1] <= 100:
            return "e1"
        elif pos[0] <= 615 and pos[1] <= 100:
            return "f1"
        elif pos[0] <= 717.5 and pos[1] <= 100:
            return "g1"
        elif pos[0] <= 820 and pos[1] <= 100:
            return "h1"
        elif pos[0] <= 102.5 and pos[1] <= 200:
            return("a2")
        elif pos[0] <= 205 and pos[1] <= 200:
            return("b2")
        elif pos[0] <= 307.5 and pos[1] <= 200:
            return("c2")
        elif pos[0] <= 410 and pos[1] <= 200:
            return("d2")
        elif pos[0] <= 512.5 and pos[1] <= 200:
            return("e2")
        elif pos[0] <= 615 and pos[1] <= 200:
            return("f2")
        elif pos[0] <= 717.5 and pos[1] <= 200:
            return("g2")
        elif pos[0] <= 820 and pos[1] <= 200:
            return("h2")
        elif pos[0] <= 102.5 and pos[1] <= 300:
            return("a3")
        elif pos[0] <= 205 and pos[1] <= 300:
            return("b3")
        elif pos[0] <= 307.5 and pos[1] <= 300:
            return("c3")
        elif pos[0] <= 410 and pos[1] <= 300:
            return("d3")
        elif pos[0] <= 512.5 and pos[1] <= 300:
            return("e3")
        elif pos[0] <= 615 and pos[1] <= 300:
            return("f3")
        elif pos[0] <= 717.5 and pos[1] <= 300:
            return("g3")
        elif pos[0] <= 820 and pos[1] <= 300:
            return("h3")
        elif pos[0] <= 102.5 and pos[1] <= 400:
            return("a4")
        elif pos[0] <= 205 and pos[1] <= 400:
            return("b4")
        elif pos[0] <= 307.5 and pos[1] <= 400:
            return("c4")
        elif pos[0] <= 410 and pos[1] <= 400:
            return("d4")
        elif pos[0] <= 512.5 and pos[1] <= 400:
            return("e4")
        elif pos[0] <= 615 and pos[1] <= 400:
            return("f4")
        elif pos[0] <= 717.5 and pos[1] <= 400:
            return("g4")
        elif pos[0] <= 820 and pos[1] <= 400:
            return("h4")
        elif pos[0] <= 102.5 and pos[1] <= 500:
            return("a5")
        elif pos[0] <= 205 and pos[1] <= 500:
            return("b5")
        elif pos[0] <= 307.5 and pos[1] <= 500:
            return("c5")
        elif pos[0] <= 410 and pos[1] <= 500:
            return("d5")
        elif pos[0] <= 512.5 and pos[1] <= 500:
            return("e5")
        elif pos[0] <= 615 and pos[1] <= 500:
            return("f5")
        elif pos[0] <= 717.5 and pos[1] <= 500:
            return("g5")
        elif pos[0] <= 820 and pos[1] <= 500:
            return("h5")
        elif pos[0] <= 102.5 and pos[1] <= 600:
            return("a6")
        elif pos[0] <= 205 and pos[1] <= 600:
            return("b6")
        elif pos[0] <= 307.5 and pos[1] <= 600:
            return("c6")
        elif pos[0] <= 410 and pos[1] <= 600:
            return("d6")
        elif pos[0] <= 512.5 and pos[1] <= 600:
            return("e6")
        elif pos[0] <= 615 and pos[1] <= 600:
            return("f6")
        elif pos[0] <= 717.5 and pos[1] <= 600:
            return("g6")
        elif pos[0] <= 820 and pos[1] <= 600:
            return("h6")
        elif pos[0] <= 102.5 and pos[1] <= 700:
            return("a7")
        elif pos[0] <= 205 and pos[1] <= 700:
            return("b7")
        elif pos[0] <= 307.5 and pos[1] <= 700:
            return("c7")
        elif pos[0] <= 410 and pos[1] <= 700:
            return("d7")
        elif pos[0] <= 512.5 and pos[1] <= 700:
            return("e7")
        elif pos[0] <= 615 and pos[1] <= 700:
            return("f7")
        elif pos[0] <= 717.5 and pos[1] <= 700:
            return("g7")
        elif pos[0] <= 820 and pos[1] <= 700:
            return("h7")
        elif pos[0] <= 102.5 and pos[1] <= 800:
            return("a8")
        elif pos[0] <= 205 and pos[1] <= 800:
            return("b8")
        elif pos[0] <= 307.5 and pos[1] <= 800:
            return("c8")
        elif pos[0] <= 410 and pos[1] <= 800:
            return("d8")
        elif pos[0] <= 512.5 and pos[1] <= 800:
            return("e8")
        elif pos[0] <= 615 and pos[1] <= 800:
            return("f8")
        elif pos[0] <= 717.5 and pos[1] <= 800:
            return("g8")
        elif pos[0] <= 820 and pos[1] <= 800:
            return("h8")
