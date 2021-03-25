import random

YELLOW_TIME = 6
TOTAL_HOLD = 12
sigma = 20
alpha = 2
taw = 7


class Agent:

    def __init__(self):
        self.time_counter = 0
        self.prev_state = None
        self.curr_state = None
        self.prev_action = None
        self.action = None
        self.prev_action_was_flip = False

    def select_action(self, state):

        if self.action == None:
            self.action = state[0]
        
        self.curr_state = self.handle_faulty_sensors(state)
        
        #print('##################################### state:', state)

        self.time_counter += 1

        if self.time_counter >= taw:
            self.action = self.act(self.curr_state)
            if self.prev_action != self.action:
                self.time_counter = 0
            
        self.prev_state = self.curr_state
        self.prev_action_was_flip = True if self.prev_action != None and self.prev_action != self.action else False
        self.prev_action = self.action


        return self.action


    def act(self, state):

        N = state[1] + (sigma * state[5])
        S = state[2] + (sigma * state[6])
        E = state[3] + (sigma * state[7])
        W = state[4] + (sigma * state[8])

        lane_weights = [N, E, S, W]

        if not any(lane_weights):
            return self.action

        action = lane_weights.index(max(lane_weights))
        #print('************************************ action:', action)

        return action
    
    def handle_faulty_sensors(self, state):

        for i in range(1, 9):
            if state[i] == -1:
                if (i in [1, 5] and state[0] == 0) \
                or (i in [2, 6] and state[0] == 2) \
                or (i in [3, 7] and state[0] == 1) \
                or (i in [4, 8] and state[0] == 3):
                    state[i] = 0

        for i in range(1, 9):
            if state[i] == -1 and self.prev_state != None:
                state[i] = self.prev_state[i] + 6 + 6 * int(self.prev_action_was_flip) if self.prev_state[i] != 0 else -1
            if state[i] == -1:
                state[i] = 0 if i >= 5 or state[i + 4] == 0 else state[i + 4] + alpha

        return state