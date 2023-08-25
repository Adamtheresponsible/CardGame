import pygame
from models import *
from engine import *

pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("SnaPy")

gameEngine = SnapEngine()

run = True
while run:
  key = None;
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      key = event.key

  gameEngine.play(key)
  renderGame(window)
  pygame.display.update()

  if gameEngine.state == GameState.SNAPPING:
    pygame.time.display(3000)
    gameEngine.state = GameState.PLAYING

