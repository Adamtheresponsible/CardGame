from enum import Enum
import pygame
from models.py import *

class GameState(Enum):
  PLAYING = 0
  SNAPPING = 1
  ENDED = 2

class SnapEngine:
  deck = None
  player1 = None
  player2 = None
  pile = None
  state = None
  currentPlayer = None
  recult = None

  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()
    self.player1 = Player("Player 1", pygame.K_q, pygame.K_w)
    self.player2 = Player("Player 2", pygame.K_o, pygame.K_p)
    self.pile = Pile()
    self.deal()
    self.currentPlayer = self.player1
    self.state = GameState.PLAYING

