# Examples

! example code !

```python
import make

# naming
stopbutton = make.button(2)
leftwheel = make.largemotor(7)
rightwheel = make.largemotor(8)
myrobot = make.drivetrain(leftwheel, rightwheel)

# actions
myrobot.drive(speed=40, seconds=4)
myrobot.turn(speed=30, seconds=0.5)
myrobot.curve(left_speed=60, right_speed=90, seconds=2.5)

# code is read top to bottom
make.wait(seconds=2)
myrobot.turn(speed=-10)
make.wait_until(stopbutton.pressed)
myrobot.stop()
```

Start: [Start](../readme.md)
| Previous: [Basics of Make](./make.md)
| Next: [Advanced Topics](./advanced.md)
