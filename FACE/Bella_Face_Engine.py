# (Bella Face Engine)
# Version 1.0
# Then "Bella OS"
# Then "Educational Companion Robot"

import pygame
import math
import random
import time

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bella Face Prototype")

clock = pygame.time.Clock()

WHITE = (245,245,245)
BLACK = (30,30,35)
BLUE = (70,170,255)
PINK = (255,160,180)
RED = (255,90,90)
GRAY = (180,180,180)

font = pygame.font.SysFont("Segoe UI", 32)

last_mouse_move = time.time()
blink_timer = random.uniform(2,5)
blink_duration = 0
expression = "happy"

def lerp(a,b,t):
    return a+(b-a)*t

running = True

while running:

    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type == pygame.MOUSEMOTION:
            last_mouse_move=time.time()

    idle=time.time()-last_mouse_move

    if idle>8:
        expression="sleep"
    elif idle>5:
        expression="thinking"
    else:
        expression="happy"

    blink_timer-=dt

    if blink_timer<=0:
        blink_duration=0.15
        blink_timer=random.uniform(2,5)

    if blink_duration>0:
        blink_duration-=dt

    mx,my=pygame.mouse.get_pos()

    offset_x=(mx-WIDTH/2)/35
    offset_y=(my-HEIGHT/2)/35

    offset_x=max(min(offset_x,15),-15)
    offset_y=max(min(offset_y,10),-10)

    t=time.time()

    breathing=math.sin(t*2)*4

    top=(35,35,70)
    bottom=(10,10,20)

    for y in range(HEIGHT):
        ratio=y/HEIGHT
        color=(
            int(top[0]*(1-ratio)+bottom[0]*ratio),
            int(top[1]*(1-ratio)+bottom[1]*ratio),
            int(top[2]*(1-ratio)+bottom[2]*ratio)
        )
        pygame.draw.line(screen,color,(0,y),(WIDTH,y))

    face_center=(WIDTH//2,int(HEIGHT//2+breathing))

    pygame.draw.circle(screen,(245,235,220),face_center,220)

    pygame.draw.circle(screen,PINK,(face_center[0]-120,face_center[1]+70),22)
    pygame.draw.circle(screen,PINK,(face_center[0]+120,face_center[1]+70),22)

    left_eye=(face_center[0]-80,face_center[1]-40)
    right_eye=(face_center[0]+80,face_center[1]-40)

    eye_height=50

    if blink_duration>0:
        eye_height=4

    if expression=="sleep":
        eye_height=2

    pygame.draw.ellipse(screen,WHITE,(left_eye[0]-40,left_eye[1]-eye_height//2,80,eye_height))
    pygame.draw.ellipse(screen,WHITE,(right_eye[0]-40,right_eye[1]-eye_height//2,80,eye_height))

    if eye_height>8:

        pygame.draw.circle(screen,BLUE,
            (int(left_eye[0]+offset_x),int(left_eye[1]+offset_y)),15)

        pygame.draw.circle(screen,BLUE,
            (int(right_eye[0]+offset_x),int(right_eye[1]+offset_y)),15)

        pygame.draw.circle(screen,BLACK,
            (int(left_eye[0]+offset_x),int(left_eye[1]+offset_y)),7)

        pygame.draw.circle(screen,BLACK,
            (int(right_eye[0]+offset_x),int(right_eye[1]+offset_y)),7)

        pygame.draw.circle(screen,WHITE,
            (int(left_eye[0]+offset_x-3),int(left_eye[1]+offset_y-3)),3)

        pygame.draw.circle(screen,WHITE,
            (int(right_eye[0]+offset_x-3),int(right_eye[1]+offset_y-3)),3)

    if expression=="happy":

        pygame.draw.arc(screen,BLACK,
            (face_center[0]-80,face_center[1]+10,160,100),
            math.radians(20),
            math.radians(160),
            5)

    elif expression=="thinking":

        pygame.draw.arc(screen,BLACK,
            (face_center[0]-60,face_center[1]+40,120,30),
            math.radians(180),
            math.radians(360),
            3)

        txt=font.render("Thinking...",True,GRAY)
        screen.blit(txt,(WIDTH//2-txt.get_width()//2,40))

    elif expression=="sleep":

        pygame.draw.arc(screen,BLACK,
            (face_center[0]-60,face_center[1]+40,120,20),
            math.radians(180),
            math.radians(360),
            3)

        z=font.render("Z z Z",True,WHITE)
        screen.blit(z,(WIDTH//2-z.get_width()//2,50))

    eyebrow_y=left_eye[1]-55

    if expression=="thinking":
        pygame.draw.line(screen,BLACK,
                         (left_eye[0]-35,eyebrow_y),
                         (left_eye[0]+20,eyebrow_y-10),4)

        pygame.draw.line(screen,BLACK,
                         (right_eye[0]-20,eyebrow_y-10),
                         (right_eye[0]+35,eyebrow_y),4)
    else:
        pygame.draw.line(screen,BLACK,
                         (left_eye[0]-30,eyebrow_y),
                         (left_eye[0]+30,eyebrow_y),4)

        pygame.draw.line(screen,BLACK,
                         (right_eye[0]-30,eyebrow_y),
                         (right_eye[0]+30,eyebrow_y),4)

    title=font.render("Bella AI Prototype",True,WHITE)
    screen.blit(title,(20,20))

    hint=pygame.font.SysFont("Segoe UI",22).render(
        "Move the mouse • Wait 5 sec = Thinking • Wait 8 sec = Sleeping",
        True,
        (220,220,220)
    )

    screen.blit(hint,(20,60))

    pygame.display.flip()

pygame.quit()

# ===================================================================

# import pygame
# import math
# import random

# # --------------------
# # Initialization
# # --------------------
# pygame.init()

# WIDTH, HEIGHT = 1000, 700
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("BELLA AI")

# clock = pygame.time.Clock()

# # Colors
# BG = (15, 18, 35)
# CYAN = (0, 255, 255)
# BLUE = (70, 150, 255)
# WHITE = (240, 240, 240)
# PINK = (255, 120, 170)

# font_big = pygame.font.SysFont("consolas", 42, True)
# font_small = pygame.font.SysFont("consolas", 22)

# blink_timer = 0
# blink = False

# emotion = "happy"

# mouth_open = 0

# particles = []

# # --------------------
# # Particle class
# # --------------------
# class Particle:
#     def __init__(self):
#         self.x = random.randint(0, WIDTH)
#         self.y = random.randint(0, HEIGHT)
#         self.r = random.randint(1, 3)
#         self.speed = random.uniform(0.2, 1.2)

#     def update(self):
#         self.y -= self.speed
#         if self.y < 0:
#             self.y = HEIGHT
#             self.x = random.randint(0, WIDTH)

#     def draw(self):
#         pygame.draw.circle(screen, (60,120,255), (int(self.x), int(self.y)), self.r)

# for i in range(120):
#     particles.append(Particle())

# running = True

# while running:

#     dt = clock.tick(60) / 1000

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_1:
#                 emotion = "happy"

#             elif event.key == pygame.K_2:
#                 emotion = "sad"

#             elif event.key == pygame.K_3:
#                 emotion = "thinking"

#             elif event.key == pygame.K_4:
#                 emotion = "surprised"

#     # --------------------
#     # Background
#     # --------------------
#     screen.fill(BG)

#     for p in particles:
#         p.update()
#         p.draw()

#     # breathing
#     t = pygame.time.get_ticks() / 1000
#     offset = math.sin(t * 2) * 4

#     # Mouse tracking
#     mx, my = pygame.mouse.get_pos()

#     eye_left = (350, 270 + offset)
#     eye_right = (650, 270 + offset)

#     def pupil(center):

#         dx = mx - center[0]
#         dy = my - center[1]

#         dist = math.hypot(dx, dy)

#         if dist > 15:
#             dx = dx / dist * 15
#             dy = dy / dist * 15

#         return center[0] + dx, center[1] + dy

#     # Blink
#     blink_timer += dt

#     if blink_timer > random.uniform(2.5,5):
#         blink = True
#         if blink_timer > random.uniform(2.6,5.1):
#             blink = False
#             blink_timer = 0

#     # Head Glow
#     pygame.draw.circle(screen, (40,70,140), (500,350), 230)

#     pygame.draw.circle(screen, (20,40,80), (500,350), 220)

#     # Face outline
#     pygame.draw.circle(screen, CYAN, (500,350),220,4)

#     # Eyes
#     for eye in [eye_left, eye_right]:

#         if blink:
#             pygame.draw.line(screen, WHITE,
#                              (eye[0]-40,eye[1]),
#                              (eye[0]+40,eye[1]),5)
#         else:
#             pygame.draw.circle(screen, WHITE,
#                                (int(eye[0]),int(eye[1])),42)

#             px, py = pupil(eye)

#             pygame.draw.circle(screen,
#                                BLUE,
#                                (int(px),int(py)),18)

#             pygame.draw.circle(screen,
#                                WHITE,
#                                (int(px-5),int(py-5)),4)

#     # Eyebrows
#     if emotion=="happy":

#         pygame.draw.arc(screen,CYAN,(290,180,120,60),0.2,2.8,4)
#         pygame.draw.arc(screen,CYAN,(590,180,120,60),0.2,2.8,4)

#     elif emotion=="sad":

#         pygame.draw.line(screen,CYAN,(300,220),(390,180),4)
#         pygame.draw.line(screen,CYAN,(610,180),(700,220),4)

#     elif emotion=="thinking":

#         pygame.draw.line(screen,CYAN,(300,180),(390,200),4)
#         pygame.draw.line(screen,CYAN,(610,200),(700,180),4)

#     elif emotion=="surprised":

#         pygame.draw.arc(screen,CYAN,(290,160,120,40),3.2,6.0,4)
#         pygame.draw.arc(screen,CYAN,(590,160,120,40),3.2,6.0,4)

#     # Mouth animation
#     mouth_open = abs(math.sin(t*7))*18

#     if emotion=="happy":

#         pygame.draw.arc(screen,
#                         PINK,
#                         (380,380,240,120),
#                         0.3,
#                         2.8,
#                         5)

#     elif emotion=="sad":

#         pygame.draw.arc(screen,
#                         PINK,
#                         (380,440,240,80),
#                         3.4,
#                         6.0,
#                         5)

#     elif emotion=="thinking":

#         pygame.draw.line(screen,
#                          PINK,
#                          (420,430),
#                          (580,430),
#                          5)

#     elif emotion=="surprised":

#         pygame.draw.circle(screen,
#                            PINK,
#                            (500,430),
#                            int(18+mouth_open),
#                            4)

#     # HUD
#     title = font_big.render("BELLA AI",True,CYAN)
#     screen.blit(title,(30,30))

#     text = font_small.render(
#         "1 Happy   2 Sad   3 Thinking   4 Surprised",
#         True,
#         WHITE)

#     screen.blit(text,(30,90))

#     status = font_small.render(
#         f"Emotion : {emotion.upper()}",
#         True,
#         CYAN)

#     screen.blit(status,(30,125))

#     # Scanning line
#     y = int((math.sin(t*0.8)+1)/2*HEIGHT)
#     pygame.draw.line(screen,(0,120,255),(0,y),(WIDTH,y),1)

#     pygame.display.flip()

# pygame.quit()