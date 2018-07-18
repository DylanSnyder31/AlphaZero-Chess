#Import Chess module
import chess

#Import from Kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

#Import files from another folder
from Visualize_the_Board.Data_Conversion.position_of_mouse import find_position
from Visualize_the_Board.Data_Conversion.position_of_pieces import conversion_to_number, team_turn, position_dic
from Visualize_the_Board.Data_Conversion.chess_coords_to_real_coords import convert_coordinates
from Visualize_the_Board.Data_Conversion.difference_for_letter import promotion_piece

#Just for the Random AI
import random
import sys
import os

class Scatter_Text_widget(Screen):
    #The function of this class is to display a GUI for the user to use when playing against the AI

    def __init__(self, **kwargs):

        super(Scatter_Text_widget, self).__init__(**kwargs)
        self.position = find_position()
        self.position_piece = position_dic
        self.turn = team_turn

        #Set the board that is used for the the Algorithm
        self.board = chess.Board()

    def on_touch_down(self, touch):
        res = super(Scatter_Text_widget, self).on_touch_down(touch)

        if res:
            pos_chess = self.position.chess_position(touch.pos)
            #Saves the data of where, and what was clicked on
            self.clicked_input = [pos_chess,self.position_piece[str(pos_chess)]]

    def on_touch_up(self, touch):
        conversion = convert_coordinates
        scatter = Scatter_Text_widget()
        self.move_worked = True

        res = super(Scatter_Text_widget, self).on_touch_up(touch)

        if res:
            self.pos_chess = self.position.chess_position(touch.pos)
            list_of_previous_data = str(self.clicked_input)

            #Get the old data, and save it
            self.chess_position_numerical = str(str(list_of_previous_data[2]) + str(list_of_previous_data[3]))
            self.piece_that_moved = ""
            index = 8
            while index != len(list_of_previous_data) -2:
                self.piece_that_moved += str(list_of_previous_data[index])
                index += 1

            #Checks to see if the user is allowed to move a piece
            if self.turn % 2 != 0:
                #The move the user has done
                move = chess.Move.from_uci("%s" %(str(self.chess_position_numerical) + str(self.pos_chess)))

                #Checks to see if the move is valid
                is_move_valid = chess.Move.from_uci(str(move)) in self.board.legal_moves
                if is_move_valid == True:
                    #Variables check for special moves (Castling and en passant)
                    is_castling = self.board.is_castling(move)
                    king_side_castling = self.board.is_kingside_castling(move)
                    is_en_passant = self.board.is_en_passant(move)

                    #Updates the board
                    self.board.push(move)
                    self.turn += 1

                    try:
                        #This will capture a piece if there is one to capture
                        piece_occupied = str(self.position_piece[str(self.pos_chess)])

                        #Deletes the piece that was captured
                        self.ids[piece_occupied].pos = (1000,1000)
                    except KeyError:
                        #If there is nothing to capture then a KeyError is thrown
                        #But we want to program to continue
                        pass

                    #Executes this code if castling is occuring
                    if is_castling == True:
                        #Checks were the castling is happening, and then moves the correct rook then
                        if king_side_castling == True:
                            if str(str(self.pos_chess)[1]) == str(1):
                                self.ids['Right White Rook'].pos = (conversion.to_number()['f1'][0], conversion.to_number()['f1'][1])
                                position_dic['h1'] = 'None'
                                position_dic['f1'] = 'Right White Rook'
                            else:
                                self.ids['Right Black Rook'].pos = (conversion.to_number()['f8'][0], conversion.to_number()['f8'][1])
                                position_dic['h8'] = 'None'
                                position_dic['f8'] = 'Right Black Rook'
                        else:
                            if str(str(self.pos_chess)[1]) == str(1):
                                self.ids['Left White Rook'].pos = (conversion.to_number()['d1'][0], conversion.to_number()['d1'][1])
                                position_dic['a1'] = 'None'
                                position_dic['d1'] = 'Left White Rook'
                            else:
                                self.ids['Left Black Rook'].pos = (conversion.to_number()['d8'][0], conversion.to_number()['d8'][1])
                                position_dic['a8'] = 'None'
                                position_dic['d8'] = 'Left Black Rook'

                    #If the move is an en passant this code is executed
                    if is_en_passant == True:
                        captured_piece_location = str(str(self.pos_chess)[0]) + str(int(str(self.pos_chess)[1]) - 1)
                        piece_occupied = str(self.position_piece[captured_piece_location])
                        self.ids[piece_occupied].pos = (1000,1000)

                    #Functionality for every move; moving the piece to the correct location and updating the dictionary
                    self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                    position_dic[str(self.chess_position_numerical)] = 'None'
                    position_dic[str(self.pos_chess)] = str(self.piece_that_moved)

                    #Move the Trail
                    self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                    self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])


                else:
                    #Checks to see if a promotion is occuring
                    not_a_promotion = True
                    sc = Scatter_Text_widget()
                    if str(self.pos_chess) == "a8" or str(self.pos_chess) == "b8" or str(self.pos_chess) == "c8" or str(self.pos_chess) == "d8" or str(self.pos_chess) == "e8" or str(self.pos_chess) == "f8" or str(self.pos_chess) == "g8" or str(self.pos_chess) == "h8":
                        if str(self.piece_that_moved)[6] == 'P':
                            if self.piece_that_moved[0] == "W":
                                if int(self.chess_position_numerical[1]) + 1 == int(str(self.pos_chess)[1]):
                                    not_a_promotion = False
                                    #If the piece being promoted is White
                                    #Adds four buttons the user can touch, symbolizing what piece the user will want to promote to
                                    content = Button(id = 'Queen Promotion', background_normal='Visualize_the_Board\Pictures\White_Queen.png', size = (60,60), pos = (410,300))
                                    content1 = Button(id = 'Rook Promotion', background_normal='Visualize_the_Board\Pictures\white_rook.png', size = (60,60), pos = (307.5,400))
                                    content2 = Button(id = 'Bishop Promotion', background_normal='Visualize_the_Board\Pictures\white_Bishop.png', size = (60,60), pos = (307.5,300))
                                    content3 = Button(id = 'Knight Promotion',  background_normal='Visualize_the_Board\Pictures\white_horse.png', size = (60,60), pos = (410,400))

                    elif str(self.pos_chess) == "a1" or str(self.pos_chess) == "b1" or str(self.pos_chess) == "c1" or str(self.pos_chess) == "d1" or str(self.pos_chess) == "e1" or str(self.pos_chess) == "f1" or str(self.pos_chess) == "g1" or str(self.pos_chess) == "h1":
                        if str(self.piece_that_moved)[6] == 'P':
                            if self.piece_that_moved[0] == "B":
                                if int(self.chess_position_numerical[1]) + 1 == int(str(self.pos_chess)[1]):
                                    not_a_promotion = False
                                    #Adds four buttons, but this time in Black, Not white
                                    content = Button(id = 'Queen Promotion', background_normal='Visualize_the_Board\Pictures/black_Queen.png', size = (60,60), pos = (410,300))
                                    content1 = Button(id = 'Rook Promotion', background_normal='Visualize_the_Board\Pictures/black_rook.png', size = (60,60), pos = (307.5,400))
                                    content2 = Button(id = 'Bishop Promotion', background_normal='Visualize_the_Board\Pictures/black_Bishop.png', size = (60,60), pos = (307.5,300))
                                    content3 = Button(id = 'Knight Promotion',  background_normal='Visualize_the_Board\Pictures/black_horse.png', size = (60,60), pos = (410,400))

                    if not_a_promotion == True:
                        #If the move was not valid, then move the piece to the starting position
                        self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                        self.move_worked = False
                    else:
                        self.move_worked = False
                        #Adds a floatlayout to the popup
                        float = FloatLayout()

                        #Adds the buttons the the layout that were just defined based on the color of the promoted piece
                        float.add_widget(content)
                        float.add_widget(content1)
                        float.add_widget(content2)
                        float.add_widget(content3)

                        #Creates the popup, with the FLoatLayout as the content, and moves it to a location the user will not see, so the
                        #popup will not be visable, because the popup does not look aesthetically pleasing
                        popup = Popup(content=float, size_hint=(None, None), size=(120, 160), auto_dismiss=False, pos_hint={'x': 10.0, 'y':10.0})

                        #Binds all of the buttons the the same funtion, and to close the popup
                        content.bind(on_press = self.promotion, on_release=popup.dismiss)
                        content1.bind(on_press = self.promotion, on_release=popup.dismiss)
                        content2.bind(on_press = self.promotion, on_release=popup.dismiss)
                        content3.bind(on_press = self.promotion, on_release=popup.dismiss)

                        #Opens the popup so the GUI will display it
                        popup.open()

                        #Deletes an array of corrdinates
                        del promotion_piece[:]

            else:
                #The player cannot move the black pieces
                self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                self.move_worked = False

            print(self.board)

        else:
            self.move_worked = False

        if self.move_worked == True:
            if self.board.is_game_over(claim_draw=False) == True:
                os.execv(sys.executable, ['python'] + sys.argv)
            #This is were the AI's inputs is visualized
            self.board.BLACK = True

            move_number = random.randint(0, len(list(self.board.legal_moves)) - 1)
            move = list(self.board.legal_moves)[move_number]

            self.board.push(move)
            self.turn += 1
            self.board.BLACK = False

            '''
            What the code does, but in a way for the Algorithm to do:
            self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])

            position_dic[str(self.chess_position_numerical)] = 'None'
            position_dic[str(self.pos_chess)] = str(self.piece_that_moved)
            '''
            try:
                piece_occupied = str(self.position_piece[str(str(move)[2] + str(move)[3])])
                #Deletes the piece that was captured
                self.ids[piece_occupied].pos = (1000,1000)

            except KeyError:
                pass

            #Functionality for every move; moving the piece to the correct location and updating the dictionary
            self.ids[position_dic[str(move)[0] + str(move)[1]]].pos = (conversion.to_number()[str(move)[2] + str(move)[3]][0], conversion.to_number()[str(move)[2] + str(move)[3]][1])

            #The ID of the piece that moved
            piece = position_dic[str(move)[0] + str(move)[1]]

            position_dic[str(str(move)[0] + str(move)[1])] = 'None'
            position_dic[str(str(move)[2] + str(move)[3])] = str(piece)

            #Move the Trail
            self.ids["Trail One"].pos = (conversion.to_number()[str(move)[2] + str(move)[3]][0], conversion.to_number()[str(move)[2] + str(move)[3]][1])
            self.ids["Trail Two"].pos = (conversion.to_number()[str(move)[0] + str(move)[1]][0], conversion.to_number()[str(move)[0] + str(move)[1]][1])

    def promotion(self, obj):
        conversion = convert_coordinates
        number_conversion = conversion_to_number

        #Appends the corrdinates to an array
        promotion_piece.append(obj.pos[0])
        promotion_piece.append(obj.pos[1])

        #'Deletes' the pawn
        self.ids[self.piece_that_moved].pos = (10000,1000)

        #Declare what piece was occupied in the location (If a pawn captures to be promoted)
        piece_occupied = str(self.position_piece[self.pos_chess])

        #If the square was not empty
        if piece_occupied != "None":
            #Delete that piece
            self.ids[piece_occupied].pos = (1000,1000)

        #If the pawn was white
        if self.piece_that_moved[0] == "W":
            if promotion_piece == [410,300]:
                #Turns the pawn into a Queen, Adds the Queen to the dictionary
                self.ids['Whire Queen'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Whire Queen'
                #Move the Trail
                self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=5)
                self.board.push(move)
                self.move_worked = True
                self.turn += 1
            elif promotion_piece == [307.5, 400]:
                #Turns the pawn into a Rook, Adds the Rook to the dictionary
                self.ids['Ledt White Rook'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt White Rook'
                #Move the Trail
                self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=4)
                self.board.push(move)
                self.move_worked = True
                self.turn += 1
            elif promotion_piece == [307.5, 300]:
                #Turns the pawn into a Bishop, Adds the Bishop to the dictionary
                self.ids['Ledt White Bishop'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt White Bishop'
                #Move the Trail
                self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=3)
                self.board.push(move)
                self.move_worked = True
                self.turn += 1
            elif promotion_piece == [410, 400]:
                #Turns the pawn into a Knight, Adds the Knight to the dictionary
                self.ids['Ledt White Knight'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt White Knight'
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=2)
                self.board.push(move)
                self.move_worked = True
                self.turn += 1
        else:
        #If the pawn is BLACK
        #Does the same thing, but changes the color of the piece and the ID of the piece
            if promotion_piece == [410,300]:
                #Turns the pawn into a Queen, Adds the Queen to the dictionary
                self.ids['Block Queen'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Block Queen'
                #Move the Trail
                self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=5)
                self.board.push(move)
                self.move_worked = True
                self.turn += 1
            elif promotion_piece == [307.5, 400]:
                #Turns the pawn into a Rook, Adds the Rook to the dictionary
                self.ids['Ledt Black Rook'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt Black Rook'
                #Move the Trail
                self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=4)
                self.board.push(move)
                self.move_worked = True
                self.turn += 1
            elif promotion_piece == [307.5, 300]:
                #Turns the pawn into a Bishop, Adds the Bishop to the dictionary
                self.ids['Ledt Black Bishop'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt Black Bishop'
                #Move the Trail
                self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=3)
                self.board.push(move)
                self.move_worked = True
                self.turn += 1
            elif promotion_piece == [410, 400]:
                #Turns the pawn into a Knight, Adds the Knight to the dictionary
                self.ids['Ledt Black Knight'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt Black Knight'
                #Move the Trail
                self.ids["Trail One"].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                self.ids["Trail Two"].pos = (conversion.to_number()[self.chess_position_numerical][0], conversion.to_number()[self.chess_position_numerical][1])
                move = chess.Move(number_conversion[str(self.chess_position_numerical)] - 1, number_conversion[str(self.pos_chess)] - 1, promotion=2)
                self.board.push(move)
                self.turn += 1
                self.move_worked = True

        if self.move_worked == True:
            #the AI can now move
            self.board.BLACK = True

            move_number = random.randint(0, len(list(self.board.legal_moves)) - 1)
            move = list(self.board.legal_moves)[move_number]

            self.board.push(move)
            self.turn += 1
            self.board.BLACK = False

            '''
            What the code does, but in a way for the Algorithm to do:
            self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])

            position_dic[str(self.chess_position_numerical)] = 'None'
            position_dic[str(self.pos_chess)] = str(self.piece_that_moved)
            '''

            try:
                piece_occupied = str(self.position_piece[str(str(move)[2] + str(move)[3])])
                #Deletes the piece that was captured
                self.ids[piece_occupied].pos = (1000,1000)

            except KeyError:
                pass
            #Functionality for every move; moving the piece to the correct location and updating the dictionary
            self.ids[position_dic[str(move)[0] + str(move)[1]]].pos = (conversion.to_number()[str(move)[2] + str(move)[3]][0], conversion.to_number()[str(move)[2] + str(move)[3]][1])

            #The ID of the piece that moved
            piece = position_dic[str(move)[0] + str(move)[1]]

            position_dic[str(str(move)[0] + str(move)[1])] = 'None'
            position_dic[str(str(move)[2] + str(move)[3])] = str(piece)

            #Move the Trail
            self.ids["Trail One"].pos = (conversion.to_number()[str(move)[2] + str(move)[3]][0], conversion.to_number()[str(move)[2] + str(move)[3]][1])
            self.ids["Trail Two"].pos = (conversion.to_number()[str(move)[0] + str(move)[1]][0], conversion.to_number()[str(move)[0] + str(move)[1]][1])

#Builds the App
class window(App):
    def build(self):
        return Scatter_Text_widget()
