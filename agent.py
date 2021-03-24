import random

YELLOW_TIME = 6
TOTAL_HOLD = 12
sigma = 3
alpha = 2
taw = 7


class Agent:

    def __init__(self):
        self.action = None
        self.time_counter = 0

    def select_action(self, state):

        if self.action == None:
            self.action = state[0]
        
        for i in range(1, 9):
            if state[i] == -1:
                state[i] = 0 if i >=5 or state[i + 4] == 0 else state[i + 4] + alpha
        
        #print('##################################### state:', state)

        self.time_counter += 1

        if self.time_counter == taw:
            self.action = self.act(state)
            self.time_counter = 0
        
        return self.action


    def act(self, state):

        N = state[1] + (sigma * state[5])
        S = state[2] + (sigma * state[6])
        E = state[3] + (sigma * state[7])
        W = state[4] + (sigma * state[8])

        lane_weights = [N, E, S, W]
        action = lane_weights.index(max(lane_weights))
        #print('************************************ action:', action)
        return action


    '''
    def get_busy(state):
        for i in range(1, 9):
            if state[i] == -1:
                state[i] = 0
        north = state[1] + state[5]
        south = state[2] + state[6]
        west = state[4] + state[8]
        east = state[3] + state[7]
        lanes = [south, west, north, east]
        return lanes.index(max(lanes))

    def get_stats(state):
        for i in range(len(state)):
            if state[i] == -1:
                state[i] = 0
        north = state[1] + state[5]
        south = state[2] + state[6]
        west = state[4] + state[8]
        east = state[3] + state[7]
        return [south, west, north, east]
    '''

