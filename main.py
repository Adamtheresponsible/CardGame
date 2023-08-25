import pygame
from models import *
from engine import *

pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("SnaPy")

gameEngine = SnapEngine()

cardBack = pygame.image.load('images/BACK.png')
cardBack = pygame.transform.scale(cardBack, (int(238*0.8), int(332*0.8)))

def renderGame(window):
  window.fill((15, 0, 169))
  font = pygame.font.SysFont('comicsans', 60, True)

  window.blit(cardBack, (100, 200))
  window.blit(cardBack, (700, 200))

  text = font.render(str(len(gameEngine.player1.hand)) + " Cards, True, (255, 255, 255)
  window.blit(cardBack, (100, 500)

  text = font.render(str(len(gameEngine.player2.hand)) + " Cards, True, (255, 255, 255)
  window.blit(cardBack, (700, 500))

  topCard = gameEngine.pile.peek()
  if (topCard != None):
    window.blit(topCard.image, (400, 200))

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

