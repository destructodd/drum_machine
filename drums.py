#from gpiozero import Motor
print('begin')
import time
import pigpio
import pygame
import numpy as np

pygame.init()

timer = pygame.time.Clock()

pi = pigpio.pi()

p = 0.035
d = 255

bpm = 35
bps = bpm/60
nps = bps*8

def right_hit(d):
    pi.set_PWM_dutycycle(20, d)
    pi.set_PWM_dutycycle(21, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 255)

def left_hit(d):
    pi.set_PWM_dutycycle(19, d)
    pi.set_PWM_dutycycle(26, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 255)
    
def both_hit(d):
    pi.set_PWM_dutycycle(20, d)
    pi.set_PWM_dutycycle(19, d)
    pi.set_PWM_dutycycle(21, 0)
    pi.set_PWM_dutycycle(26, 0)
    time.sleep(p)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(21, 255)
    pi.set_PWM_dutycycle(26, 255)


    
def rest():
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, d)
    pi.set_PWM_dutycycle(21, d)
    time.sleep(0.05)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(19, 0)
    pi.set_PWM_dutycycle(26, 0)
    pi.set_PWM_dutycycle(21, 0)

arr = np.array([[255,0,0],[0,0,0],[0,255,0],[0,0,0],
                [0,255,0],[0,0,0],[0,255,0],[0,0,0],
                [255,0,0],[0,0,255],[0,255,0],[0,0,0],
                [0,255,0],[0,0,0],[0,255,0],[0,0,0],
               ])

arr_full = arr

for x in range(5):
    arr_full = np.concatenate((arr_full, arr))
    
length = len(arr_full)
etime =length/nps

print(f"Notes Per Second: {nps}")
print(f"Beats Per Second: {bps}")
print(f"Beats Per Minute: {bpm}")
print(f"Expected time: {etime}")


start = time.time()
try:
    for n in arr_full:
        if n[0]>0:
            both_hit(n[0])
        else:
            left_hit(n[1])
            right_hit(n[2])
    
        timer.tick_busy_loop(nps)  
    
except KeyboardInterrupt:
    print('quit')

rest()

print(time.time()-start)
    
        

      
    


