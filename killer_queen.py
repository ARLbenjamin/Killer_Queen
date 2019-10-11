import ask_data
import queen_move

# Take data

board_obstcle = ask_data.ask_board_obstacle()
queen_position = ask_data.ask_queen_position(board_obstcle[0])
queen_position_tuple = tuple(queen_position)
obstacles_positions = ask_data.obstacles(board_obstcle[1], queen_position, board_obstcle[0])


# Evaluating queen´s move

queen_up = queen_move.up_move(board_obstcle[0], queen_position_tuple, obstacles_positions)
queen_donw = queen_move.down_move(board_obstcle[0], queen_position_tuple, obstacles_positions)
queen_rigth = queen_move.rigth_move(board_obstcle[0], queen_position_tuple, obstacles_positions)
queen_left = queen_move.left_move(board_obstcle[0], queen_position_tuple, obstacles_positions)
queen_up_rigth = queen_move.up_rigth_move(board_obstcle[0], queen_position_tuple, obstacles_positions)
queen_up_left = queen_move.up_left_move(board_obstcle[0], queen_position_tuple, obstacles_positions)
queen_down_left = queen_move.down_left_move(board_obstcle[0], queen_position_tuple, obstacles_positions)
queen_down_rigth = queen_move.down_rigth_move(board_obstcle[0], queen_position_tuple, obstacles_positions)

# Calculating numbers of movements and show answer

total_move =  queen_up + queen_donw + queen_rigth + queen_left + queen_up_rigth + queen_up_left + queen_down_left + queen_down_rigth

print('   ')
print('With your´d contidions:')
print(f'-> The dimention of cheessboard is {board_obstcle[0]} X {board_obstcle[0]}')
print(f'-> The queen´s position is ({queen_position[0]}, {queen_position[1]})')
print(f'-> There is/are {len(obstacles_positions)} obstacle(s) with specific(s) position(s)')
print('------------------------------------------------------')
print(f'--> The queen can move for {total_move} square(s) <--')
print('------------------------------------------------------')
