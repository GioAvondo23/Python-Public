import board
import os
b1 = board.Board((8, 8))
repboard = board.Board((8, 8))
repboard05 = board.Board((8, 8))
repboard1 = board.Board((8, 8))
repboard15 = board.Board((8, 8))
repboard2 = board.Board((8, 8))
repboard25 = board.Board((8, 8))
repboard3 = board.Board((8, 8))

print('no')
def Check(matrix, item):
  for z in matrix:
    if isinstance(z, tuple) == True:
      for i in matrix:
        if matrix[i] == item:
          return i
      return False
  try:
    for i in matrix:
      count = 0
      for n in i:
        if n == item:
          return (matrix.index(i),count)
        count = count + 1
    return None
  except:
    return False
def Find(matrix, pos):
  for i in matrix:
    if isinstance(i, tuple) == True:
      return matrix[pos]
  count = 0
  for row in matrix:
    if count == pos[0]:
      count = 0
      for item in row:
        if count == pos[1]:
          return item
        count = count + 1
    count = count + 1
  return False
def Swap(board, row1, row2, pos1='board', pos2 = 'board'):
  if pos1 != 'board' and pos2 != 'board':
    buffer1 = 'hi'
    smaller = min(row1,row2)
    bigger = max(row1,row2)
    if smaller == row1:
      position1 = pos1
      position2 = pos2
    elif smaller == row2:
      position1 = pos2
      position2 = pos1
    for i in range(2):
      count = 0
      for row in board:
        if count == smaller:
          count1 = 0
          for item in row:
            if count1 == position1:
              row[count1], buffer1 = buffer1, row[count1]
              if i == 1:
                return board
            count1 = count1 + 1
        elif count == bigger:
          count1 = 0
          for item in row:
            if count1 == position2:
              row[count1], buffer1 = buffer1, row[count1]
            count1 = count1 + 1
        count = count + 1
      
  elif pos1 == 'board' and pos2 == 'board':
    board[row1], board[row2] = board[row2], board[row1]
    return board
knight = [
'___________________',
'|   ||||__        |',
'|   -  ˚   \____  |',
'|   -         __\ |',
'|   -        |__  |',
'|   -   _______/  |',
'|   |    \        |', 
'|   |     \       |',
'|   |      \__    |',
'|   |_________|   |'
]
pawn = [
'___________________',
'|      __O__      |',
'|     /     \     |',
'|    |       |    |',
'|     \     /     |',
'|      |   |      |',
'|      |   |      |',
'|   ___|   |___   |',
'|  [___________]  |',
'|                 |'
]
bishop = [
'___________________',
'|      __O_       |',
'|    /    / /\    |',
'|   |    / /  |   |',
'|   |    \/   |   |',
'|    \__   __/    |',
'|      |   |      |',
'|      |   |      |',
'|   ___|   |___   |',
'|  [___________]  |'
]
rook = [
'___________________',
'|   __  __  __    |',
'|  |  ||  ||  |   |',
'|   \        /    |',
'|    |      |     |',
'|    |      |     |',
'|    |      |     |',
'|    |      |     |',
'|  __|      |__   |', 
'| [____________]  |'
]
queen = [
'___________________',
'|_O_    _O_    _O_|',
'|  _|   | |   |_  |', 
'\ \     | |     / /',
'|\ \    | |    / /|',
'| \ \   | |   / / |',
'|  \ \  | |  / /  |',
'|   \ \ | | / /   |',
'|    \ \| |/ /    |',
'|     \_____/     |'
]
king = [
'___________________',
'|       |||       |',
'|    ≈≈≈|||≈≈≈    |',
'|      _|||_      |',
'| __  /_   _\  __ |',
' /  \  |   |  /  \|',
'|    |/     \|    |',
' \               /|',
'| \_____________/ |',
'|  |___________|  |',
]
bknight = [
'___________________',
'|   ||||__        |',
'|   -  ˚   \____  |',
'|   -         __\ |',
'|   -        |__  |',
'|   -   _______/  |',
'|   |||||\        |', 
'|   ||B|||\       |',
'|   |||||||\__    |',
'|   |_________|   |'
]
bpawn = [
'___________________',
'|      __O__      |',
'|     /|||||\     |',
'|    |||||||||    |',
'|     \ ||| /     |',
'|      |||||      |',
'|      | B |      |',
'|   ___|||||___   |',
'|  [___________]  |',
'|                 |'
]
bbishop = [
'___________________',
'|      __O_       |',
'|    ////// /\    |',
'|   |///// ///|   |',
'|   |////\////|   |',
'|    \__|||__/    |',
'|      |||||      |',
'|      | B |      |',
'|   ___|||||___   |',
'|  [___________]  |'
]
brook = [
'___________________',
'|   __  __  __    |',
'|  |  ||  ||  |   |',
'|   \        /    |',
'|    ||||||||     |',
'|    ||||||||     |',
'|    |   B  |     |',
'|    ||||||||     |',
'|  __||||||||__   |', 
'| [____________]  |'
]
bqueen = [
'___________________',
'|_O_    _O_    _O_|',
'|  _|   |||   |_  |', 
'\ \     |||     ///',
'|\ \    |||    ///|',
'| \ \   |||   /// |',
'|  \ \  |||  ///  |',
'|   \ \ ||| ///   |',
'|    \ \|||///    |',
'|     \__B__/     |'
]
bking = [
'___________________',
'|       |||       |',
'|    ≈≈≈|||≈≈≈    |',
'|      _|||_      |',
'| __  /_   _\  __ |',
'|/||\  |||||  /||\|',
'||||||/  B  \|||| |',
'|\ ||||||||||||| /|',
'| \_____________/ |',
'|  |___________|  |'
]
extra = [
'___________________',
'|                 |',
'|                 |',
'|                 |',
'|                 |',
'|                 |',
'|                 |',
'|                 |',
'|                 |',
'|                 |'      
]
squares = [
  ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
  ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
  ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
  ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
  ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
  ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
  ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
  ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
]
drawcombs = [
  ['king','bking'],
  ['king','bking','knight'],
  ['king','bking','bknight'],
  ['king','bking','ishop'],
  ['king','bking','bbishop'],
  ['king','bking','ishop','bbishop'],
  ['king','bking','bbishop','ishop']
]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
taken = []
pieces = ['rook', 'knight', 'ishop', 'queen', 'king', 'pawn', 'brook', 'bknight', 'bbishop', 'bqueen', 'bking', 'bpawn', '']
dpieces = ['king', 'bking', 'knight', 'bknight', 'ishop', 'bbishop']
altpos = [0, 1, 2, 2, 2, 2]
moved = []
def Reverse(tuples): 
    new_tup = tuples[::-1] 
    return new_tup 
contr_pieces = [rook, knight, bishop, queen, king, pawn, brook, bknight, bbishop, bqueen, bking, bpawn, extra]
board = [
  [brook, bknight, bbishop, bqueen, bking, bbishop, bknight, brook],
  [bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn],
  [extra, extra,extra, extra,extra, extra,extra, extra],
  [extra, extra,extra, extra,extra, extra,extra, extra],
  [extra, extra,extra, extra,extra, extra,extra, extra],
  [extra, extra,extra, extra,extra, extra,extra, extra],
  [pawn, pawn, pawn, pawn, pawn, pawn, pawn, pawn],
  [rook, knight, bishop, queen, king, bishop, knight, rook]
]

countee = 0
for i in board:
  for num in range(8):
    b1[num,countee] = pieces[contr_pieces.index(i[num])]
  countee = countee + 1
#for i in b1:
  #if b1[i] != 'king' and b1[i] != 'bking' and b1[i] != 'queen':
    #b1[i] = ''

bkin = 0
wkin = 0
brooki = [0,0]
wrooki = [0,0]
positions = [(0,7),(7,7),(0,0),(0,7)]
kpos = [(4,0),(4,7)]
def Rookie(current, after, turn, block = 'stop', squares = squares, wkin = wkin, bkin = bkin):
  position = Reverse(Check(squares,current))
  nextpos = Reverse(Check(squares,after))
  moves = [(0,1),(0,-1),(1,0),(-1,0)]
  if block != 'stop':
    n = 0
    for i in moves:
      if 8>(position[0] + i[1]) >= 0 and 8>(position[1] + i[0]) >= 0:
        try:
          item = Find(b1,(position[0] + i[1], position[1] + i[0]))
          if item == '':
            pass
          elif turn == 'white':
            if item[0] != 'b':
              n = n + 1
          elif turn == 'black':
            if item[0] == 'b':
              n = n + 1
        except:
          n = n + 1
      else:
        n = n + 1
    if n == 4:
      return '\nRook is blocked: Please try again: \n'
    else:
      return True
  x = nextpos[0] - position[0]
  y = nextpos[1] - position[1]
  cont = 'no'
  if x == 0:
    if y > 0:
      for i in range(1,y):
        item = Find(b1,(position[0],position[1]+i))
        if item != '':
          return '\nRook is blocked: Please try again: \n'
      item = Find(b1,(position[0], position[1] + y))
      if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nRook cannot move to this position: Please try again: \n'
      elif turn == 'black':
        if item != '' and item[0] == 'b':
          return '\nRook cannot move to this position: Please try again: \n'
    elif y < 0:
      for i in range(1,(-1*y)):
        item = Find(b1,(position[0],position[1]-i))
        if item != '':
          return '\nRook is blocked: Please try again: \n'
      item = Find(b1,(position[0], position[1] + y))
      if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nRook cannot move to this position: Please try again: \n'
      elif turn == 'black':
        if item != '' and item[0] == 'b':
          return '\nRook cannot move to this position: Please try again: \n'
    cont = 'yes'
  if y == 0:
    if x > 0:
      for i in range(1,x):
        item = Find(b1,(position[0]+i,position[1]))
        if item != '':
          return '\nRook is blocked: Please try again: \n'
      item = Find(b1,(position[0]+x, position[1]))
      if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nRook cannot move to this position: Please try again: \n'
      elif turn == 'black':
        if item != '' and item[0] == 'b':
          return '\nRook cannot move to this position: Please try again: \n'
    elif x < 0:
      for i in range(1,(-1*x)):
        item = Find(b1,(position[0]-i,position[1]))
        if item != '':
          return '\nRook is blocked: Please try again: \n'
      item = Find(b1,(position[0]+x, position[1]))
      if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nRook cannot move to this position: Please try again: \n'
      elif turn == 'black':
        if item != '' and item[0] == 'b':
          return '\nRook cannot move to this position: Please try again: \n'
    cont = 'yes'
  indeces = [0,1,0,1]
  if cont == 'yes':
    try:
      pos = positions.index(position)
      pos1 = indeces[pos]
      if turn == 'white':
        wrooki[pos1] = wrooki[pos1]+1
      elif turn == 'black':
        brooki[pos1] = brooki[pos1]+1
    except:
      pass
    return True
  return '\nRook cannot move to this position: Please try again: \n'
pastc = 'a1'
pasta = 'a2'
def Pawn(current, after, turn, block = 'stop', wkin = wkin, bkin = bkin, squares = squares, b1=b1):
  position = Reverse(Check(squares,current))
  nextpos = Reverse(Check(squares,after))
  if block != 'stop':
    if turn == 'white':
      moves = [-1, (-1,-1), (1,-1)]
      n = 0
      for i in moves:
        if isinstance(i, tuple) == True:
          try:
            nextpos = position[0]+i[0], position[1]+i[1]
            item = Find(b1,(position[0]+i[0], position[1]+i[1]))
            if item == '':
              if nextpos == (position[0]+1, position[1]-1):
                nexto = Find(squares, (position[1], position[0]+1))
                if nexto == pasta:
                  dig1 = int(pastc[1])
                  dig2 = int(pasta[1])
                  if Find(b1, Reverse(Check(squares, nexto))) == 'bpawn':
                    if (dig1-2) == dig2:
                      pos = (position[0]+1, position[1])
                      n = n - 1
                n = n + 1
              elif nextpos == (position[0]-1, position[1]-1):
                nexto = Find(squares, (position[1], position[0]-1))
                if nexto == pasta:
                  dig1 = int(pastc[1])
                  dig2 = int(pasta[1])
                  if Find(b1, Reverse(Check(squares, nexto))) == 'bpawn':
                    if (dig1-2) == dig2:
                      pos = (position[0]-1, position[1])
                      n = n - 1
                n = n + 1
            elif item[0] != 'b':
              n = n + 1
          except:
            n = n + 1
        else:
          item = Find(b1,(position[0], position[1]+i))
          if item != '':
            n = n + 1
      if n == 3:
        return '\nPawn is blocked: Choose a different piece: \n'
      else:
        return True
    if turn == 'black':
      moves = [1, (1,1), (-1,1)]
      n = 0
      for i in moves:
        if isinstance(i, tuple) == True:
          try:
            nextpos = position[0]+i[0], position[1]+i[1]
            item = Find(b1,(position[0]+i[0], position[1]+i[1]))
            if item == '':
              if nextpos == (position[0]+1, position[1]-1):
                nexto = Find(squares, (position[1], position[0]+1))
                if nexto == pasta:
                  dig1 = int(pastc[1])
                  dig2 = int(pasta[1])
                  if Find(b1, Reverse(Check(squares, nexto))) == 'bpawn':
                    if (dig1-2) == dig2:
                      pos = (position[0]+1, position[1])
                      n = n - 1
                n = n + 1
              elif nextpos == (position[0]-1, position[1]-1):
                nexto = Find(squares, (position[1], position[0]-1))
                if nexto == pasta:
                  dig1 = int(pastc[1])
                  dig2 = int(pasta[1])
                  if Find(b1, Reverse(Check(squares, nexto))) == 'bpawn':
                    if (dig1-2) == dig2:
                      pos = (position[0]-1, position[1])
                      n = n - 1
                n = n + 1
            elif item[0] == 'b':
              n = n + 1
          except:
            n = n + 1
        else:
          item = Find(b1,(position[0], position[1]+i))
          if item != '':
            n = n + 1
      if n == 3:
        return '\nPawn is blocked: Choose a different piece: \n'
      else:
        return True
  if nextpos[0] == position[0]:
    if turn == 'white':
      x = position[1] - nextpos[1]
      if current[1] != '2':
        if x == 1:
          if Find(b1, (position[0], position[1]-1)) != '':
            return '\nPawn is blocked: Please try again: \n'
        elif x<=0 or x>1:
          return '\nPawn cannot move to this position: Please try again: \n'
      else:
        if x == 2:
          if Find(b1, (position[0], position[1]-2)) != '' or Find(b1, (position[0], position[1]-1)) != '':
            return '\nPawn is blocked: Please try again: \n'
        elif x == 1: 
          if Find(b1, (position[0], position[1]-1)) != '':
            return '\nPawn is blocked: Please try again: \n'
        else:
          return '\nPawn cannot move to this position: Please try again: \n'
      return True
    elif turn == 'black':
      x = nextpos[1]-position[1]
      if current[1] !='7':
        if x == 1:
          if Find(b1, (position[0], position[1]+1)) != '':
            return '\nPawn is blocked: Please try again: \n'
        elif x<=0 or x>1:
          return '\nPawn cannot move to this position: Please try again: \n'
      else:
        if x == 2:
          if Find(b1, (position[0], position[1]+2)) != '' or Find(b1, (position[0], position[1]+1)) != '':
            return '\nPawn is blocked: Please try again: \n'
        elif x == 1: 
          if Find(b1, (position[0], position[1]+1)) != '':
            return '\nPawn is blocked: Please try again: \n'
        else:
          return '\nPawn cannot move to this position: Please try again: \n'
      return True
  elif nextpos[0] != position[0]:
    if turn == 'white':
      if nextpos == (position[0]+1, position[1]-1) or nextpos == (position[0]-1, position[1]-1):
        item = Find(b1, nextpos)  
        try:
          if item == '':
            if nextpos == (position[0]+1, position[1]-1):
              nexto = Find(squares, (position[1], position[0]+1))
              if nexto == pasta:
                dig1 = int(pastc[1])
                dig2 = int(pasta[1])
                if Find(b1, Reverse(Check(squares, nexto))) == 'bpawn':
                  if (dig1-2) == dig2:
                    pos = (position[0]+1, position[1])
                    b1 = Swap(b1,pos,nextpos)
                    return True
              return '\nEn passant is not possible: Please try again\n'
            elif nextpos == (position[0]-1, position[1]-1):
              nexto = Find(squares, (position[1], position[0]-1))
              if nexto == pasta:
                dig1 = int(pastc[1])
                dig2 = int(pasta[1])
                if Find(b1, Reverse(Check(squares, nexto))) == 'bpawn':
                  if (dig1-2) == dig2:
                    pos = (position[0]-1, position[1])
                    b1 = Swap(b1,pos,nextpos)
                    return True
              return '\nEn passant is not possible: Please try again\n'
          elif item[0] != 'b':
            return '\nPawn cannot move to this position: Please try again: \n'
        except:
          return '\nPawn cannot move to this position: Please try again: \n'
        return True
    elif turn == 'black':
      if nextpos == (position[0]+1, position[1]+1) or nextpos == (position[0]-1, position[1]+1):
        item = Find(b1, nextpos)
        try:
          if item == '':
            if nextpos == (position[0]+1, position[1]+1):
              nexto = Find(squares, (position[1], position[0]+1))
              if nexto == pasta:
                dig1 = int(pastc[1])
                dig2 = int(pasta[1])
                if Find(b1, Reverse(Check(squares, nexto))) == 'pawn':
                  if (dig1+2) == dig2:
                    pos = (position[0]+1, position[1])
                    b1 = Swap(b1,pos,nextpos)
                    return True
              return '\nEn passant is not possible: Please try again\n'
            elif nextpos == (position[0]-1, position[1]+1):
              nexto = Find(squares, (position[1], position[0]-1))
              if nexto == pasta:
                dig1 = int(pastc[1])
                dig2 = int(pasta[1])
                if Find(b1, Reverse(Check(squares, nexto))) == 'pawn':
                  if (dig1+2) == dig2:
                    pos = (position[0]-1, position[1])
                    b1 = Swap(b1,pos,nextpos)
                    return True
              return '\nEn passant is not possible: Please try again\n'
          elif item[0] == 'b':
            return '\nPawn cannot move to this position: Please try again: \n'
        except:
          return '\nPawn cannot move to this position: Please try again: \n'
        return True
  return '\nPawn cannot move to this position: Please try again: \n'

def Knight(current, after, turn, blocked = 'stop', wkin = wkin, bkin = bkin):
  position = Reverse(Check(squares,current))
  nextpos = Reverse(Check(squares,after))
  moves = [(-2,1), (-2,-1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]
  if blocked != 'stop':
    n = 0
    for i in moves:
      if 8>position[0] + i[1] >= 0 and 8>position[1] + i[0] >= 0:
        try:
          item = Find(b1,(position[0] + i[1], position[1] + i[0]))
          if item == '':
            pass
          elif turn == 'white':
            if item[0] != 'b':
              n = n + 1
          elif turn == 'black':
            if item[0] == 'b':
              n = n + 1
        except:
          n = n + 1
      else:
        n = n + 1
    if n == 8:
      return '\nKnight is blocked: Please try again: \n'
    else:
      return True
  if turn == 'white':
    x = nextpos[0] - position[0]
    y = nextpos[1] - position[1]
    try:
      pos = moves.index((y,x))
      item = Find(b1, (position[0] + x, position[1] + y))
      if item == '':
        return True
      elif item[0] == 'b':
        return True
    except:
      return '\nKnight cannot move to this position: Please try again: \n'
  elif turn == 'black':
    x = nextpos[0] - position[0]
    y = nextpos[1] - position[1]
    try:
      pos = moves.index((y,x))
      item = Find(b1, (position[0] + x, position[1] + y))
      if item == '':
        return True
      elif item[0] != 'b':
        return True
    except:
      return '\nKnight cannot move to this position: Please try again: \n'
  return '\nKnight cannot move to this position: Please try again: \n'
def Bishop(current, after, turn, blockade = 'stop', wkin = wkin, bkin = bkin):
  position = Reverse(Check(squares,current))
  nextpos = Reverse(Check(squares,after))
  moves = [(1,1),(1,-1),(-1,1),(-1,-1)]
  if blockade != 'stop':
    n = 0
    for i in moves:
      if 8>position[0] + i[1] >= 0 and 8>position[1] + i[0] >= 0:
        try:
          item = Find(b1,(position[0] + i[1], position[1] + i[0]))
          if item == '':
            pass
          elif turn == 'white':
            if item[0] != 'b':
              n = n + 1
          elif turn == 'black':
            if item[0] == 'b':
              n = n + 1
        except:
          n = n + 1
      else:
        n = n + 1
    if n == 4:
      return '\nBishop is blocked: Please try again: \n'
    else:
      return True
  x = nextpos[0] - position[0]
  y = nextpos[1] - position[1]
  if y!=0 and x/y == 1:
    if x > 0:
      for i in range(1,x):
        item = Find(b1, (position[0] + i, position[1] + i))
        if item != '':
          return '\nBishop is blocked: Please try again: \n'
    elif x < 0:
      for i in range(1,(x*-1)):
        item = Find(b1, (position[0] - i, position[1] - i))
        if item != '':
          return '\nBishop is blocked: Please try again: \n'
    item = Find(b1, (position[0] + x, position[1] + y))
    if turn == 'white':
      if item != '' and item[0] != 'b':
        return '\nBishop cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nBishop cannot move to this position: Please try again: \n'
    return True
  elif y!=0 and x/y == -1:
    if x > 0:
      for i in range(1,x):
        item = Find(b1, (position[0] + i, position[1] - i))
        if item != '':
          return '\nBishop is blocked: Please try again: \n'
    if y > 0:
      for i in range(1,y):
        item = Find(b1, (position[0] - i, position[1] + i))
        if item != '':
          return '\nBishop is blocked: Please try again: \n'
    item = Find(b1, (position[0] + x, position[1] + y))
    if turn == 'white':
      if item != '' and item[0] != 'b':
        return '\nBishop cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nBishop cannot move to this position: Please try again: \n'
    return True
  return '\nBishop cannot move to this position: Please try again\n' 

def Queen(current, after, turn, blockade = 'stop', wkin = wkin, bkin = bkin):
  position = Reverse(Check(squares,current))
  nextpos = Reverse(Check(squares,after))
  moves = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
  if blockade != 'stop':
    n = 0
    for i in moves:
      if 8>position[0] + i[1] >= 0 and 8>position[1] + i[0] >= 0:
        try:
          item = Find(b1,(position[0] + i[1], position[1] + i[0]))
          if item == '':
            pass
          elif turn == 'white':
            if item[0] != 'b':
              n = n + 1
          elif turn == 'black':
            if item[0] == 'b':
              n = n + 1
        except:
          n = n + 1
      else:
        n = n + 1
    if n == 8:
      return '\nQueen is blocked: Please try again: \n'
    else:
      return True
  x = nextpos[0] - position[0]
  y = nextpos[1] - position[1]
  if x == 0:
    if y > 0:
      for i in range(1,y):
        item = Find(b1, (position[0], position[1] + i))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    elif y < 0:
      for i in range(1,(y*-1)):
        item = Find(b1, (position[0], position[1] - i))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    item = Find(b1, (position[0] + x, position[1] + y))
    if turn == 'white':
      if item != '' and item[0] != 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    return True
  if y == 0:
    if x > 0:
      for i in range(1,x):
        item = Find(b1, (position[0]+i, position[1]))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    elif x < 0:
      for i in range(1,(x*-1)):
        item = Find(b1, (position[0]-1, position[1]))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    item = Find(b1, (position[0] + x, position[1] + y))
    if turn == 'white':
      if item != '' and item[0] != 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    return True
  elif x/y == 1:
    if x > 0:
      for i in range(1,x):
        item = Find(b1, (position[0] + i, position[1] + i))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    elif x < 0:
      for i in range(1,(x*-1)):
        item = Find(b1, (position[0] - i, position[1] - i))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    item = Find(b1, (position[0] + x, position[1] + y))
    if turn == 'white':
      if item != '' and item[0] != 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    return True
  elif x/y == -1:
    if x > 0:
      for i in range(1,x):
        item = Find(b1, (position[0] + i, position[1] - i))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    if y > 0:
      for i in range(1,y):
        item = Find(b1, (position[0] - i, position[1] + i))
        if item != '':
          return '\nQueen is blocked: Please try again: \n'
    item = Find(b1, (position[0] + x, position[1] + y))
    if turn == 'white':
      if item != '' and item[0] != 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nQueen cannot move to this position: Please try again: \n'
    return True
  return '\nQueen cannot move to this position: Please try again: \n'

sofar = [Rookie, Knight, Bishop, Queen, 'king', Pawn, Rookie, Knight, Bishop, Queen, 'bking', Pawn]
def King(current, after, turn, blocked = 'stop', wkin = wkin, bkin = bkin):
  position = Reverse(Check(squares,current))
  nextpos = Reverse(Check(squares,after))
  moves = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
  if blocked != 'stop':
    n = 0
    old = -1
    for i in moves:
      if n - old > 1:
        n = n - 1
      old = n
      c = 0
      if 8>position[0]+i[0] >= 0 and 8>position[1] + i[1] >= 0:
        try:
          item = Find(b1,(position[0] + i[0], position[1] + i[1]))
          if item == '':
            c = c + 1
          elif turn == 'white':
            if item[0] != 'b':
              n = n + 1
            else:
              c = c + 1
          elif turn == 'black':
            if item[0] == 'b':
              n = n + 1
            else:
              c = c + 1
          else:
            c = c + 1
        except:
          n = n + 1
        if c > 0:
          oggy = (position[0]+i[0],position[1]+i[1])
          used = b1[oggy]
          b1[oggy] = ''
          if turn == 'white':
            for row in squares:
              for z in row:
                itemi = Find(b1,Reverse(Check(squares,z)))
                if itemi == 'bking':
                  posi = (position[0]+i[0],position[1]+i[1])
                  nextpos1 = Reverse(Check(squares,z))
                  x = nextpos1[0]-posi[0]
                  y = nextpos1[1]-posi[1]
                  if (-2<x<2 and -2<y<2):
                    n = n + 1
                    break
                    break
                elif itemi == 'bpawn':
                  pos1 = (position[0]+i[0], position[1]+i[1])
                  after1 = Find(squares, Reverse(pos1))
                  b1[position], b1[pos1] = b1[pos1], b1[position]
                  if Pawn(z, after1, 'black') == True:
                    b1[position], b1[pos1] = b1[pos1], b1[position]
                    n = n + 1
                    break
                    break
                  b1[position], b1[pos1] = b1[pos1], b1[position]
                elif itemi != '' and itemi != 'bking' and itemi[0] == 'b':
                  after1 = Find(squares,(position[1]+i[1],position[0]+i[0]))
                  current1 = z
                  piecepos = pieces.index(Find(b1,Reverse(Check(squares, current1))))
                  if sofar[piecepos](current1,after1,'black') == True:
                    n = n + 1
                    b1[oggy], b1[position] = b1[position], b1[oggy]
                    b1[oggy] = used
                    break
                    break
                  b1[oggy], b1[position] = b1[position], b1[oggy]
                  b1[oggy] = used
          elif turn == 'black':
              for row in squares:
                for z in row:
                  itemi = Find(b1,Reverse(Check(squares,z)))
                  if itemi == 'king':
                    posi = (position[0]+i[0],position[1]+i[1])
                    nextpos1 = Reverse(Check(squares,z))
                    x = nextpos1[0]-posi[0]
                    y = nextpos1[1]-posi[1]
                    if (-2<x<2 and -2<y<2):
                      n = n + 1
                      break
                      break  
                  elif itemi == 'pawn':
                    pos1 = (position[0]+i[0], position[1]+i[1])
                    after1 = Find(squares, Reverse(pos1))
                    b1[position], b1[pos1] = b1[pos1], b1[position]
                    if Pawn(z, after1, 'white') == True:
                      b1[position], b1[pos1] = b1[pos1], b1[position]
                      n = n + 1
                      break
                      break
                    b1[position], b1[pos1] = b1[pos1], b1[position]
                  elif itemi != '' and itemi != 'king' and itemi[0] != 'b':
                    after1 = Find(squares,(position[1]+i[1],position[0]+i[0]))
                    current1 = z
                    piecepos = pieces.index(Find(b1,Reverse(Check(squares, current1))))
                    if sofar[piecepos](current1,after1,'white') == True:
                      print(piecepos)
                      input()
                      b1[oggy] = used
                      n = n + 1
                      break
                      break
              b1[oggy] = used
      else:
        n = n + 1
    if n == 8:
      return '\nKing is blocked: Please try again: \n'
    else:
      return True
  x = nextpos[0]-position[0]
  y = nextpos[1]-position[1]
  c = 0
  d = 0
  confirm = 'no'
  if x == 0:
    if y == 1 or y == -1:
      confirm = 'yes'
      item = Find(b1,(position[0],position[1]+y))
      if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nKing cannot move to this position: Please try again: \n'
      elif turn == 'black':
        if item != '' and item[0] == 'b':
          return '\nKing cannot move to this position: Please try again: \n'
    c = y
  elif y == 0:
    if x == 1 or x == -1:
      confirm = 'yes'
      item = Find(b1,(position[0]+x,position[1]))
      if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nKing cannot move to this position: Please try again: \n'
      elif turn == 'black':
        if item != '' and item[0] == 'b':
          return '\nKing cannot move to this position: Please try again: \n'
    d = x
  elif x/y == 1 and (x == 1 or x == -1):
    confirm = 'yes'
    item = Find(b1,(position[0]+x,position[1]+y))
    if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nKing cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nKing cannot move to this position: Please try again: \n'
    c = y
    d = x
  elif x/y == -1 and (x == 1 or y == 1):
    confirm = 'yes'
    item = Find(b1,(position[0]+x,position[1]+y))
    if turn == 'white':
        if item != '' and item[0] != 'b':
          return '\nKing cannot move to this position: Please try again: \n'
    elif turn == 'black':
      if item != '' and item[0] == 'b':
        return '\nKing cannot move to this position: Please try again: \n'
    c = y
    d = x
  if y == 0 and x == 2:
    if Checkie(turn) != True:
      return '\nKing cannot castle out of Check\n'
    if turn == 'white':
      if wkin == 0 and wrooki[1] == 0:
        wkin = wkin + 1
        for i in range(1,3):
          item = Find(b1,(position[0]+i,position[1]))
          sq = Find(squares,(position[1],position[0]+i))
          if item == '':
            for row in squares:
              for z in row:
                item1 = Find(b1,Reverse(Check(squares,z)))
                if item1 == 'bking':
                  position1 = Reverse(Check(squares,z))
                  nextpos1 = (position[0]+2,position[1])
                  x = nextpos1[0]-position1[0]
                  y = nextpos1[1]-position1[1]
                  if (-2<x<2 and -2<y<2):
                    return '\nKing cannot castle close to another King: Please try again\n'
                elif item1 == 'bpawn':
                  pos1 = (position[0]+i,position[1])
                  b1[position], b1[pos1] = b1[pos1], b1[position]
                  if Pawn(z, sq, 'black') == True:
                    b1[position], b1[pos1] = b1[pos1], b1[position]
                    return '\nKing cannot castle through/into Check: Please try again: \n'
                elif item1 != '' and item1 != 'bking' and item1[0] == 'b':
                  piecepos = pieces.index(item1)
                  if sofar[piecepos](z, sq, 'black') == True:
                    return '\nKing cannot castle through/into Check: Please try again: \n'
          else:
            return '\nObstruction: King cannot castle!\n'
        wkin = wkin + 1
        return 2
      else:
        return '\nKing/Rook has already moved: Please try again: \n'
    elif turn == 'black':
      if bkin == 0 and brooki[1] == 0:
        bkin = bkin + 1
        for i in range(1,3):
          item = Find(b1,(position[0]+i,position[1]))
          sq = Find(squares,(position[1],position[0]+i))
          if item == '':
            for row in squares:
              for z in row:
                item1 = Find(b1,Reverse(Check(squares,z)))
                if item1 == 'king':
                  position1 = Reverse(Check(squares,z))
                  nextpos1 = (position[0]+2,position[1])
                  x = nextpos1[0]-position1[0]
                  y = nextpos1[1]-position1[1]
                  if (-2<x<2 and -2<y<2):
                    return '\nKing cannot castle close to another King: Please try again\n'
                elif item1 == 'pawn':
                  pos1 = (position[0]+i,position[1])
                  b1[position], b1[pos1] = b1[pos1], b1[position]
                  if Pawn(z, sq, 'white') == True:
                    b1[position], b1[pos1] = b1[pos1], b1[position]
                    return '\nKing cannot castle through/into Check: Please try again: \n'
                elif item1 != '' and item1 != 'king' and item1[0] != 'b':
                  piecepos = pieces.index(item1)
                  if sofar[piecepos](z, sq, 'white') == True:
                    return '\nKing cannot castle through/into Check: Please try again: \n'
          else:
            return '\nObstruction: King cannot castle!\n'
        bkin = bkin + 1
        return 3
      else:
        return '\nKing/Rook has already moved: Please try again: \n'
  elif y == 0 and x == -2:
    if Checkie(turn) != True:
      return '\nKing Cannot castle out of Check\n'
    if turn == 'white':
      if wkin == 0 and wrooki[0] == 0:
        wkin = wkin + 1
        for i in range(1,4):
          item = Find(b1,(position[0]-i,position[1]))
          sq = Find(squares,(position[1],position[0]-i))
          if item == '':
            for row in squares:
              for z in row:
                item1 = Find(b1,Reverse(Check(squares,z)))
                if item1 == 'bking':
                  position1 = Reverse(Check(squares,z))
                  nextpos1 = (position[0]-2,position[1])
                  x = nextpos1[0]-position1[0]
                  y = nextpos1[1]-position1[1]
                  if (-2<x<2 and -2<y<2):
                    return '\nKing cannot castle close to another King: Please try again\n'
                elif item1 == 'bpawn':
                  pos1 = (position[0]-i,position[1])
                  b1[position], b1[pos1] = b1[pos1], b1[position]
                  if Pawn(z, sq, 'black') == True:
                    b1[position], b1[pos1] = b1[pos1], b1[position]
                    return '\nKing cannot castle through/into Check: Please try again: \n'
                elif item1 != '' and item1 != 'bking' and item1[0] == 'b':
                  piecepos = pieces.index(item1)
                  if sofar[piecepos](z, sq, 'black') == True:
                    return '\nKing cannot castle through/into Check: Please try again: \n'
          else:
            return '\nObstruction!!! King cannot castle!\n'
        wkin = wkin + 1
        return 4
      else:
        return '\nKing/Rook has already moved: Please try again\n'
    elif turn == 'black':
      if bkin == 0 and brooki[0] == 0:
        bkin = bkin + 1
        for i in range(1,4):
          item = Find(b1,(position[0]-i,position[1]))
          sq = Find(squares,(position[1],position[0]-i))
          if item == '':
            for row in squares:
              for z in row:
                item1 = Find(b1,Reverse(Check(squares,z)))
                if item1 == 'king':
                  position1 = Reverse(Check(squares,z))
                  nextpos1 = (position[0]-2,position[1])
                  x = nextpos1[0]-position1[0]
                  y = nextpos1[1]-position1[1]
                  if (-2<x<2 and -2<y<2):
                    return '\nKing cannot castle close to another King: Please try again\n'
                elif item1 == 'pawn':
                  pos1 = (position[0]-i,position[1])
                  b1[position], b1[pos1] = b1[pos1], b1[position]
                  if Pawn(z, sq, 'white') == True:
                    b1[position], b1[pos1] = b1[pos1], b1[position]
                    return '\nKing cannot castle through/into Check: Please try again: \n'
                elif item1 != '' and item1 != 'king' and item1[0] != 'b':
                  piecepos = pieces.index(item1)
                  if sofar[piecepos](z, sq, 'white') == True:
                    return '\nKing cannot castle through/into Check: Please try again: \n'
          else:
            return '\nObstruction!!! King cannot castle!\n'
        bkin = bkin + 1
        return 5
      else:
        return '\nKing/Rook has already moved: Please try again: \n'
  if confirm == 'yes':
    used = b1[nextpos]
    b1[nextpos] = ''
    if turn == 'white':
      for row in squares:
        for z in row:
          item = Find(b1,Reverse(Check(squares,z)))
          if item == 'bking':
            position1 = Reverse(Check(squares,z))
            nextpos1 = (position[0]+d,position[1]+c)
            x = nextpos1[0]-position1[0]
            y = nextpos1[1]-position1[1]
            if (-2<x<2 and -2<y<2):
              return '\nKing cannot be close to another King: Please try again: \n'
          elif item != '' and item != 'bking' and item[0] == 'b':
            after1 = Find(squares,(position[1]+c,position[0]+d))
            current1 = z
            piecepos = pieces.index(Find(b1,Reverse(Check(squares, current1))))
            if sofar[piecepos](current1,after1,'black') == True:
              b1[nextpos] = used
              return '\nKing cannot move into Check: Please try again: \n'
            b1[nextpos] = used
      wkin = wkin + 1
    elif turn == 'black':
      for row in squares:
        for z in row:
          item = Find(b1,Reverse(Check(squares,z)))
          if item == 'king':
            position1 = Reverse(Check(squares,z))
            nextpos1 = (position[0]+d,position[1]+c)
            x = nextpos1[0]-position1[0]
            y = nextpos1[1]-position1[1]
            if (-2<x<2 and -2<y<2):
              return '\nKing cannot be close to another King: Please try again: \n'
          elif item != '' and item != 'king' and item[0] != 'b':
            after1 = Find(squares,(position[1]+c,position[0]+d))
            current1 = z
            piecepos = pieces.index(Find(b1,Reverse(Check(squares, current1))))
            if sofar[piecepos](current1,after1,'white') == True:
              b1[nextpos] = used
              return '\nKing cannot move into Check: Please try again: \n'
            b1[nextpos] = used
      bkin = bkin + 1
    return True
  return '\nKing cannot move to this position: Please try again: \n'
sofar = [Rookie, Knight, Bishop, Queen, King, Pawn, Rookie, Knight, Bishop, Queen, King, Pawn]
def Checkie(turn):
  if turn == 'white':
    position = Check(b1,'king')
    for row in squares:
        for z in row:
          item = Find(b1, Reverse(Check(squares, z)))
          if item != '' and item != 'bking' and item[0] == 'b':
            after1 = Find(squares,(position[1],position[0]))
            current1 = z
            piecepos = pieces.index(Find(b1,Reverse(Check(squares, current1))))
            if sofar[piecepos](current1,after1,'black') == True:
              return '\nKing is in Check\n'
  elif turn == 'black':
    posti = Check(b1,'bking')
    for row in squares:
        for z in row:
          item = Find(b1,Reverse(Check(squares,z)))
          if item != '' and item != 'king' and item[0] != 'b':
            after1 = Find(squares,(posti[1],posti[0]))
            current1 = z
            piecepos = pieces.index(Find(b1,Reverse(Check(squares, current1))))
            if sofar[piecepos](current1,after1,'white') == True:
              return '\nKing is in Check\n'
  return True

def Escape(current, after, turn, single = 'stop', block = 'stop'):
  position = Reverse(Check(squares, current))
  nextpos = Reverse(Check(squares, after))
  if turn == 'white':
    alt = 'black'
  if turn == 'black':
    alt = 'white'
  if block != 'stop':
    if Checkie(alt) != True:
      for row in squares:
        for i in row:
          item = Find(b1, Reverse(Check(squares, i)))
          if alt == 'white':
            if item != '' and item[0] != 'b':
              position = Reverse(Check(squares, i))
              ppos = int(pieces.index(item))
              for rows in squares:
                for ig in rows:
                  npos = Reverse(Check(squares, ig))
                  if sofar[ppos](i, ig, alt) == True:
                    item1 = b1[npos]
                    b1[npos], b1[position] = b1[position], b1[npos]
                    b1[position] = ''
                    if Checkie(alt) == True:
                      b1[position] = item1
                      b1[npos], b1[position] = b1[position], b1[npos]
                      return True
                    else:
                      b1[position] = item1
                      b1[npos], b1[position] = b1[position], b1[npos]
          elif alt == 'black':
            if item != '' and item[0] == 'b':
              position = Reverse(Check(squares, i))
              ppos = int(pieces.index(item))
              for rows in squares:
                for ig in rows:
                  npos = Reverse(Check(squares, ig))
                  if sofar[ppos](i, ig, alt) == True:
                    item1 = b1[npos]
                    b1[npos], b1[position] = b1[position], b1[npos]
                    b1[position] = ''
                    if Checkie(alt) == True:
                      b1[position] = item1
                      b1[npos], b1[position] = b1[position], b1[npos]
                      return True
                    else:
                      b1[position] = item1
                      b1[npos], b1[position] = b1[position], b1[npos]
      return print('\nCheckmate!!!', turn, 'wins!')
    elif Checkie(alt) == True:
      for row in squares:
        for i in row:
          item = Find(b1, Reverse(Check(squares,i)))
          if turn == 'white':
            if item != '' and item[0] == 'b':
              piecepos = pieces.index(item)
              if sofar[piecepos](i, 'b1', alt, 'go') == True:
                return True
          elif turn == 'black':
            if item != '' and item[0] != 'b':
              piecepos = pieces.index(item)
              if sofar[piecepos](i, 'b1', alt, 'go') == True:
                return True
      return print('\nStalemate!')    
  if single != 'stop':
    piecepos = int(pieces.index(Find(b1,Reverse(Check(squares, current)))))
    for row in squares:
      for i in row:
        if sofar[piecepos](current, i, turn) == True:
          npos = Reverse(Check(squares, i))
          item = b1[npos]
          b1[npos], b1[position] = b1[position], b1[npos]
          b1[position] = ''
          if Checkie(turn) == True:
            b1[position] = item
            b1[npos], b1[position] = b1[position], b1[npos]
            return True
          else:
            b1[position] = item
            b1[npos], b1[position] = b1[position], b1[npos]
    return '\nYou cannot move this piece as it is pinned by Check\n'
  piecepos = pieces.index(Find(b1,position))
  if sofar[piecepos](current,after,turn) == True:
    npos = Reverse(Check(squares, after))
    item = b1[npos]
    b1[nextpos], b1[position] = b1[position], b1[nextpos]
    b1[position] = ''
    if Checkie(turn) == True:
      b1[position] = item
      b1[nextpos], b1[position] = b1[position], b1[nextpos]
      return True
    else:
      b1[position] = item
      b1[nextpos], b1[position] = b1[position], b1[nextpos]
  return '\nYou cannot move to this position as King is in Check\n'

def castle(n):
  if n == 2:
    b1[7,7], b1[5,7] = b1[5,7], b1[7,7]
  elif n == 3:
    b1[7,0], b1[5,0] = b1[5,0], b1[7,0]
  elif n == 4:
    b1[0,7], b1[3,7] = b1[3,7], b1[0,7]
  elif n == 5:
    b1[0,0], b1[3,0] = b1[3,0], b1[0,0]
  return b1
def Draw():
  setup = []
  for coord in b1:
    if b1[coord] != '':
      setup.append(b1[coord])
  for piece in setup:
    try:
      pos = altpos[dpieces.index(piece)]
      pos1 = setup.index(piece)
      setup[pos], setup[pos1] = setup[pos1], setup[pos]
    except:
      pass
  try:
    index = drawcombs.index(setup)
    return index
  except:
    return True
count = 0
for dog in board:
    for cat in range(10):
      final =''
      for row in dog:
        final = final + row[cat]
      print(final)

turn = ['white', 'black']
def touchy(turn, bob):
  if turn == 'white':
      new = True
      try:
        if bob[0] == 'b':
          new = False
          return new
      except:
        pass
      return new
  elif turn == 'black':
      new = True
      try:
        if bob[0] != 'b':
          new = False
          return new
      except:
        pass
      return new
moves = [Rookie, Knight, Bishop, Queen, King, Pawn, Rookie, Knight, Bishop, Queen, King, Pawn]
dcount = 0
repcount = -1
end = 12
pastc = 'a1'
pasta = 'a2'
options = ['rook', 'bishop', 'queen', 'knight']



while True:
  repcount = repcount + 1
  if repcount == 0:
    for coord in b1:
      repboard[coord] = b1[coord]
  elif repcount == 1:
    for coord in b1:
      repboard05[coord] = b1[coord]
  elif repcount == 2:
    for coord in b1:
      repboard1[coord] = b1[coord]
  elif repcount == 3:
    for coord in b1:
      repboard15[coord] = b1[coord]
  elif repcount == 4:
    for coord in b1:
      repboard2[coord] = b1[coord]
    if repboard2 != repboard:
      for coord in repboard05:
        repboard[coord] = repboard05[coord]
      for coord in repboard1:
        repboard05[coord] = repboard1[coord]
      for coord in repboard15:
        repboard1[coord] = repboard15[coord]
      for coord in repboard2:
        repboard15[coord] = repboard2[coord]
      repcount = 3
  elif repcount == 5:
    for coord in b1:
      repboard25[coord] = b1[coord]
  elif repcount == 6:
    for coord in b1:
      repboard3[coord] = b1[coord]
    if repboard3 == repboard1:
      end = 3
      break
    for coord in repboard15:
      repboard[coord] = repboard15[coord]
    for coord in repboard2:
      repboard05[coord] = repboard2[coord]
    for coord in repboard25:
      repboard1[coord] = repboard25[coord]
    for coord in repboard3:
      repboard15[coord] = repboard3[coord]
    repcount = 3
  dcount = dcount+1
  if Checkie(turn[count%2]) != True:
    print(Checkie(turn[count%2]))
  current = str(input('Please input the square you would like to move: '))
  current = current.lower()
  try:
    piecepos = pieces.index(Find(b1,Reverse(Check(squares, current))))
  except:
    piecepos = 12
  while Check(squares, current) == None or b1[Reverse(Check(squares,current))] == '' or touchy(turn[count%2], b1[Reverse(Check(squares,current))]) == False or pieces[piecepos] == '' or moves[piecepos](current, 'b1', turn[count%2], 'go') != True or Escape(current, 'b1', turn[count%2], 'go') != True:
    if Check(squares, current) == None:
      print('\nInput was not valid: Such a square does not exist \n Please Try again: ')
    elif b1[Reverse(Check(squares,current))] == '':
      print('\nEmpty square: Please try again: \n')
    elif touchy(turn[count%2], b1[Reverse(Check(squares,current))]) == False:
      print('\nDo not touch your opponent\'s pieces: It\'s rude!')
    elif b1[Reverse(Check(squares,current))] == '':
      print('This is an empty square: \n Please try again: ')
    elif moves[piecepos](current, 'b1', turn[count%2], 'go') != True:
      print(moves[piecepos](current, 'b1', turn[count%2], 'go'))
    elif Escape(current, 'b1', turn[count%2], 'go') != True:
      print(Escape(current, 'b1', turn[count%2], 'go'))
    current = str(input('\nPlease input the square you would like to move: '))
    current = current.lower()
    try:
      piecepos = pieces.index(Find(b1,Reverse(Check(squares,current))))
    except:
      piecepos = 12
  after = str(input('Please input the square you would like to move to: '))
  after = after.lower()
  item = Find(b1, Reverse(Check(squares, current)))
  while Check(squares, after) == None or moves[piecepos](current, after, turn[count%2]) != True or current == after or Escape(current, after, turn[count%2]) != True:
    if Check(squares, after) == None:
      print('\nInput was not valid: Such a square does not exist \n Please Try again: ')
    elif current == after:
      print('\nPlease Choose a different square to move to: ')
    elif item == 'king':
      if isinstance(King(current, after, turn[count%2], 'stop', wkin, bkin), int) == True:
        if King(current, after, turn[count%2], 'stop', wkin, bkin)>1:
          break
        elif King(current, after, turn[count%2], 'stop', wkin, bkin) == True:
          break
      else:
        print(King(current, after, turn[count%2], 'stop', wkin, bkin))
    elif item == 'bking':
      if isinstance(King(current, after, turn[count%2], 'stop', wkin, bkin), int) == True:
        if King(current, after, turn[count%2], 'stop', wkin, bkin)>1:
          break
        elif King(current, after, turn[count%2], 'stop', wkin, bkin) == True:
          break
      else:
        print(King(current, after, turn[count%2], 'stop', wkin, bkin))
    elif moves[piecepos](current, after, turn[count%2]) != True:
      print(moves[piecepos](current, after, turn[count%2]))
    elif Escape(current, after, turn[count%2]) != True:
      print(Escape(current, after, turn[count%2]))
    after = str(input('Please input the square you would like to move to: '))
    after = after.lower()
  moved.append(current)
  if item == 'king':
    if isinstance(moves[piecepos](current, after, turn[count%2]), int) == True:
      castle(moves[piecepos](current, after, turn[count%2]))
    wkin = wkin + 1
  elif item == 'bking':
    if isinstance(moves[piecepos](current, after, turn[count%2]), int) == True:
      castle(moves[piecepos](current, after, turn[count%2]))
    bkin = bkin + 1
  pastc = current
  pasta = after
  if item == 'pawn':
    if after[1]=='8':
      while True:
        change = str(input('\nWhat piece would you like to change to: \n'))
        try:
          po = options.index(change)
          b1[Reverse(Check(squares, current))] = change
          break
        except:
          print('\nCannot change to this piece: Please try again: \n')
  elif item == 'bpawn':
    if after[1]=='1':
      while True:
        change = input('\nWhat piece would you like to change to: \n')
        try:
          po = options.index(change)
          b1[Reverse(Check(squares, current))] = 'b'+ change
          break
        except:
          print('\nCannot change to this piece: Please try again: \n')
  current = Check(squares,current)
  after = Check(squares,after)
  b1 = Swap(b1, Reverse(current), Reverse(after))
  board = Swap(board, current[0], after[0], current[1], after[1])
  if b1[Reverse(current)] != '':
    taken.append(b1[Reverse(current)])
    dcount = 0
  b1[Reverse(current)] = ''
  if Escape('a1', 'b1', turn[count%2], 'stop', 'go') != True:
    end = 1
    break
  elif Draw() != True:
    end = 0
    break
  elif dcount == 100:
    end = 2
    break
  dcount = dcount + 1
  count = count + 1
  os.system('clear')
  cowntee = 0
  for i in board:
    for num in range(8):
      i[num] = contr_pieces[pieces.index(b1[num, cowntee])]
    cowntee = cowntee + 1
  for dog in board:
    for cat in range(10):
      final =''
      for row in dog:
        final = final + row[cat]
      print(final)

os.system('clear')
cowntee = 0
for i in board:
  for num in range(8):
    i[num] = contr_pieces[pieces.index(b1[num, cowntee])]
  cowntee = cowntee + 1
for dog in board:
  for cat in range(10):
    final =''
    for row in dog:
      final = final + row[cat]
    print(final)

if end == 1:
  Escape('a1', 'b1', turn[count%2], 'stop', 'go')
elif end == 0:
  print('Draw!!\nOnly', drawcombs[Draw()], 'are on the board.')
elif end == 2:
  print('Draw!!Too many moves without taking!\nYou are very boring people!!')
elif end == 3:
  print('\nDraw by repetition: You are seriously boring people!\n')
whites = []
ws = 0
blackes = []
bs = 0
for i in taken:
  if i[0] == 'b':
    whites.append(i)
  else:
    blackes.append(i)
print('White has taken: ', whites)
print('Black has taken: ', blackes)
