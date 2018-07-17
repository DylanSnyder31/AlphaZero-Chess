'''
This is the position of all the pieces, in a dictionary. This data is essential for the gameplay to work
'''
position_dic = { 'a1': "Left White Rook", 'b1': "Left White Knight", 'c1': "Left White Bishop", 'd1': "White Queen", 'e1': "White King", 'f1': "Right White Bishop", 'g1': "Right White Knight", 'h1': "Right White Rook",
                        'a2': "White Pawn1", 'b2': "White Pawn2", 'c2': "White Pawn3", 'd2': "White Pawn4", 'e2': "White Pawn5", 'f2': "White Pawn6", 'g2': "White Pawn7", 'h2': "White Pawn8",
                        'a3': "None", 'b3': "None", 'c3': "None", 'd3': "None", 'e3': "None", 'f3': "None", 'g3': "None", 'h3': "None",
                        'a4': "None", 'b4': "None", 'c4': "None", 'd4': "None", 'e4': "None", 'f4': "None", 'g4': "None", 'h4': "None",
                        'a5': "None", 'b5': "None", 'c5': "None", 'd5': "None", 'e5': "None", 'f5': "None", 'g5': "None", 'h5': "None",
                        'a6': "None", 'b6': "None", 'c6': "None", 'd6': "None", 'e6': "None", 'f6': "None", 'g6': "None", 'h6': "None",

                        'a8': "Left Black Rook", 'b8': "Left Black Knight", 'c8': "Left Black Bishop", 'd8': "Black Queen", 'e8': "Black King", 'f8': "Right Black Bishop", 'g8': "Right Black Knight", 'h8': "Right Black Rook",
                        'a7': "Black Pawn1", 'b7': "Black Pawn2", 'c7': "Black Pawn3", 'd7': "Black Pawn4", 'e7': "Black Pawn5", 'f7': "Black Pawn6", 'g7': "Black Pawn7", 'h7': "Black Pawn8"
}

'''
Decalres what team is allowed to move their pieces
'''

conversion_to_number = {'a1': 1, 'b1': 2, 'c1': 3, 'd1':4, 'e1':5, 'f1':6, 'g1':7, 'h1':8,
                        'a2': 9, 'b2': 10, 'c2': 11, 'd2':12, 'e2':13, 'f2':14, 'g2':15, 'h2':16,
                        'a3': 17, 'b3': 18, 'c3': 19, 'd3':20, 'e3':21, 'f3':22, 'g3':23, 'h3':24,
                        'a4': 25, 'b4': 26, 'c4': 27, 'd4':28, 'e4':29, 'f4':30, 'g4':31, 'h4':32,
                        'a5': 33, 'b5': 34, 'c5': 35, 'd5':36, 'e5':37, 'f5':38, 'g5':39, 'h5':40,
                        'a6': 41, 'b6': 42, 'c6': 43, 'd6':44, 'e6':45, 'f6':46, 'g6':47, 'h6':48,
                        'a7': 49, 'b7': 50, 'c7':51, 'd7':52, 'e7':53, 'f7':54, 'g7':55, 'h7':56,
                        'a8': 57, 'b8': 58, 'c8': 59, 'd8':60, 'e8':61, 'f8':62, 'g8':63, 'h8':64}

team_turn = 1
