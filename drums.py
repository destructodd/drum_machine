#from gpiozero import Motor
import time
import pigpio

pi = pigpio.pi()

p = 0.05
d = 255

bpm = 90
bps = bpm/60

def left_hit():
    pi.set_PWM_dutycycle(20, d)
    pi.set_PWM_dutycycle(21, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 0)
    
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, d)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 0)
    

def both_hit():
    pi.set_PWM_dutycycle(19, d)
    pi.set_PWM_dutycycle(26, 0)
    pi.set_PWM_dutycycle(20, d)
    pi.set_PWM_dutycycle(21, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 0)
    #print('out')
    
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, d)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, d)
    time.sleep(p)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 0)
    #print('in')

def right_hit():
    pi.set_PWM_dutycycle(19, d)
    pi.set_PWM_dutycycle(26, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)
    #print('out')
    
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, d)
    time.sleep(p)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)

print("start")
while True:
    both_hit()
    time.sleep((1/bps)/8)
    right_hit()
    time.sleep((1/bps)/8)
    right_hit()
    time.sleep((1/bps)/8)
    right_hit()
    time.sleep((1/bps)/16)
    right_hit()
    time.sleep((1/bps)/8)
#left_hit()
#left_hit()
#left_hit()

print('end')

#print("hit")
#time.sleep(1)
#pi.set_PWM_dutycycle(21, d)
#print("retract")
#print("done")
#while True: 
#    left_stick.forward()
#    print("drum1")
#    time.sleep(10)
#    left_stick.backward()
#    print("drum2")

#print(dir(pigpio.pi))
