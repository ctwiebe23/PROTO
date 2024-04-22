# MAKE

AUTHOR(S)

- Carston Wiebe ([carstonwiebe17@gmail.com](carstonwiebe17@gmail.com))

UPDATED

- 2024-04-22 : translated doc to markdown
- 2024-04-21 : `largemotor` & `button`
- 2024-04-12 : `dc_motors`, `servos`, `stopall`
- 2024-04-10 : PHILOSOPHY
- 2024-04-06 : techdoc creation

PURPOSE

- Created for the University of Nebraska-Lincoln's SPARK student organization

## DESCRIPTION

Wrapper for CIRCUITPython (also written in Python) to be used on the MakerPI
RP2040 in order to allow the simple creation of code by elementary and middle
school students for educational purposes.

## PHILOSOPHY

Classes and functions should be written with ease of use in mind-- a minimum
amount of knowledge on coding should be assumed and expected, and the users may
not have access to a proper IDE with features like intelligent syntax
highlighting.

As such, convention should be disregarded when it conflicts with ease of
understanding; for instance, *all* names should be lowercase only so as to
prevent simple issues with capitalization that young users might encounter (and
that won't be caught by the computer without an IDE).

(Incomplete) list of rules:

- all flatcase (lowercase, no underscores)
- prioritize one-word names
- if possible, lines should read like English; i.e. `until( button.pressed )`
- use simple words without complicated spelling
- abstract complexities away; i.e. rather than require users to input
  `board.GP10`, create a dict with the key `10` and value `board.GP10`

## CONTENT

### CLASSES :: button

    button( pin )

Represents a button, either one of the two mounted to the board or one attached
later. Requires only a port to be constructed, and can be built from either one
of the `BUTTON_PIN`s or one of the `GROVE_PINs`.

### CLASSES :: button :: pressed

    button.pressed()

Returns `true` if the button is pressed, and `false` otherwise.

### CLASSES :: largemotor

    largemotor( pinset )

Represents a DC motor mounted on one of the 2 DC motor ports. Requires only a
`pinset` in `DC_PIN`s to be constructed, which limits the number of
`largemotor`s to 2.

### CLASSES :: largemotor :: spin

    largemotor.spin( speed, ~time~ )

Takes a `speed` in the range `[-100, 100]` (all values outside the range are
constrained) and runs the motor at that speed. Optionally, a `time` can be
passed in seconds and the motor will only spin for the allotted time before
stopping.

### CLASSES :: largemotor :: stop

    largemotor.stop()

Equivalent to `largemotor.spin( 0 )`.

### CLASSES :: sensor



### CLASSES :: sensor :: distance



### CLASSES :: smallmotor



### CLASSES :: smallmotor :: spin



### CLASSES :: smallmotor :: stop



### CONSTANTS :: BUTTON_PIN



### CONSTANTS :: CYCLE



### CONSTANTS :: DC_PIN



### CONSTANTS :: FRQ



### CONSTANTS :: GROVE_PIN



### CONSTANTS :: SERVO_PIN



### FUNCTIONS :: loop



### FUNCTIONS :: pause

    pause( ~time~ )

If a `time` is passed, waits for the allotted `time`. Otherwise, waits for
0.005 seconds.

### FUNCTIONS :: until

    until( condition )

Pauses the program until the passed `condition` is satisfied.

### FUNCTIONS :: stopall

    stopall()

Halts all constructed `large`/`smallmotors` (tracked in `dc_motors` and
`servos`).

### VARIABLES :: dc_motors

Tracks all constructed `largemotors`.

### VARIABLES :: servos

Tracks all constructed `smallmotors`.
