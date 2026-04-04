import lib.make as make

led1 = make.light(8)
led2 = make.light(9)
dc = make.drive_motor(6)

led1.on()
dc.spin(100)

while True:
  led2.toggle()
  make.wait(0.2)
