import lib.make as make
import board
import pulseio

motor = make.largemotor(6)
debug = make.largemotor(7)
button = make.button(8)
pulses = pulseio.PulseIn(board.GP27, maxlen=200, idle_state=True)

pulses.pause()
if len(pulses) == 0:
    motor.spin(100, 3)
pulses.resume()

make.wait()

while True:
    pulses.pause()
    length = len(pulses)
    debug.spin(length, 1)
    pulses.resume()
    make.wait(1)
