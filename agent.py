import random

YELLOW_TIME = 6
TOTAL_HOLD = 12
omega = 15
sigma = 20
taw = 3
zeta = 5

class Agent:
    def __init__(self):
        self.time_counter = 0
        self.prev_state = [0] * 9
        self.curr_state = None
        self.prev_action = None
        self.action = None
        self.prev_action_was_flip = False
        self.prev_state_was_zero = True
        self.taw = 1
        self.sigma = 20

    def select_action(self, state):

        if self.action == None:
            self.action = state[0]
        
        self.time_counter += 1

        self.curr_state = self.handle_faulty_sensors(state)
        print(self.curr_state)
        
        if (self.prev_state[1:9] == [0] * 8):
            self.prev_state_was_zero = True
        else:
            self.prev_state_was_zero = False

        if self.prev_state_was_zero:
            self.action = self.act(self.curr_state)
            self.time_counter = 0

        '''single_wt = self.is_single_wt(self.curr_state)
        if single_wt:
            self.action = self.act(self.curr_state) '''
        
        #max_close = self.max_close(self.curr_state)

        if self.time_counter >= self.taw:
        #if max_close > omega:
            self.action = self.act(self.curr_state)
            self.time_counter = 0

        self.prev_state = self.curr_state
        self.prev_action_was_flip = True if self.prev_action != self.action else False
        self.prev_action = self.action

        print('__________', self.action, '__________')
        return self.action

    def act(self, state):

        N = state[1] + (self.sigma * state[5])
        S = state[2] + (self.sigma * state[6])
        E = state[3] + (self.sigma * state[7])
        W = state[4] + (self.sigma * state[8])

        lane_weights = [N, E, S, W]

        if not any(lane_weights):
            return self.action

        action = lane_weights.index(max(lane_weights))
        if (action == 0 and state[5] == 0) \
                or (action == 1 and state[7] == 0) \
                or (action == 2 and state[6] == 0) \
                or (action == 3 and state[8] == 0):
            self.taw = 4
        else:
            self.taw = 7


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
            if state[i] == -1:
                if i >= 5 and state[i - 4] == 0:
                    state[i] = 0
                elif i >= 5 and state[i - 4] != 0 and self.prev_state[i] == 0:
                    state[i] = 6 if int(self.prev_action_was_flip) else 3
                elif i < 5 and self.prev_state[i] == 0:
                    state[i] = 0
                elif self.prev_state[i] != 0:
                    state[i] = self.prev_state[i] + 6 + 6 * int(self.prev_action_was_flip)

        return state

    def max_close(self, state):
        close_detectors = state[1:5]
        return max(close_detectors)

    def is_single_wt(self, state):
        ## Checks if there is only one lane with wait time out the closed three
        lanes = state[1:5]
        has_wt = 0
        for lane in lanes:
            if lane > 0:
                has_wt += 1
        return has_wt == 1


'''
class Ahmed:

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

        #print(self.curr_state)

        single_wt = self.is_single_wt(self.curr_state)

        self.time_counter += 1

        if self.time_counter == zeta and single_wt:
            self.time_counter = 0
            self.action = self.act(self.curr_state)

        if self.time_counter >= taw:
            self.action = self.act(self.curr_state)
            if self.prev_action != self.action:
                self.time_counter = 0

        self.prev_state = self.curr_state
        self.prev_action_was_flip = True if self.prev_action != None and self.prev_action != self.action else False
        self.prev_action = self.action

        #print('__________', self.action, '__________')
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
            if state[i] == -1 and self.prev_state == None:
                state[i] = 0
            if state[i] == -1 and self.prev_state != None:
                if i >= 5 and state[i - 4] == 0:
                    state[i] = 0
                elif i >= 5 and state[i - 4] != 0 and self.prev_state[i] == 0:
                    state[i] = 6 if int(self.prev_action_was_flip) else 3
                elif i < 5 and self.prev_state[i] == 0:
                    state[i] = 0
                elif self.prev_state[i] != 0:
                    state[i] = self.prev_state[i] + 6 + 6 * int(self.prev_action_was_flip)

        return state
    
    def max_close(self, state):
        close_detectors = state[1:5]
        return max(close_detectors)

    def is_single_wt(self, state):
        ## Checks if there is only one lane with wait time out the closed three
        lanes = state[1:5]
        has_wt = 0
        for lane in lanes:
            if lane > 0:
                has_wt += 1
        return has_wt == 1
'''
