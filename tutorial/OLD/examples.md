# Examples

! example code !

```python
import lib.make as make

# name the drive motors
left    = make.smallmotor( port=11 )
right   = make.smallmotor( port=13, direction=-1 )  # this motor's facing the
                                                    #  opposite direction
# name the robot, using the motors
robot   = make.drivetrain( left_motor=left, right_motor=right )

# name the buttons
button1 = make.button( port=8 )
button2 = make.button( port=9 )

# make actions using your robot
while True:
    robot.drive( power=100 )            # no time given -- spins forever!
    make.wait_until( button2.pressed )  # motor still spins while code waits
    robot.stop()                        # stops the motor no matter what
    make.wait_until( button2.pressed )  # stays stopped while the bot's waiting
    # loops back to the `while True`
```

Start: [Start](../readme.md)
| Previous: [Basics of Make](./make.md)
| Next: [Advanced Topics](./advanced.md)
