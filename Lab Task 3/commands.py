# --- Command Interface ---
class Command:
    def execute(self, turtle):
        pass
    def name(self):
        return "Unnamed Command"

# --- Concrete Commands ---
class ForwardCommand(Command):
    def name(self):
        return "Move Forward"
    def execute(self, turtle):
        turtle.forward()

class TurnLeftCommand(Command):
    def name(self):
        return "Turn Left"
    def execute(self, turtle):
        turtle.turn_left()

class TurnRightCommand(Command):
    def name(self):
        return "Turn Right"
    def execute(self, turtle):
        turtle.turn_right()
