# Examples

! example code !

```python
import make

forward  = make.button( 1 )
backward = make.button( 2 )
motor    = make.small_motor( 3 )

while True:  # loops forever

    if forward.pressed():
        motor.spin( 100 )

    if backward.pressed():
        motor.spin( -100 )

    if forward.pressed() and backward.pressed():
        motor.stop()

    make.pause()  # pause briefly before looping
```

Start: [Start](../readme.md)
| Previous: [Basics of Make](./make.md)
| Next: [Advanced Topics](./advanced.md)
