#from gpiozero import Motor
print('begin')
import time
import pigpio
import pygame
import numpy as np

pygame.init()

timer = pygame.time.Clock()

pi = pigpio.pi()

p = 0.05
d = 255

bpm = 90
bps = bpm/60
nps = bpm*8

def right_hit(d):
    pi.set_PWM_dutycycle(20, d)
    pi.set_PWM_dutycycle(21, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, d)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 0)
   

def left_hit(d):
    pi.set_PWM_dutycycle(19, d)
    pi.set_PWM_dutycycle(26, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, d)
    time.sleep(p)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)
    
def both_hit(d):
    pi.set_PWM_dutycycle(20, d)
    pi.set_PWM_dutycycle(19, d)
    pi.set_PWM_dutycycle(26, 0)
    pi.set_PWM_dutycycle(21, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, d)
    pi.set_PWM_dutycycle(21, d)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)
    pi.set_PWM_dutycycle(21, 0)

arr = np.array([[255,0,0],[0,255,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,100],[0,0,100],
                [255,0,0],[0,100,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,100],[0,0,100],
                [100,0,0],[0,100,0],[0,0,110],[0,0,100],
                [255,0,0],[0,255,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,255],[0,0,255],
                [255,0,0],[0,255,0],[0,0,255],[0,0,255]])



run = True
n = 0

try:
    for n in arr:
        print('tick')
        both_hit(n[0])
        left_hit(n[1])
        right_hit(n[2])
    
        timer.tick_busy_loop(nps)
        
except KeyboardInterrupt:
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)
    pi.set_PWM_dutycycle(21, 0)
    print('quit')

    
        

      
    


