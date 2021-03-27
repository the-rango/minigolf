import pygame
pygame.init()
wn = pygame.display.set_mode((600,600))

HOLER = 25

xspeed = 0
yspeed = 0

x = 500
y = 500

strokes = 0
modulator = 20

sand = [(200,300,100,100),(300,400,50,50)]
waters = [(0,200,50,300)]
lwalls = [(150,0,10,300),(400,300,10,50)]
rwalls = [(250,0,10,300),(500,300,10,50)]
twalls = [(150,300,100,10),(400,300,100,10)]
bwalls = [(150,0,100,10),(400,350,100,10)]

font = pygame.font.Font('BRLNSB.TTF', 30)

while True:
  wn.fill((24,110,47))
  pygame.time.delay(10)

  pos = pygame.mouse.get_pos()

  pygame.draw.circle(wn, (255,255,255), (100,100), HOLER)
  pygame.draw.circle(wn, (0,0,0), (100,100), HOLER-1)

  # Drawing sand
  for patch in sand:
    sandbox = pygame.draw.rect(wn, (212,176,106), patch)
    # Behavior:
    if sandbox.collidepoint(x,y):
      xspeed *= 0.9
      yspeed *= 0.9

  for patch in waters:
    water = pygame.draw.rect(wn, (54,84,217), patch)
    # Behavior:
    if water.collidepoint(x,y):
      x = 500
      xspeed = 0
      y = 500
      yspeed = 0

  for wall in lwalls:
    wall = pygame.draw.rect(wn, (111,111,111), wall)
    # Behavior:
    if wall.collidepoint(x,y):
      xspeed = -1 *abs(xspeed)

  for wall in rwalls:
    wall = pygame.draw.rect(wn, (111,111,111), wall)
    # Behavior:
    if wall.collidepoint(x,y):
      xspeed = abs(xspeed)

  for wall in twalls:
    wall = pygame.draw.rect(wn, (111,111,111), wall)
    # Behavior:
    if wall.collidepoint(x,y):
      yspeed = -1 *abs(yspeed)

  for wall in bwalls:
    wall = pygame.draw.rect(wn, (111,111,111), wall)
    # Behavior:
    if wall.collidepoint(x,y):
      yspeed = abs(yspeed)


  pygame.draw.circle(wn, (255,255,255), (round(x),round(y)), 15)

  # Only draw line when stopped
  if abs(xspeed) < 0.1 and abs(yspeed) < 0.1:
    pygame.draw.line(wn, (255,165,0), (x,y), pos)

  # Hit the ball on click
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      xspeed = int((pos[0]-x)/modulator)
      yspeed = int((pos[1]-y)/modulator)
      strokes += 1

  # Move the ball
  x += xspeed
  y += yspeed

  # Deceleration
  xspeed = xspeed*0.98
  yspeed = yspeed*0.98

  # Bouncing
  if x > 584 or x < 16:
    xspeed *= -1
  if y >584 or y < 16:
    yspeed *= -1

  # Checks to see if in hole
  if ((x-100)**2+(y-100)**2)**0.5 < HOLER:
    xspeed *= 0.97
    yspeed *= 0.97
    if abs(yspeed) < 0.1 and abs(xspeed) < 0.1:
      winmsg = font.render(f'Nice! {strokes} strokes!', True, (255,255,255), (24,110,47))
      wn.blit(winmsg, (150,400))

  pygame.display.update()
