class Rover(object):
    position = None
    heading = None
    supported_directions_count = None
    supported_directions = ['N', 'E', 'S', 'W']

    def __init__(self, plateau, position, heading):

        self.plateau = plateau
        self.update_position(position, heading)

    def update_position(self, new_position, heading):
        self.heading = heading
        self.position = new_position
        self.supported_directions_count = self.supported_directions.index(heading)

    def process(self, actions):
        max_x = self.plateau.width
        max_y = self.plateau.height

        min_x, min_y = 0, 0

        current_x = self.position[0]
        current_y = self.position[1]

        direction = self.heading

        x = 0
        # PROCESS ACTIONS
        for i in actions:
            # ROTATE 90 RIGHT
            if i == 'R':
                direction = self.r_rotate()
            # ROTATE 90 LEFT
            elif i == 'L':
                direction = self.l_rotate()
            # MOVE ONE POINT
            else:
                if direction == 'N' and (current_y + 1) <= max_y:
                    current_y += 1
                elif direction == 'W' and (current_x - 1) >= min_x:
                    current_x -= 1
                elif direction == 'E' and (current_x + 1) <= max_x:
                    current_x += 1
                elif direction == 'S' and (current_y - 1) >= min_y:
                    current_y -= 1
                else:
                    return "can't move in that direction"

            x += 1

        return current_x, current_y, direction

    def l_rotate(self):
        self.supported_directions_count = (self.supported_directions_count - 1) % 4
        return self.supported_directions[self.supported_directions_count]

    def r_rotate(self):
        self.supported_directions_count = (self.supported_directions_count + 1) % 4
        return self.supported_directions[self.supported_directions_count]
