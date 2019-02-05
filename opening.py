import chess
import chess.polyglot

def get_moves_from_opening(board_fen):
	board = chess.Board(str(board_fen))

	print (board)

	with chess.polyglot.open_reader("opening-books/DCbook_large.bin") as reader:
		try:
			for entry in reader.find_all(board):
				print (entry.move(), entry.weight, entry.learn)
			print ("The chosen next move is " + str(next(reader.find_all(board)).move()))

			nextMove = str(next(reader.find_all(board)).move())

		except StopIteration:
			return None
		
		return nextMove

print (get_moves_from_opening('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'))