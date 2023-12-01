"""
finir deplacements roi
"""

from turtle import*
import ast

ChessBoard = []
ChessBoardOrganization = [["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"],
                          ["Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]]
color_turn = 'white'

from_white = '()'
to_white = '()'

from_black = '()'
to_black = '()'



def get_from_piece(chess_board, case, color) :
    for i in range(8) :
        for j in range(8) :
            if chess_board[i][j] != "empty" :
                if color == chess_board[i][j].color :
                    if chess_board[i][j].position == ast.literal_eval(case) :
                        return chess_board[i][j]

    return 'Invalid case'

def is_right_to_case(chess_board, case, picked_piece) :
    if not(picked_piece == 'Invalid case') :
    
        if (picked_piece.piece == "rook" and ast.literal_eval(case) in picked_piece.get_available_straight_mooves(chess_board)['available positions']) or (picked_piece.piece == "knight" and ast.literal_eval(case) in picked_piece.get_available_knight_mooves(chess_board)['available positions']) or (picked_piece.piece == "bishop" and ast.literal_eval(case) in picked_piece.get_available_diagonal_mooves(chess_board)['available positions']) or (picked_piece.piece == "queen" and (ast.literal_eval(case) in picked_piece.get_available_straight_mooves(chess_board) or ast.literal_eval(case) in picked_piece.get_available_diagonal_mooves(chess_board))) or (picked_piece.piece == "king" and ast.literal_eval(case) in picked_piece.get_available_mooves(chess_board)) or (picked_piece.piece == "pawn" and (ast.literal_eval(case) in picked_piece.get_available_mooves(chess_board)['available straight mooves'] or ast.literal_eval(case) in picked_piece.get_available_mooves(chess_board)['available diagonal mooves'])) :   

            return True

    return False

def pick_color_turn(last_color_turn) :
    if last_color_turn == 'white' :
        return 'black'
    return 'white'

def get_case_status(chess_board, pos) :
    if pos[0] > 7 or pos[1] > 7 or pos[0] < 0 or pos[1] < 0:
        return "case out of range"
    
    if chess_board[pos[0]][pos[1]] == "empty" :
        return "empty"

    return chess_board[pos[0]][pos[1]].color
    

class Piece () :
    def __init__ (self) :
        self.position = ()
        self.color = ""
        self.piece = ""

class Rook(Piece) :
    def __init__ (self) :
        super().__init__()
            
    def get_available_straight_mooves(self, chess_board) :
        available_positions = []
        protected_pieces = []

        
        for i in range(self.position[1]+1, 8) :
            x,y = self.position[0],i
            
            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break
                
        for i in range(self.position[0]+1, 8) :
            x,y = i, self.position[1]
            
            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break

        for i in range(0,self.position[1]) :
            x,y = self.position[0], self.position[1]-1-i
            
            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break
                
        for i in range(0,self.position[0]) :
            x,y = self.position[0]-1-i, self.position[1]
            
            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break

        return {'available positions' : available_positions,
                'protected pieces' :protected_pieces}

class Knight(Piece) :
    def __init__ (self) :
        super().__init__()
        
    def get_available_knight_mooves(self,chess_board) :
        available_positions = []
        possible_positions = [(self.position[0]+2,self.position[1]+1), (self.position[0]+2,self.position[1]-1), (self.position[0]-2,self.position[1]+1),
                             (self.position[0]-2,self.position[1]-1), (self.position[0]+1,self.position[1]+2), (self.position[0]+1,self.position[1]-2),
                             (self.position[0]-1,self.position[1]+2), (self.position[0]-1,self.position[1]-2)]
        protected_pieces = []


        for possible_position in possible_positions :
            if get_case_status(chess_board,possible_position) != "case out of range" :
                if get_case_status(chess_board,possible_position) == "empty" or get_case_status(chess_board,possible_position) != self.color :
                    available_positions.append(possible_position)

                if get_case_status(chess_board,possible_position) == self.color :
                    protected_pieces.append(possible_position)
                                                                                                                         
        return {'available positions' : available_positions,
                'protected pieces' :protected_pieces}


class Bishop(Piece) :
    def __init__ (self) :
        super().__init__()
    
    def get_available_diagonal_mooves(self, chess_board) :
        available_positions = []
        protected_pieces = []

        for i in range(7-self.position[1]) :
            

            x, y = self.position[0]+i+1, self.position[1]+i+1

            if x > 7 :
                break

            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break

        for i in range(7-self.position[1]) :

            x, y = self.position[0]-i-1, self.position[1]+i+1

            if x < 0 :
                break

            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break

        for i in range(self.position[1]) :

            x, y = self.position[0]-i-1, self.position[1]-i-1
            
            if x < 0 :
                break

            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break

        for i in range(self.position[1]-1) :

            x, y = self.position[0]+i+1, self.position[1]-i-1
            
            if x > 7 :
                break
            
            
            


            if get_case_status(chess_board,(x,y)) == "empty" :
                available_positions.append((x, y))

            if get_case_status(chess_board,(x,y)) != "empty" :
                if get_case_status(chess_board,(x,y)) == self.color :
                    protected_pieces.append((x,y))
                    break
                
                if get_case_status(chess_board,(x,y)) != self.color :
                    available_positions.append((x, y))
                    break

        return {'available positions' : available_positions,
                'protected pieces' :protected_pieces}

class Queen(Rook, Bishop) :
    def __init__ (self) :
        super().__init__()

class King(Piece) :
    def __init__ (self) :
        super().__init__()



    def get_protected_positions_opposite_color (self, chess_board) :
        
        for i in range (8) :
            for j in range(8) :
                if chess_board[i][j] != "empty" :
                    if chess_board[i][j].color != self.color :
                        
                        if chess_board[i][j].piece == "rook" :
                            for pos in chess_board[i][j].get_available_straight_mooves(chess_board)['available positions'] :
                                protected_positions_opposite_color.append(pos)

                            for pos in chess_board[i][j].get_available_straight_mooves(chess_board)['protected pieces'] :
                                protected_positions_opposite_color.append(pos)

                        if chess_board[i][j].piece == "knight" :
                            for pos in chess_board[i][j].get_available_knight_mooves(chess_board)['available positions'] :
                                protected_positions_opposite_color.append(pos)

                            for pos in chess_board[i][j].get_available_knight_mooves(chess_board)['protected pieces'] :
                                protected_positions_opposite_color.append(pos)
                        
                        if chess_board[i][j].piece == "bishop" :
                            for pos in chess_board[i][j].get_available_diagonal_mooves(chess_board)['available positions'] :
                                protected_positions_opposite_color.append(pos)

                            for pos in chess_board[i][j].get_available_diagonal_mooves(chess_board)['protected pieces'] :
                                protected_positions_opposite_color.append(pos)

                        if chess_board[i][j].piece == "queen" :
                            for pos in chess_board[i][j].get_available_straight_mooves(chess_board)['available positions'] :
                                protected_positions_opposite_color.append(pos)

                            for pos in chess_board[i][j].get_available_straight_mooves(chess_board)['protected pieces'] :
                                protected_positions_opposite_color.append(pos)

                            for pos in chess_board[i][j].get_available_diagonal_mooves(chess_board)['available positions'] :
                                protected_positions_opposite_color.append(pos)

                            for pos in chess_board[i][j].get_available_diagonal_mooves(chess_board)['protected pieces'] :
                                protected_positions_opposite_color.append(pos)

                        if chess_board[i][j].piece == "pawn" :
                            for pos in chess_board[i][j].get_available_mooves(chess_board)['diagonal empty positions'] :
                                protected_positions_opposite_color.append(pos)

                            for pos in chess_board[i][j].get_available_mooves(chess_board)['protected pieces'] :
                                protected_positions_opposite_color.append(pos)

                        if chess_board[i][j].piece == "king" :
                            possible_positions = [(chess_board[i][j].position[0]+1, chess_board[i][j].position[1]), (chess_board[i][j].position[0]+1, chess_board[i][j].position[1]+1), (chess_board[i][j].position[0]+1, chess_board[i][j].position[1]-1),
                              (chess_board[i][j].position[0]-1, chess_board[i][j].position[1]), (chess_board[i][j].position[0]-1, chess_board[i][j].position[1]+1), (chess_board[i][j].position[0]-1, chess_board[i][j].position[1]-1),
                              (chess_board[i][j].position[0], chess_board[i][j].position[1]+1), (chess_board[i][j].position[0], chess_board[i][j].position[1]-1)]

                            for pos in possible_positions :
                                protected_positions_opposite_color.append(pos)
                            
        return protected_positions_opposite_color

    def get_available_mooves(self,chess_board) :
        """ unended func """
        available_positions = []
        possible_positions = [(self.position[0]+1, self.position[1]), (self.position[0]+1, self.position[1]+1), (self.position[0]+1, self.position[1]-1),
                              (self.position[0]-1, self.position[1]), (self.position[0]-1, self.position[1]+1), (self.position[0]-1, self.position[1]-1),
                              (self.position[0], self.position[1]+1), (self.position[0], self.position[1]-1)]

        for possible_position in possible_positions :
            if not(possible_position in get_protected_positions_opposite_color(chess_board)) and get_case_status(chess_board, possible_position) != self.color :
                available_positions.append(possible_position)
                
        return available_positions

    def is_being_check(self,chess_board) :
        if self.position in self.get_protected_positions_opposite_color(chess_board) :
            return True
        
        return False

    def is_being_checkmate(self,chess_board) :
        if self.is_being_check(chess_board) and self.get_available_mooves(chess_board) == [] :
            return True

        return False
        
                            

class Pawn(Piece) :
    def __init__ (self) :
        super().__init__()
        self.first_moove = 1

    def get_available_mooves(self,chess_board) :
        available_straight_mooves = []
        available_diagonal_mooves = []
        diagonal_empty_positions = []
        protected_pieces = []
        

        if self.color == "white" :
            if get_case_status(chess_board,(self.position[0]+1,self.position[1])) == "empty" :
                available_straight_mooves.append((self.position[0]+1,self.position[1]))

                if self.first_moove :
                    if get_case_status(chess_board,(self.position[0]+2,self.position[1])) == "empty" :
                        available_straight_mooves.append((self.position[0]+2,self.position[1]))

            if get_case_status(chess_board,(self.position[0]+1,self.position[1]+1)) != "case out of range"  :
                if get_case_status(chess_board,(self.position[0]+1,self.position[1]+1)) != "empty" :
                    if get_case_status(chess_board,(self.position[0]+1,self.position[1]+1)) != self.color :
                        available_diagonal_mooves.append((self.position[0]+1,self.position[1]+1))

                    if get_case_status(chess_board,(self.position[0]+1,self.position[1]+1)) == self.color :
                        protected_pieces.append((self.position[0]+1,self.position[1]+1))
                    

                if get_case_status(chess_board,(self.position[0]+1,self.position[1]+1)) == "empty" :
                    diagonal_empty_positions.append((self.position[0]+1,self.position[1]+1))

            if get_case_status(chess_board,(self.position[0]+1,self.position[1]-1)) != "case out of range" :
                if get_case_status(chess_board,(self.position[0]+1,self.position[1]-1)) != "empty" :
                    if get_case_status(chess_board,(self.position[0]+1,self.position[1]-1)) != self.color :
                        available_diagonal_mooves.append((self.position[0]+1,self.position[1]-1))

                    if get_case_status(chess_board,(self.position[0]+1,self.position[1]+1)) == self.color :
                        protected_pieces.append((self.position[0]+1,self.position[1]-1))

                if get_case_status(chess_board,(self.position[0]+1,self.position[1]-1)) == "empty" :
                    diagonal_empty_positions.append((self.position[0]+1,self.position[1]-1))


        if self.color == "black" :
            if get_case_status(chess_board,(self.position[0]-1,self.position[1])) == "empty" :
                available_straight_mooves.append((self.position[0]-1,self.position[1]))

                if self.first_moove :
                    if get_case_status(chess_board,(self.position[0]-2,self.position[1])) == "empty" :
                        available_straight_mooves.append((self.position[0]-2,self.position[1]))

            if get_case_status(chess_board,(self.position[0]-1,self.position[1]+1)) != "case out of range" :
                if get_case_status(chess_board,(self.position[0]-1,self.position[1]+1)) != "empty" :
                    if get_case_status(chess_board,(self.position[0]-1,self.position[1]+1)) != self.color :
                        available_diagonal_mooves.append((self.position[0]-1,self.position[1]+1))

                    if get_case_status(chess_board,(self.position[0]-1,self.position[1]+1)) == self.color :
                        protected_pieces.append((self.position[0]-1,self.position[1]+1))

                if get_case_status(chess_board,(self.position[0]-1,self.position[1]+1)) == "empty" :
                    diagonal_empty_positions.append((self.position[0]-1,self.position[1]+1))

            if get_case_status(chess_board,(self.position[0]-1,self.position[1]-1)) != "case out of range" :
                if get_case_status(chess_board,(self.position[0]-1,self.position[1]-1)) != "empty":
                    if get_case_status(chess_board,(self.position[0]-1,self.position[1]-1)) != self.color :
                        available_diagonal_mooves.append((self.position[0]-1,self.position[1]-1))

                    if get_case_status(chess_board,(self.position[0]-1,self.position[1]-1)) == self.color :
                        protected_pieces.append((self.position[0]-1,self.position[1]-1))

                        

                if get_case_status(chess_board,(self.position[0]-1,self.position[1]-1)) == "empty":
                    diagonal_empty_positions.append((self.position[0]-1,self.position[1]-1))
            
            
        return {'available straight mooves' : available_straight_mooves,
                'available diagonal mooves' : available_diagonal_mooves,
                'diagonal empty positions' : diagonal_empty_positions,
                'protected pieces' : protected_pieces
                }

    

for i in range(8) :
    ChessBoard.append([])
    for j in range(8) :
        if i == 0 or i == 1 or i == 6 or i == 7 :
           
            if i == 0 or i == 7 :
                if j == 0 or j == 7 :
                    ChessBoard[-1].append(Rook())
                    ChessBoard[-1][-1].piece = "rook"

                if j == 1 or j == 6 :
                    ChessBoard[-1].append(Knight())
                    ChessBoard[-1][-1].piece = "knight"

                if j == 2 or j == 5 :
                    ChessBoard[-1].append(Bishop())
                    ChessBoard[-1][-1].piece = "bishop"

                if j == 3 :
                    ChessBoard[-1].append(Queen())
                    ChessBoard[-1][-1].piece = "queen"

                if j == 4 :
                    ChessBoard[-1].append(King())
                    ChessBoard[-1][-1].piece = "king"

            if i == 1 or i == 6 :
                ChessBoard[-1].append(Pawn())
                ChessBoard[-1][-1].piece = "pawn"
                    
            ChessBoard[-1][-1].position = (i,j)
            
            if i == 0 or i == 1 :
                ChessBoard[-1][-1].color = "white"

            if i == 6 or i == 7 :
                ChessBoard[-1][-1].color = "black"
            

        else :
            ChessBoard[-1].append("empty")
            
chess_board_size = 50
chess_board_pos = (-170, 170)

speed(5000)


while 1 :
    clear()

    width(1)
    
    penup()
    goto(chess_board_pos)
    pendown()
    


    for i in range(9) :
        fd(8*chess_board_size)
        penup()
        goto(chess_board_pos[0], chess_board_pos[1] - (i+1)*chess_board_size)
        pendown()
        
    right(90)

    penup()
    goto(chess_board_pos)
    pendown()

    for i in range(9) :
        fd(8*chess_board_size)
        penup()
        goto(chess_board_pos[0]+ (i+1)*chess_board_size, chess_board_pos[1] )
        pendown()

    width(3)
    
    for i in range(8) :
        for j in range(8) :
            piece = ChessBoard[i][j]
            if piece != "empty" :
                if piece.color == "white" :
                    color('yellow')

                if piece.color == "black" :
                    color('black')

                
                penup()
                goto(chess_board_pos[0] + piece.position[0]*chess_board_size, (chess_board_pos[1] -piece.position[1]*chess_board_size)-25)
                pendown()
                circle(25)

    

    left(90)

    if color_turn == 'white' :
        print("--- White's turn ---")

        while not(is_right_to_case(ChessBoard, to_white, get_from_piece(ChessBoard, from_white, color_turn))) :
            from_white = input('From :')
            to_white = input('To :')


        ChessBoard[ast.literal_eval(to_white)[0]][ast.literal_eval(to_white)[1]] = get_from_piece(ChessBoard, from_white, color_turn)
        get_from_piece(ChessBoard, from_white, color_turn).position = ast.literal_eval(to_white)
        ChessBoard[ast.literal_eval(from_white)[0]][ast.literal_eval(from_white)[1]] = "empty"

    if color_turn == 'black' :
        print("--- Black's turn ---")

        while not(is_right_to_case(ChessBoard, to_black, get_from_piece(ChessBoard, from_black, color_turn))) :
            from_black = input('From :')
            to_black = input('To :')


        ChessBoard[ast.literal_eval(to_black)[0]][ast.literal_eval(to_black)[1]] = get_from_piece(ChessBoard, from_black, color_turn)
        get_from_piece(ChessBoard, from_black, color_turn).position = ast.literal_eval(to_black)
        ChessBoard[ast.literal_eval(from_black)[0]][ast.literal_eval(from_black)[1]] = "empty"
                

    color_turn = pick_color_turn(color_turn)

    
            
            
    




    
