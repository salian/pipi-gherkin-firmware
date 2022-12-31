# SPDX-FileCopyrightText: 2022 Pranab Salian
# PiPi-GHERKIN - Raspberry Pi Pico based 30-key Keyboard/Macropad

import board
from kmk.keys import KC

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes

gherkin = KMKKeyboard()

modtap = ModTap()
layers_ext = Layers()
# optional: set a custom tap timeout in ms
# modtap.tap_time = 300
gherkin.modules = [layers_ext, modtap]

gherkin.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
gherkin.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)
gherkin.diode_orientation = DiodeOrientation.COLUMNS
gherkin.debug_enabled = False

# Rotate gherkin so the USB port of the Pico is on the right side. 
# Comment out if the USB port is on the left.

# gherkin.col_pins = tuple(reversed(gherkin.col_pins))
# gherkin.row_pins = tuple(reversed(gherkin.row_pins))


# Clean key names

_______ = KC.TRNS
XXXXXXX = KC.NO

FN1_SPC = KC.LT(1, KC.SPC)
FN2_BSPC = KC.LT(2, KC.BSPC)
FN3_C = KC.LT(3, KC.C)
FN4_V = KC.LT(4, KC.V)
CTL_Z = KC.MT(KC.Z, KC.LCTL)
ALT_X = KC.MT(KC.X, KC.LALT)
ALT_N = KC.MT(KC.N, KC.LALT)
CTL_M = KC.MT(KC.M, KC.LCTL)
SFT_ENT = KC.LSFT(KC.ENT)

gherkin.keymap = [
    [
        KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,     KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,   KC.G,     KC.H,    KC.J,    KC.K,    KC.L,    KC.ESC,
        CTL_Z,   ALT_X,   FN3_C,   FN4_V,  FN2_BSPC, FN1_SPC, KC.B,   ALT_N,   CTL_M,   SFT_ENT
    ],
    [
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,
        _______, _______, _______, _______, KC.DEL,  _______, _______, _______, _______, _______
    ],
    [
        KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
        KC.F11,  KC.F12,  _______, _______, _______, _______, _______, _______, _______, KC.GRV,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______
    ],
    [
        _______, _______, _______, _______, _______, KC.MINS, KC.EQL,  KC.LBRC, KC.RBRC, KC.BSLS,
        KC.TAB,  _______, _______, _______, _______, KC.COMM, KC.DOT,  KC.SLSH, KC.SCLN, KC.QUOT,
        _______, _______, _______, _______, _______, _______, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT
    ],
    [
        _______, _______, _______, _______, _______, KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,
        KC.TAB,  _______, _______, _______, _______, KC.LABK, KC.RABK, KC.QUES, KC.COLN, KC.DQUO,
        _______, _______, _______, _______, _______, _______, KC.HOME, KC.PGDN, KC.PGUP, KC.END
    ],
]

if __name__ == '__main__':
    gherkin.go(hid_type=HIDModes.USB) # Enable Wired USB
    
