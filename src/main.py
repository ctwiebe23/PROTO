import lib.make as make  # same as `import make`

'''
FOR:  PROTO Focus Group
BY:   Carston Wiebe
ON:   2024.11.08
DOES: Endless loop where both buttons correspond to a largemotor.  When
      a button is pressed, its paired motor spins uninterrupted for 5
      seconds.  It then continues looping.
'''

# name components
motor1  = make.largemotor( port=6 )
motor2  = make.largemotor( port=7 )
button1 = make.button    ( port=8 )
button2 = make.button    ( port=9 )

while True:  # loops forever, because `True` is always true
  
    make.wait()  # wait for a very short time to stop the brain from
                 # working as fast as it possibly can and overworking
    
    if button1.pressed():
        motor1.spin( power=100, seconds=5 )
    elif button2.pressed():  # 'elif' means 'else if'
        motor2.spin( power=100, seconds=5 )
