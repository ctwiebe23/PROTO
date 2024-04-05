import make

# on_button  = make.button( 1 )
# off_button = make.button( 2 )

# left_motor  = make.motor( 1 )
# right_motor = make.motor( 2 )

# # servo1 = make.servo( 4 )

# while True:
#     if on_button.is_pressed():
#         # servo1.spin( 0 )
#         left_motor.spin( 50 )
#         right_motor.spin( -50 )

#     if off_button.is_pressed():
#         # servo1.spin( 180 )
#         left_motor.spin( 0 )
#         right_motor.spin( 0 )

#     make.pause( 0.05 )

on_button  = make.button( 1 )
off_button = make.button( 2 )

motor = make.motor( 1 )

make.pause_until(on_button.is_pressed)
motor.spin( 50 )

make.pause_until(off_button.is_pressed)
motor.spin( 0 )

make.pause( 3 )

while not off_button.is_pressed():
    # must wait until the cycle ends to check condition
    motor.spin( 25, 3 )
    make.pause( 3 )
    motor.spin( -25, 3 )
    make.pause( 3 )
