from enum import Enum
import pygame
from models.py import *

class GameState(Enum):
  PLAYING = 0
  SNAPPING = 1
  ENDED = 2

