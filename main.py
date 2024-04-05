import make

on_button  = make.button( 1 )
off_button = make.button( 2 )

motor = make.motor( 1 )

make.pause_until( on_button.is_pressed )
motor.spin( 50 )

make.pause_until( off_button.is_pressed )
motor.spin( 0 )

make.pause( 3 )

while not off_button.is_pressed():
    # must wait until the cycle ends to check condition
    motor.spin( 25, 3 )
    make.pause( 3 )
    motor.spin( -25, 3 )
    make.pause( 3 )
