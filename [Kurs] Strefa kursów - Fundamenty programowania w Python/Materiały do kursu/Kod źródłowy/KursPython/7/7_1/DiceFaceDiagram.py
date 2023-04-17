class DiceFaceDiagram:
    def __init__(self, roll_results):
        self.dice_faces_diagram = self.generate_dice_faces_diagram(roll_results)

    DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    DIE_HEIGHT = len(DICE_ART[1])
    DIE_WIDTH = len(DICE_ART[1][0])
    DIE_FACE_SEPARATOR = " "

    def generate_dice_faces_diagram(self, roll_results):
        dice_faces = []

        for value in roll_results:
            dice_faces.append(self.DICE_ART[value])

        dice_faces_rows = []
        for row_idx in range(self.DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_idx])
            row_string = self.DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)

        width = len(dice_faces_rows[0])
        diagram_header = " RESULTS ".center(width, "~")

        dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
        return dice_faces_diagram

    def display_results(self):
        print(f"\n{self.dice_faces_diagram}")
