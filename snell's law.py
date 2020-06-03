# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:09:28 2020

@author: Paras

Snell's Law Visualization

"""
import numpy as np
import pygame
import sys
import math
import time

pygame.init()


def get_angle(x,y):
    s = math.atan2(300-y, 300-x)
    angle = 90 + (s*180/math.pi)
    angle = round(angle,2)
    return angle 

def snells_law(theta1,n1,n2):
    
    critical_theta1 = math.asin(n2/n1)  ## keeping theta2 as 90 degree
    critical_theta1 = round((critical_theta1*180)/math.pi, 2)    ## Now critical_Theta1 is in degree

              
    if theta1 < critical_theta1:
        
        text = font.render('Refraction', True, (0,0,0))
        screen.blit(text, (240,5))
        a = math.sin((theta1*math.pi)/180)       
        theta2 = math.asin((n1/n2)*a)
        theta2 = round((theta2*180)/math.pi, 2)
        x1 = 300 + 300
        y1 = 300 - (math.tan((90-theta2)*math.pi/180)*300)
        
        text_surface1 = angle_font.render(f'{theta2} deg', True, (0,0,0))
        screen.blit(text_surface1, (310, 200)) 
    
    elif theta1 == critical_theta1:
        text = font.render('Critical incidence angle', True, (0,0,0))
        screen.blit(text, (180,5))
        x1 = 600
        y1 = 300
        
        theta2 = 90
        text_surface1 = angle_font.render(f'{theta2} deg', True, (0,0,0))
        screen.blit(text_surface1, (310, 200)) 
    
    
    else:
        text = font.render('Total Internal Reflection', True, (0,0,0))
        screen.blit(text, (200,5))
        x1 = 300 + 300
        y1 = 300 + (math.tan((90-theta1)*math.pi/180)*300)
        
        theta2 = theta1
        text_surface1 = angle_font.render(f'{theta2} deg', True, (0,0,0))
        screen.blit(text_surface1, (310, 400)) 
                
    return x1, y1


n1 = 1.33   # Refractive index of water
n2 = 1        # Refractive index of air
x = 0


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snell's Law Visualization")
font = pygame.font.Font('freesansbold.ttf', 20)
angle_font = pygame.font.Font('freesansbold.ttf', 15)
a = 'Water'
b = (50,100,255)

while True:    
    
    ## Window layout
    
    screen.fill((255,255,255))
    pygame.draw.rect(screen,b,(0,300,600,300))
    pygame.draw.line(screen, (0, 0, 0), (300,40), (300,600), 2)
    pygame.draw.line(screen, (0, 0, 0), (0,300), (600,300), 2)
    Air = angle_font.render('Air', True, (0,0,0))
    screen.blit(Air, (10,20)) 
    Water = angle_font.render(f'{a}', True, (0,0,0))
    screen.blit(Water, (10,550)) 
   
    ## Buttons
    
    pygame.draw.rect(screen,(50,120,255),(5,40,70,30))
    Air = angle_font.render('Water', True, (0,0,0))
    screen.blit(Air, (13,48)) 
    pygame.draw.rect(screen,(193,154,107),(5,75,70,30))
    Air = angle_font.render('Wood', True, (0,0,0))
    screen.blit(Air, (13,83)) 
    pygame.draw.rect(screen,(185,242,255),(5,110,70,30))
    Air = angle_font.render('Diamond', True, (0,0,0))
    screen.blit(Air, (7,118)) 
    
    
    
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEMOTION:
            # print (u'pressed buttons {}, position {} and relative movement {}'.format(event.buttons, event.pos, event.rel))
            if event.pos[0] <= 300 and event.pos[1] >=300:
                pygame.draw.line(screen, (0,0,0), event.pos, (300,300), 2)

            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print (u'button {} pressed in the position {}'.format(event.button, event.pos))
            
            if event.pos[0] <= 300 and event.pos[1] >=300:
                x, y = event.pos
            if 5 <= event.pos[0] <= 75 and 40 <= event.pos[1] <= 70:
                a = 'Water'
                b = (50,100,255)
                n1 = 1.33
            if 5 <= event.pos[0] <= 75 and 75 <= event.pos[1] <=105:
                a = 'Wood'
                b = (193,154,107)
                n1 = 1.60
            if 5 <= event.pos[0] <= 75 and 110 <= event.pos[1] <= 140:
                a = 'Diamond'
                b = (185,242,255)
                n1 = 2.47
        
        
    if x != 0:
        pygame.draw.line(screen, (0,0,0), (x, y), (300,300), 2)
        theta1 = get_angle(x,y)
        x2 = 300 + 300
        y2 = 300 - (math.tan((90-theta1)*math.pi/180)*300)
        pygame.draw.line(screen, (255,0,0), (300,300),(x2,y2), 1)
        text_surface = font.render(u'x={}, y={}'.format(x, y), True, (0,0,0))
        screen.blit(text_surface, (x + 10, y+ 5))
        text_surface1 = angle_font.render(f'{theta1} deg', True, (0,0,0))
        screen.blit(text_surface1, (230, 400)) 
        
        x1,y1 = snells_law(theta1,n1,n2)
        pygame.draw.line(screen, (0,0,0), (300,300),(x1,y1), 2)
       
        
        
    pygame.display.update()
        
