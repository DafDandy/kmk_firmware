# kmk for handwired corne keyboard
# credit given to reddit user gandi800 for providing a portion of this code

#right
import board

from kmk.modules.split import SplitSide

# adjust pins accordingly
class varList():
    col_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7
        )
    row_pins = (
        board.GP16,
        board.GP17,
        board.GP20,
        board.GP18
    )


# This is the only difference between the 2 sides and is flashed accordingly
    ss = SplitSide.RIGHT
