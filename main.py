import Make

button1 = Make.Button( 20 )
button2 = Make.Button( 21 )

dc1 = Make.DC(  8,  9 )
dc2 = Make.DC( 10, 11 )

servo = Make.Servo( 15 )

while True:

    if button1.is_pressed():
        servo.spin( 0 )
        dc1.spin(  0.5 )
        dc2.spin( -0.5 )

    if button2.is_pressed():
        servo.spin( 180 )
        dc1.spin( 0 )
        dc2.spin( 0 )

    Make.Pause( 0.05 )
