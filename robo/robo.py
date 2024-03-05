

colors = {
        "black": '\x1b[90m',
        "blue": '\x1b[94m',
        "cyan": '\x1b[96m',
        "green": '\x1b[92m',
        "magenta": '\x1b[95m',
        "red": '\x1b[91m',
        "white": '\x1b[97m',
        "yellow":'\x1b[93m',
    }


# parte 5
def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status
      
        
def build_robot():
    robot_name = input("Robot name: ")
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot

def choose_color():
    available_colors = colors
    print("Available colors:")
    for key, value in available_colors.items():
        print(value, key)
    print(colors["White"])
    chosen_color = input("Choose a color: ")
    color_code = available_colors[chosen_color]
    return color_code

# parte 6

def play():
    playing = True
    print("Welcome to the game!")
    print("Datas for player 1:")
    robot_one = build_robot()
    print("Datas for player 2:")
    robot_two = build_robot()

    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        current_robot.print_status()
        print("What part should I use to attack?:")
        part_to_use = input("Choose a number part: ")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        print("Which part of the enemy should we attack?")
        part_to_attack = input("Choose a enemy number part to attack: ")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print("Congratulations, you won")
play()
