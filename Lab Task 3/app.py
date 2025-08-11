from turtle_sim import Turtle
from commands import ForwardCommand, TurnLeftCommand, TurnRightCommand

class App:
    def __init__(self):
        self.turtle = Turtle()
        self.commands = {
            'F': ForwardCommand(),
            '+': TurnRightCommand(),
            '-': TurnLeftCommand()
        }

    def run(self):
        print("Drawing Commands: F = forward, + = right turn, - = left turn")
        pattern = input("Enter pattern (e.g., F+F+F+F): ").strip().upper()

        for char in pattern:
            cmd = self.commands.get(char)
            if cmd:
                cmd.execute(self.turtle)
            else:
                print(f"Unknown command: {char}")

        print("\nPath taken by turtle:")
        for p in self.turtle.path:
            print(f" -> {p}")
