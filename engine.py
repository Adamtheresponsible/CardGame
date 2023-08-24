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

  def deal(self):
    half = self.deck.length() // 2
    for i in range(0, half):
      self.player1.draw(self.deck)
      self.player2.draw(self.deck)

  def switchPlayer(self):
    if self.currentPlayer == self.player1:
      self.currentPlayer == self.player2
    else:
      self.currentPlayer = self.player2

  def winRound(self, player):
    self.state = GameState.SNAPPING
    player.hand.extend(self.pile.popAll())
    self.pile.clear()

  def play(self, key):
    if key == None
      return

    if self.state == GameState.ENDED:
      return
      
