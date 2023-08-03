# kmk for handwired corne keyboard
# credit given to reddit user gandi800 for providing a portion of this code
import board

from kmk.kmk_keyboard import KMKKeyboard

from kb import varList

from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide




from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# debug feature allows user to validate keystrokes during debugging
keyboard.debug_enabled = True

# using uart wiring for tx/rx communication
# use pio is required 
# uart flip allows same wiring but each side to flip for proper tx->rx communication
split = Split(split_type=SplitType.UART, split_side=varList.ss, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)

keyboard.modules.append(split)

layers_ext = Layers()
keyboard.modules.append(layers_ext)

keyboard.col_pins = varList.col_pins
keyboard.row_pins = varList.row_pins

_______ = KC.TRNS
XXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.MO(3)

# base layer for colemak
keyboard.keymap = [
    [KC.ESCAPE , KC.Q, KC.W, KC.F, KC.P, KC.G,          KC.J, KC.L, KC.U, KC.Y, KC.SCOLON, KC.EQUAL,
     KC.TAB, KC.A, KC.R, KC.S, KC.T, KC.D,              KC.H, KC.N, KC.E, KC.I, KC.O, KC.QUOTE,
     KC.LEFT_SHIFT , KC.Z, KC.X, KC.C, KC.V, KC.B,      KC.K, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT,
     KC.WINDOWS, KC.LEFT_CONTROL, KC.BSPACE,          KC.SPACEBAR, KC.ENTER, KC.RALT
     ]

]


if __name__ == '__main__':
    keyboard.go()
