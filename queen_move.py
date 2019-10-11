
def up_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[0]
    while i < b :
        e = 0
        q_position[0] = (q_position[0]+1)
        while e < len(obs):
            if q_position == obs[e]:
                i = b
            e = e + 1
        if (not(i == b)):
            m = m + 1
        i = i + 1
    return m

def down_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[0]
    while i > 1 :
        e = 0
        q_position[0] = (q_position[0]-1)
        while e < len(obs):
            if q_position == obs[e] :
                i = 1
            e = e + 1
        if (not(i == 1)):
            m = m + 1
        i = i - 1
    return m

def rigth_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[1]
    while i < b :
        e = 0
        q_position[1] = (q_position[1]+1)
        while e < len(obs):
            if q_position == obs[e]:
                i = b
            e = e + 1
        if (not(i == b)):
            m = m + 1
        i = i + 1
    return m

def left_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[1]
    while i > 1 :
        e = 0
        q_position[1] = (q_position[1]-1)
        while e < len(obs):
            if q_position == obs[e] :
                i = 1
            e = e + 1
        if (not(i == 1)):
            m = m + 1
        i = i - 1
    return m

def up_rigth_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[0]
    c = q_p[1]
    while i < b and c < b :
        e = 0
        q_position[0] = (q_position[0]+1)
        q_position[1] = (q_position[1]+1)
        while e < len(obs):
            if q_position == obs[e]:
                i = b
                c = b
            e = e + 1
        if (not(i == b or c == b)):
            m = m + 1
        i = i + 1
        c = c + 1 
    return m

def up_left_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[0]
    c = q_p[1]
    while i < b and c > 1 :
        e = 0
        q_position[0] = (q_position[0]+1)
        q_position[1] = (q_position[1]-1)
        while e < len(obs):
            if q_position == obs[e]:
                i = b
                c = 1
            e = e + 1
        if (not(i == b or c == 1)):
            m = m + 1
        i = i + 1
        c = c - 1 
    return m

def down_left_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[0]
    c = q_p[1]
    while i > 1 and c > 1 :
        e = 0
        q_position[0] = (q_position[0]-1)
        q_position[1] = (q_position[1]-1)
        while e < len(obs):
            if q_position == obs[e]:
                i = 1
                c = 1
            e = e + 1
        if (not(i == 1 or c == 1)):
            m = m + 1
        i = i - 1
        c = c - 1 
    return m

def down_rigth_move(b, q_p, obs):
    q_position = list(q_p)
    m = 0
    i = q_p[0]
    c = q_p[1]
    while i > 1 and c < b :
        e = 0
        q_position[0] = (q_position[0]-1)
        q_position[1] = (q_position[1]+1)
        while e < len(obs):
            if q_position == obs[e]:
                i = 1
                c = b
            e = e + 1
        if (not(i == 1 or c == b)):
            m = m + 1
        i = i - 1
        c = c + 1 
    return m

