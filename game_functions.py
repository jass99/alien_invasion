import sys
import pygame

from bullet import Bullet



def check_keydown_events(event,ai_settings,screen,ship,bullets):
    
    if event.key == pygame.K_RIGHT:
                    
        ship.moving_right = True
                    
    if event.key == pygame.K_LEFT:
                    
        ship.moving_left = True
        
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
                    
                    
def check_keyup_events(event,ship):
    
    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False            
                    
    if event.key == pygame.K_LEFT:
                    
        ship.moving_left = False



def check_events(ai_settings,screen,ship,bullets):
    
    for event in pygame.event.get():
            # event gets any input from mouse or keyboard
            # any mouse or keyboard input will make this for loop to run
            
            if event.type == pygame.QUIT:
                
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                
                check_keydown_events(event,ai_settings,screen,ship,bullets)
            
            if event.type == pygame.KEYUP:
            
                check_keyup_events(event,ship)

           
            
            
def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()    
    pygame.display.flip()