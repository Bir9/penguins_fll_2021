# This is where we keep all the shared blocks. Please only include functions
# and constants in this file for now.

SHARPNESS = 0.7
SPEED = 300
WHEEL_CIRCUMFERENCE = 180

def follow_line(tank, left_cs, right_cs, millies):
    tank.reset()
    while tank.distance() < millies:
        subtract = left_cs.reflection() - right_cs.reflection() # subtracts color sensors
        multiply = subtract * SHARPNESS # multiplies the difference by 0.7
        tank.drive(SPEED, multiply) # follows the line 

def gyro_straight(tank, gyro, millies, target):
    tank.reset()
    while tank.distance() < millies:
        subtract = gyro.angle() - target  # subtracts color sensors
        multiply = subtract * SHARPNESS # multiplies the difference by 0.7
        tank.drive(SPEED, multiply) # follows the line
        
        
        
def gyro_angle( tank, gyro_sensor, left_wheel, right_wheel, angle):
    gyro_sensor.reset_angle(0)
    big = angle + 1
    small = angle - 1
    while gyro.angle() <= small or gyro.angle() >= big:
        while gyro.angle() <= small or gyro.angle() >= big: 
            if gyro_sensor.angle() <= small:
                left_wheel.run(TURN_SPEED)
                right_wheel.run(TURN_SPEED * -1)
            else:
                left_wheel.run(TURN_SPEED * -1)
                right_wheel.run(TURN_SPEED)
        tank.stop()
        time.sleep(0.5)
        #print(gyro.angle())
        
        
        
def stop_on_black(left_cs, right_cs):
        if left_cs.reflection() <= 14 and right_cs.reflection() <= 14:
            return True
        else:
            return False

        
def perpendicular_line(tank, left_cs, right_cs, line_distance):
    if line_distance >= 0:
        turn = 85
    else:
        turn = -85
    tank.settings(200, 100, 100, 100)
    tank.turn(turn)
    tank.straight(abs(line_distance))
    tank.turn(turn * -1)
    while not stop_on_black(left_cs, right_cs):
        tank.drive(100, 0)
    tank.stop()
    
    
    
                    
# Definitions ////////////////////////////////////////////////////////////////////
TURN_SPEED  = 50


def go_to_coordinate(tank, gyro_sensor, left_wheel, right_wheel, targetx, targety):
    # The assumption is that the robot is at (0,0) along x axis. 
    slope = targety/targetx
    angle = math.atan(slope)
    angle_degrees = math.degrees(angle)
    gyro_angle(tank, gyro_sensor, left_wheel, right_wheel, angle_degrees * -1)
    length = math.sqrt(targetx**2 + targety**2)
    tank.straight(length)
    tank.stop()
