def get_hangman_states(game_mode):
    states =['''
    +---------+
    |         :
    |         
    |        
    |        
    |         
    ================
    ''','''
    +---------+
    |         :
    |         O
    |        
    |        
    |         
    ================
    ''','''
    +---------+
    |         :
    |         O
    |         |
    |        
    |         
    ================
    ''','''
    +---------+
    |         :
    |         O
    |        /|
    |        
    |         
    ================
    ''',r'''
    +---------+
    |         :
    |         O
    |        /|\
    |        
    |         
    ================
    ''',r'''
    +---------+
    |         :
    |         O
    |        /|\
    |        / 
    |         
    ================
    ''', r'''
    +---------+
    |         :
    |         O
    |        /|\
    |        / \
    |         
    ================
    ''' ]

    if game_mode == "long":
        return states
    else:
        game_states = states[:3]
        game_states.append(states[4])
        game_states.append(states[6])
        return game_states
    
    