# Examples

! example code !

```python
import make

stop_button = make.button(port = 2)

left_wheel = make.large_motor(port = 7)
right_wheel = make.large_motor(port = 8, direction = make.reversed)

arm = make.small_motor(port = 6)

robot = make.drivetrain(left_motor = left_wheel, right_motor = right_wheel)

# drive in a curved line
robot.curve(left_speed = 80, right_speed = 40, time = 3)

# drive forward
robot.drive(speed = 40, time = 2)

# turn on the spot
robot.turn(speed = 60, time = 1)

# extend and retract the arm
arm.spin(speed = 20, time = 1)
arm.spin(speed = -20, time = 1)

# spin slowly until turned off
robot.turn(speed = 10)
make.pause_until(stop_button.pressed)
robot.stop()
```

Start: [Start](../readme.md)
| Previous: [Basics of Make](./make.md)
| Next: [Advanced Topics](./advanced.md)
