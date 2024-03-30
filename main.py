import make

button1 = make.button( 20 )
button2 = make.button( 21 )

motor1 = make.motor(  8,  9 )
motor2 = make.motor( 10, 11 )

# servo1 = make.servo( 15 )

while True:
    if button1.is_pressed():
        # servo1.spin( 0 )
        motor1.spin(  0.5 )
        motor2.spin( -0.5 )

    if button2.is_pressed():
        # servo1.spin( 180 )
        motor1.spin( 0 )
        motor2.spin( 0 )

    make.pause( 0.05 )
