def rule_of_data():
    print('      ')
    print('!! Considerate the next rules when you tried to introduce the data:')
    print('-> Data only can be positive integers over 0, except the quantity of obstacles (it can be 0).')
    print('-> The limit value of board is 10^5 squares in each side(row and column).')
    print('-> You can´t put a obstacle in the position´s queen.')
    print('-> A single cell may contain more than one obstacle.')
    print('-> Queen´s position and obstacles´ position cannot put in out of board´s dimensions.')
    print('-> The correct way for introduce two elements is separate these only with one space and not begin the first number with a space.')
    
def confirm_data(data):
    B = list(data)
    i = 0
    n = []
    numeros = [] 

    while i < len(B):
        if (not(B[i] == ' ')):
            n.append(B[i])
            i = i + 1
        else:
            try:
                e = 0
                nu = ' '
                while e < len(n):
                    nu = f'{nu}{n[e]}'
                    e = e + 1
                numero = int(nu)
                numeros.append(numero)
                n.clear()
                i = i + 1
            except ValueError:
                break 
    try:
        e = 0
        nu = ' '
        while e < len(n):
            nu = f'{nu}{n[e]}'
            e = e + 1
        numero = int(nu)
        numeros.append(numero)
        if (not(len(numeros) == 2)) :
            return False
    
    except ValueError:
        return False
     
    return numeros

def ask_board_obstacle():
    rule_of_data()
    print('   ')
    B_O = input('PLease, introduce the dimesion of board (first value, rows = columns) and the number of obstacles (second value), separate the data with a space: ')
    b_o = confirm_data(B_O)
    try:
        if b_o[0] > 1000000 or b_o[0] <= 0 or b_o[1] < 0 :
            b_o = False
    except TypeError:
        b_o = confirm_data(B_O)
    while b_o == False:
        rule_of_data()
        print('   ')
        print('** ALERT!!: Data were not introduced for correct way, watch the rules and try again. **')
        B_O = input('PLease, introduce the dimesion of board (first value, rows = columns) and the number of obstacles (second value), separate the data with a space: ')
        b_o = confirm_data(B_O)
        try:
            if b_o[0] > 1000000 or b_o[0] <= 0 or b_o[1] < 0 :
                 b_o = False
        except TypeError:
            b_o = confirm_data(B_O)
    return b_o

def ask_queen_position(board):
    print('  ')
    Rq_Cq = input('PLease, introduce the queen´s position (frist value: row, second value: column): ')
    rq_cq = confirm_data(Rq_Cq)
    try:
        if rq_cq[0] > board or rq_cq[1] > board or rq_cq[0] <= 0 or rq_cq[1] <= 0 :
            rq_cq = False
    except TypeError:
        rq_cq = confirm_data(Rq_Cq)
    while rq_cq == False:
        rule_of_data()
        print('   ')
        print('** ALERT!!: Data were not introduced for correct way, watch the rules and try again. **')
        Rq_Cq = input('PLease, introduce the queen´s position (frist value: row, second value: column): ')
        rq_cq = confirm_data(Rq_Cq)
        try:
            if rq_cq[0] > board or rq_cq[1] > board or rq_cq[0] <= 0 or rq_cq[1] <= 0 :
                 rq_cq = False
        except TypeError:
             rq_cq = confirm_data(Rq_Cq)
    return rq_cq

def obstacles(n_ob, q_p, board):
    obstacle_list = []
    i = 0
    while i < n_ob:
        print('  ')
        obs = input(f'Introduce the obstacle number {i+1} (frist value: row, second value: column)')
        data = confirm_data(obs)
        try:
            if data[0] > board or data[1] > board or data[0] <= 0 or data[1] <= 0 or data == q_p :
                data = False
        except TypeError:
            data = confirm_data(obs)
        while data == False:
            rule_of_data()
            print('  ')
            print('** ALERT!!: Data were not introduced for correct way, watch the rules and try again. **')
            obs = input(f'Introduce the obstacle number {i+1} (frist value: row, second value: column): ')
            data = confirm_data(obs)
            try:
                if data[0] > board or data[1] > board or data[0] <= 0 or data[1] <= 0 or data == q_p :
                    data = False
            except TypeError:
                data = confirm_data(obs)
        obstacle_list.append(data)
        i = i + 1
    return obstacle_list


