from Elevator import Elevator
import ElevatorStates

class ElevatorController:

    def __init__(self, total_floors):
        self.elevator_obj = Elevator()
        self.max_floor_number = total_floors

    def floor_button_pressed(self, floor_number, button_direction):

        if(self.elevator_obj.current_state == ElevatorStates.NOT_MOVING):
            if(self.elevator_obj.current_position < floor_number):
                self.elevator_obj.floors_to_stop_up.append(floor_number)
            else:
                self.elevator_obj.floors_to_stop_down.append(floor_number)

        if(button_direction == "UP"):
            if(self.elevator_obj.current_state == ElevatorStates.MOVING_UP):
                self.elevator_obj.floors_to_stop_up.append(floor_number)
            
        elif(button_direction == "DOWN"):
            if(self.elevator_obj.current_state == ElevatorStates.MOVING_DOWN):
                self.elevator_obj.floors_to_stop_down.append(floor_number)
        
    def elevator_button_pressed(self, elevator_object, floor_number):

        if(elevator_object.current_state == ElevatorStates.MOVING_DOWN):
            if(floor_number not in elevator_object.floors_to_stop_down):
                elevator_object.floors_to_stop_down.append(floor_number)

        elif(elevator_object.current_state == ElevatorStates.MOVING_UP):
            if(floor_number not in elevator_object.floors_to_stop_up):
                elevator_object.floors_to_stop_up.append(floor_number)

        else:
            if(elevator_object.current_position > floor_number):
                elevator_object.floors_to_stop_up.append(floor_number)
            else:
                elevator_object.floors_to_stop_down.append(floor_number)

    def move_elevator(self, elevator_object):

        if(len(elevator_object.floors_to_stop_up) == 0 and len(elevator_object.floors_to_stop_down) == 0):
            elevator_object.current_state = ElevatorStates.NOT_MOVING

        else:
            if(elevator_object.current_state == ElevatorStates.MOVING_UP):
                if(len(elevator_object.floors_to_stop_up) > 0):
                    next_target = elevator_object.floors_to_stop_up[0]
                    del elevator_object.floors_to_stop_up[0]
                    elevator_object.move_up(next_target)

                else:
                    next_target = elevator_object.floors_to_stop_down[0]
                    del elevator_object.floors_to_stop_down[0]
                    elevator_object.move_down(next_target)

            elif(elevator_object.current_state == ElevatorStates.MOVING_DOWN):
                if(len(elevator_object.floors_to_stop_down) > 0):
                    next_target = elevator_object.floors_to_stop_down[0]
                    del elevator_object.floors_to_stop_down[0]
                    elevator_object.move_down(next_target)

                else:
                    next_target = elevator_object.floors_to_stop_up[0]
                    del elevator_object.floors_to_stop_up[0]
                    elevator_object.move_up(next_target)

            elif(elevator_object.current_state == ElevatorStates.NOT_MOVING):
                if(len(elevator_object.floors_to_stop_down) > 0):
                    next_target = elevator_object.floors_to_stop_down[0]
                    del elevator_object.floors_to_stop_down[0]
                    elevator_object.move_down(next_target)

                else:
                    next_target = elevator_object.floors_to_stop_up[0]
                    del elevator_object.floors_to_stop_up[0]
                    elevator_object.move_up(next_target)


    def authenticate_user_request(self, floor_number):
        
        if(floor_number > self.max_floor_number or floor_number < 0):
            print("floor number error")
            return False
        else:
            return True