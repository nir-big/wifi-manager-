from machine import Pin, PWM

class MotorController:
    def __init__(self, motor_pins):
        self.motor1_fwd = Pin(motor_pins['input1'], Pin.OUT)
        self.motor1_bwd = Pin(motor_pins['input2'], Pin.OUT)
        self.motor1_en = PWM(Pin(motor_pins['enable']))
        self.motor1_en.freq(1000)

        self.motor2_fwd = Pin(motor_pins['input3'], Pin.OUT)
        self.motor2_bwd = Pin(motor_pins['input4'], Pin.OUT)
        self.motor2_en = PWM(Pin(motor_pins['enable2']))
        self.motor2_en.freq(1000)

    def forward(self, speed=30000):
        self.motor1_fwd.on()
        self.motor1_bwd.off()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.on()
        self.motor2_bwd.off()
        self.motor2_en.duty_u16(speed)

    def backward(self, speed=30000):
        self.motor1_fwd.off()
        self.motor1_bwd.on()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.off()
        self.motor2_bwd.on()
        self.motor2_en.duty_u16(speed)

    def stop(self):
        self.motor1_fwd.off()
        self.motor1_bwd.off()
        self.motor1_en.duty_u16(0)
        self.motor2_fwd.off()
        self.motor2_bwd.off()
        self.motor2_en.duty_u16(0)

    def forward_left(self, speed=30000):
        self.motor1_fwd.on()
        self.motor1_bwd.off()
        self.motor1_en.duty_u16(speed // 2)  # Reduce speed on one motor
        self.motor2_fwd.on()
        self.motor2_bwd.off()
        self.motor2_en.duty_u16(speed)

    def forward_right(self, speed=30000):
        self.motor1_fwd.on()
        self.motor1_bwd.off()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.on()
        self.motor2_bwd.off()
        self.motor2_en.duty_u16(speed // 2)  # Reduce speed on one motor

    def backward_left(self, speed=30000):
        self.motor1_fwd.off()
        self.motor1_bwd.on()
        self.motor1_en.duty_u16(speed // 2)  # Reduce speed on one motor
        self.motor2_fwd.off()
        self.motor2_bwd.on()
        self.motor2_en.duty_u16(speed)

    def backward_right(self, speed=30000):
        self.motor1_fwd.off()
        self.motor1_bwd.on()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.off()
        self.motor2_bwd.on()
        self.motor2_en.duty_u16(speed // 2)  # Reduce speed on one motor

    def rotate_left(self, speed=30000):
        self.motor1_fwd.off()
        self.motor1_bwd.on()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.on()
        self.motor2_bwd.off()
        self.motor2_en.duty_u16(speed)

    def rotate_right(self, speed=30000):
        self.motor1_fwd.on()
        self.motor1_bwd.off()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.off()
        self.motor2_bwd.on()
        self.motor2_en.duty_u16(speed)

    def left(self, speed=30000):
        self.motor1_fwd.off()
        self.motor1_bwd.on()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.on()
        self.motor2_bwd.off()
        self.motor2_en.duty_u16(speed)

    def right(self, speed=30000):
        self.motor1_fwd.on()
        self.motor1_bwd.off()
        self.motor1_en.duty_u16(speed)
        self.motor2_fwd.off() 
        self.motor2_bwd.on()
        self.motor2_en.duty_u16(speed)

