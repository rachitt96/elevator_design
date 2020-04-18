import time
import ElevatorStates

class Elevator:

    def __init__(self, default_position = 0):
        self.current_position = default_position
        self.current_state = ElevatorStates.NOT_MOVING
        self.floors_to_stop_up = []
        self.floors_to_stop_down = []
        
    '''
    def call(self, called_floor_number):
        self.floors_to_stop.append(called_floor_number)
        self.move()
    '''
    
    def print_current_position(self):
        print("Elevator is at: ", self.current_position)

    def move_up(self, target_floor_number):
        self.current_state = ElevatorStates.MOVING_UP
        for i in range(self.current_position, target_floor_number):
            time.sleep(3)
            self.current_position = i + 1
            self.print_current_position()

    def move_down(self, target_floor_number):
        self.current_state = ElevatorStates.MOVING_DOWN
        for i in range(self.current_position, target_floor_number, -1):
            time.sleep(3)
            self.current_position = i - 1
            self.print_current_position()
    '''
    def move(self, next_target):
        
        next_target = self.floors_to_stop[0]
        del self.floors_to_stop[0]
        

        if(next_target > self.current_position):
            self.move_up(next_target)
        elif(next_target < self.current_position):
            self.move_down(next_target)
        else:
            self.print_current_position()
    '''