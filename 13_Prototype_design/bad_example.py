class ChessPiece:
    def __init__(self, name, position, color):
        self.name=name
        self.position=position
        self.color=color

    def display(self):
        return f"{self.name} at {self.position} ({self.color})"
    
class ChessBoard:
    def __init__(self):
        self.pieces=[]
    
    def add_piece(self, piece: ChessPiece):
        self.pieces.append(piece)
    
    def display_board(self):
        for piece in self.pieces:
            print(piece.display())

piece1=ChessPiece("King", "E1", "White")
piece2=ChessPiece("Queen", "D1", "White")
piece3=ChessPiece("Rook", "A1", "White")

board1=ChessBoard()
board1.add_piece(piece1)
board1.add_piece(piece2)
board1.add_piece(piece3)

board1.display_board()

board2=ChessBoard()
board2.add_piece(piece1.clone())
board2.add_piece(piece2.clone())
board2.add_piece(piece3.clone())

board2.display_board()
