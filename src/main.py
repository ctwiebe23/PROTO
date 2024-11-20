import lib.make as make

left = make.smallmotor(11)
right = make.smallmotor(13, -1)

d = make.drivetrain(left, right)

up = make.button(8)
down = make.button(9)

while True:
    d.turn(1)
    down.wait_until_pressed()
    d.stop()
    down.wait_until_pressed()

# poll_time = 0.05
# count = 0
# intr1 = 2.5
# intr2 = 0.75
# cycle = intr1 + intr2

# while not down.pressed():
#     if count < intr1:
#         d.drive(100)
#     elif count < intr2:
#         d.turn(50)
#     else:
#         d.stop()
#         count = 0
#     count += poll_time
#     make.wait(poll_time)

# def poll(end_condition: any, intervals: tuple[float,any]):
#     buf = 0.05
#     curr = 0
#     while not end_condition():
#         for i,time,action in enumerate(intervals):
#             if i == 0 and curr < time:
#                 action()
#             elif intervals[i - 1][0] <= curr and curr < time:
#                 action()
