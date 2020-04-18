from ElevatorController import ElevatorController

if(__name__ == "__main__"):
    elevator_controller_obj = ElevatorController(total_floors = 5)

    print("1: to call elevator by pressing button on floor")
    print("2: to go to destination floor by pressing button inside elevator")
    print("3: to exit from the program")

    def option_one():
        floor_number = int(input("enter floor number person is standing at:\n"))
        button_direction = input("enter button direction:\n")

        if(elevator_controller_obj.authenticate_user_request(floor_number = floor_number)):
            elevator_controller_obj.floor_button_pressed(floor_number, button_direction)
            elevator_controller_obj.move_elevator(elevator_controller_obj.elevator_obj)

    def option_two():
        floor_number = int(input("enter floor number after going inside of elevator:"))

        if(elevator_controller_obj.authenticate_user_request(floor_number = floor_number)):
            elevator_controller_obj.elevator_button_pressed(elevator_object = elevator_controller_obj.elevator_obj, floor_number = floor_number)
            elevator_controller_obj.move_elevator(elevator_controller_obj.elevator_obj)


    while(True):
        user_input = input("enter your request:\n")
        user_input = int(user_input)

        if(user_input == 3):
            break

        options = {
            1 : option_one,
            2 : option_two
        }

        options[user_input]()

        

        
        
        