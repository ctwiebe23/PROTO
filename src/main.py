import lib.make as make

# define both motors to be safe
m1 = make.largemotor(port=6)
m2 = make.largemotor(port=7)

# use the default start button
button = make.button(port=8)

# after initial press
m1.spin(100)
m2.spin(100)
make.wait(3)
m1.stop()
m2.stop()

while True:
    # subsequent presses
    make.wait_until(button.pressed)
    make.wait(1)
    
    m1.spin(100)
    m2.spin(100)
    make.wait(3)
    m1.stop()
    m2.stop()
