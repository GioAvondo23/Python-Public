import os
import random
import time
#When inputting the colours, input the first letter of each colour in lower case: If the program takes more than five-ten seconds to complete, you have inputted the data incorrectly, so run the code again; I know that it's not great that I haven't validated the data, but hey that's just the way it is.
print('Step1: hold the cube such that the face with: \n the WHITE centre is on the TOP \n the ORANGE centre is to your LEFT \n the GREEN centre is FACING YOU i.e. in Front \n the RED centre is to your RIGHT \n the BLUE centre is at the BACK \n the YELLOW centre is at the BOTTOM')
print('Step2: input colours using the edges first (of each face), then the corners (of each face)')
print('Step3: if a move has a "p", it means it is anticlockwise')
w = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
b = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
def Check(pos, x, y, z, a, w = w, b = b):
  if (x[pos] == z[pos] and y[pos] == a[pos] and w[pos] == b[pos]) or (x[pos] == b[pos] and y[pos] == z[pos] and w[pos] == a[pos]) or (x[pos] == a[pos] and y[pos] == b[pos] and w[pos] == z[pos]):
    return True
  elif (x[pos] == z[pos] and y[pos] == a[pos]) or (x[pos] == a[pos] and z[pos] == y[pos]):
    return True
  else:
    return False
  
def Find(item1, item2, z, a, item3 = '1', b = b):
  if item3 == '1':
    count = 0
    for i in z:
        if i == item1 and a[count] == item2:
          break
        count = count + 1
    if count >= len(z):
      return False
    else:
      return count
  elif item3 != '1':
    count = 0
    for i in z:
      if i == item1 and a[count] == item2 and b[count] == item3:
        break
      count = count + 1
  return count

def Choose(x, y, z, a, w=w, b=b):
  if x == z and y == a and w==b:
    return False
  new = []
  newR = []
  newR2 = []
  count = 0
  for i in x:
    new.append(x[count])
    newR.append(y[count])
    newR2.append(w[count])
    count = count + 1
  indeces = [i for i, n in enumerate(x) if n == z[i] and y[i] == a[i] and w[i] == b[i]]
  indeces.reverse()
  for i in indeces:
    new.pop(i)
    newR.pop(i)
    newR2.pop(i)
  if len(new) == 0:
    return False
  elif len(new) > 0:
    chosen = random.randint(0, len(new)-1)
    final = Find(new[chosen], newR[chosen], x, y, newR2[chosen], w)
    return final
Right = """
    _______ /\ 
   /__/__/ /  \ 
  /__/__/ /    \   
 /__/__/ /  R  /  
 \__\__\ \    /      
  \__\__\ \  /     
   \__\__\ \/       
"""
Rp = """
    _______ /\ 
   /__/__/ /  \ 
  /__/__/ /    \   
 /__/__/ /  Rp /  
 \__\__\ \    /      
  \__\__\ \  /     
   \__\__\ \/       
"""
Rw = """
     /\ ______
    /  /__/__/\ 
   /  /__/__/  \ 
  /  /__/__/    \  
 /  /__/__/  Rw /  
 \  \__\__\    /      
  \  \__\__\  /     
   \/ \__\__\/      
"""
Rwp = """
     /\ ______
    /  /__/__/\ 
   /  /__/__/  \ 
  /  /__/__/    \   
 /  /__/__/ Rwp /  
 \  \__\__\    /      
  \  \__\__\  /     
   \/ \__\__\/      
"""
Left = """
  /\  ______  
 /  \ \__\__\ 
/    \ \__\__\ 
\  L  \ \__\__\ 
 \    / /__/__/ 
  \  / /__/__/ 
   \/ /__/__/ 
"""
Lp = """
  /\  ______  
 /  \ \__\__\ 
/    \ \__\__\ 
\  Lp \ \__\__\ 
 \    / /__/__/ 
  \  / /__/__/ 
   \/ /__/__/ 
"""
Lw = """
   ______ /\ 
  /\__\__\  \ 
 /  \__\__\  \ 
/    \__\__\  \ 
\  Lw \__\__\  \ 
 \    /__/__/  / 
  \  /__/__/  / 
   \/__/__/ \/ 
"""
Lwp = """
   ______ /\ 
  /\__\__\  \ 
 /  \__\__\  \ 
/    \__\__\  \ 
\ Lwp \__\__\  \ 
 \    /__/__/  / 
  \  /__/__/  / 
   \/__/__/ \/ 
"""
Down = """
   _________    
  /__/__/__/\ 
 /__/__/__/\/\  
/__/__/__/\/\/__ 
\__\__\__\/\/  / 
 \__\__\__\/  /  
  /__________/  D  
"""
Dp = """
   _________    
  /__/__/__/\ 
 /__/__/__/\/\  
/__/__/__/\/\/__ 
\__\__\__\/\/  / 
 \__\__\__\/  /  
  /__________/  Dp  
"""

Dw = """
   _________    
  /__/__/__/  
 /__/__/__/ /\ 
/__/__/__/ /\/\ 
 _________/\/\/ 
 \   Dw   \/\/  
  \________\/   
"""

Dwp = """
   _________    
  /__/__/__/  
 /__/__/__/ /\ 
/__/__/__/ /\/\ 
 _________/\/\/ 
 \   Dwp  \/\/  
  \________\/ 
"""   

Front = """
   _________  
  /__/__/__/\ 
 /__/__/__/\/\   
_________ \/\/\ 
\        \ \/\/ 
 \   F    \ \/
  \________\   
"""

Fp = """   
   _________ 
  /__/__/__/\ 
 /__/__/__/\/\ 
_________ \/\/\ 
\        \ \/\/ 
 \   Fp   \ \/ 
  \________\ 
  """
def Tperm():
  print('R U R\' U\' R\' F R2 U\' R\' U\' R U R\' F\'')
def Yperm():
  print("R U' R' U' R U R' F' R U R' U' R' F R")
def Jperm():
  print("R U R' F' R U R' U' R' F R2 U' R' U' ")
def Rperm():
  print("U' L U2 L' U2 L F' L' U' L U L F L2 U2")
edges = []
corners = []
moves = []
algs = []
Mt = 'w'
Ml = 'o'
Mf = 'g'
Mr = 'r'
MB = 'b'
Mb = 'y'
print('Please input the colours of the squares of the Top face: ')
A = input()
B = input()
C = input()
D = input()
Ac = input()
Bc = input()
Cc = input()
Dc = input()
Top = [[Ac, A, Bc], 
        [D, Mt, B], 
        [Dc, C, Cc]]
print('Please input the colours of the squares of the Left face: ')

E = input()
F = input()
G = input()
H = input()
Ec = input()
Fc = input()
Gc = input()
Hc = input()
LeftE = [[Ec, E, Fc],
         [H, Ml, F],
         [Hc, G, Gc]]
print('Please input the colours of the squares of the Front face: ')
I = input()
J = input()
K = input()
L = input()
Ic = input()
Jc = input()
Kc = input()
Lc = input()
FrontE = [[Ic, I, Jc],
         [L, Mf, J],
         [Lc, K, Kc]]
print('Please input the colours of the squares of the Right face')
M = input()
N = input()
O = input()
P = input()
Mc = input()
Nc = input()
Oc = input()
Pc = input()
RightE = [[Mc, M, Nc],
         [P, Mr, N],
         [Pc, O, Oc]]
print('Please input the colours of the squares of the Back face: ')
Q = input()
R = input()
S = input()
T = input()
Qc = input()
Rc = input()
Sc = input()
Tc = input()
Back = [[Rc, Q, Qc],
         [R, MB, T],
         [Sc, S, Tc]]
print('Please input the colours of the the squares of the Bottom face: ')
U = input()
V = input()
W = input()
X = input()
Uc = input()
Vc = input()
Wc = input()
Xc = input()
Bottom = [[Uc, U, Vc],
           [X, Mb, V],
           [Xc, W, Wc]]
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
contr_alpha = ['Q', 'M', 'I', 'E', 'D', 'L', 'X', 'T', 'C', 'P', 'U', 'F', 'B', 'R', 'V', 'J', 'A', 'N', 'W', 'H', 'K', 'O', 'S', 'G']
contr_edges= [Q, M, I, E, D, L, X, T, C, P, U, F, B, R, V, J, A, N, W, H, K, O, S, G]
fake_edges = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X]
set_edges = ['w', 'w', 'w', 'w', 'o', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'y', 'y', 'y', 'y']
contr_sedges = ['b', 'r', 'g', 'o', 'w', 'g', 'y', 'b', 'w', 'r', 'y', 'o', 'w', 'b', 'y', 'g', 'w', 'r', 'y', 'o', 'g', 'r', 'b', 'o']
os.system('clear')
print('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in Top))
print('')
print('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in FrontE))
print('')
print('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in Bottom))
print('')
print('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in Back))
print('')
print('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in LeftE))
print('')
print('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in RightE))
input()
os.system('clear')

bufferT = fake_edges[1]
bufferR = contr_edges[1]
while True:
  while Check(1,fake_edges,contr_edges,set_edges,contr_sedges) == False:
    rpos = Find(bufferT, bufferR, set_edges, contr_sedges)
    apos = Find(bufferR, bufferT, set_edges, contr_sedges)
    fake_edges[1], fake_edges[rpos] = fake_edges[rpos], fake_edges[1]
    contr_edges[1], contr_edges[rpos] = contr_edges[rpos], contr_edges[1]
    fake_edges[12], fake_edges[apos] = fake_edges[apos], fake_edges[12]
    contr_edges[12], contr_edges[apos] = contr_edges[apos], contr_edges[12] 
    edges.append(alpha[rpos])
    bufferT = fake_edges[1]
    bufferR = contr_edges[1]
  new = Choose(fake_edges,contr_edges,set_edges,contr_sedges)
  if fake_edges == set_edges and contr_edges == contr_sedges:
    break
  else:
    other = Find(contr_edges[new], fake_edges[new], fake_edges, contr_edges)
    fake_edges[1], fake_edges[new] = fake_edges[new], fake_edges[1]
    contr_edges[1], contr_edges[new] = contr_edges[new], contr_edges[1]
    fake_edges[12], fake_edges[other] = fake_edges[other], fake_edges[12]
    contr_edges[12], contr_edges[other] = contr_edges[other], contr_edges[12] 
    bufferT = fake_edges[1]
    bufferR = contr_edges[1]
    edges.append(alpha[new])
for i in edges:
  if i == 'B' or i == 'M':
    print('hi')
    edges.remove(i)
print(edges)
input()
x = [Ac, Bc, Cc, Dc, Ec, Fc, Gc, Hc, Ic, Jc, Kc, Lc, Mc, Nc, Oc, Pc, Qc, Rc, Sc, Tc, Uc, Vc, Wc, Xc]
y =[Ec, Rc, Mc, Ic, Qc, Dc, Lc, Xc, Fc, Cc, Pc, Uc, Jc, Bc, Sc, Vc, Ac, Nc, Wc, Hc, Gc, Kc, Oc, Tc]
w=[Qc, Nc, Jc, Fc, Ac, Ic, Uc, Tc, Dc, Mc, Vc, Gc, Cc, Rc, Wc, Kc, Ec, Bc, Oc, Xc, Lc, Pc, Sc, Hc]
z      = ['w', 'w', 'w', 'w', 'o', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'y', 'y', 'y', 'y']
a = ['o', 'b', 'r', 'g', 'b', 'w', 'g', 'y', 'o', 'w', 'r', 'y', 'g', 'w', 'b', 'y', 'w', 'r', 'y', 'o', 'o', 'g', 'r', 'b']
b =['b', 'r', 'g', 'o', 'w', 'g', 'y', 'b', 'w', 'r', 'y', 'o', 'w', 'b', 'y', 'g', 'o', 'w', 'r', 'y', 'g', 'r', 'b', 'o']
bufferT = x[0]
bufferR = y[0]
bufferR2 = w[0]
while True:
  while Check(0, x, y, z, a, w, b)==False:
    rpos = Find(bufferR, bufferR2, z, a, bufferT, b)
    apos = Find(bufferR2, bufferT, z, a, bufferR, b)
    bpos = Find(bufferT, bufferR, z, a, bufferR2, b)
    x[0], x[bpos] = x[bpos], x[0]
    y[0], y[bpos] = y[bpos], y[0]
    w[0], w[bpos] = w[bpos], w[0]
    x[4], x[rpos] = x[rpos], x[4]
    y[4], y[rpos] = y[rpos], y[4]
    w[4], w[rpos] = w[rpos], w[4] 
    x[16], x[apos] = x[apos], x[16]
    y[16], y[apos] = y[apos], y[16]
    w[16], w[apos] = w[apos], w[16]
    bufferT = x[0]
    bufferR = y[0]
    bufferR2 = w[0]
    corners.append(alpha[rpos])
  new = Choose(x,y,z,a,w,b)
  if x == z and y == a and w == b:
    break
  else:
    apos = Find(w[new], x[new], x, y, y[new], w)
    bpos = Find(y[new], w[new], x, y, x[new], w)
    x[0], x[apos] = x[apos], x[0]
    y[0], y[apos] = y[apos], y[0]
    w[0], w[apos] = w[apos], w[0]
    x[4], x[new] = x[new], x[4]
    y[4], y[new] = y[new], y[4]
    w[4], w[new] = w[new], w[4] 
    x[16], x[bpos] = x[bpos], x[16]
    y[16], y[bpos] = y[bpos], y[16]
    w[16], w[bpos] = w[bpos], w[16]
    bufferT = x[0]
    bufferR = y[0]
    bufferR2 = w[0]
    corners.append(alpha[new])
count = 0
for i in corners:
  if i == 'A' or i == 'E' or i == 'Q':
    corners.pop(count)
  count = count + 1
print('\n', corners) 

slotD = ['A', 'D', 'F', 'H', 'I', 'J', 'L', 'N', 'P', 'R', 'T', 'U', 'V', 'W', 'X']
dm = [Lw + Lw + Dp + Lp + Lp, '-press enter-', Dwp + Left, Dw + Lp, Lw + Dp + Lp + Lp, Dwp + Dwp + Left, Lp, Dw + Left, Dwp + Lp, Dw + Dw + Lp, Left, Dp + Lp + Lp, Dp + Dp + Lp + Lp, Down + Lp + Lp, Lp + Lp]
dmp = [Lp + Lp + Down + Lwp + Lwp, '-press enter-', Lp + Dw, Left + Dwp, Left + Left + Down + Lwp, Lp + Dw + Dw, Left, Lp + Dwp, Left + Dw, Left + Dwp + Dwp, Lp, Lp + Lp + Down, Lp + Lp + Dp + Dp, Lp + Lp + Dp, Lp + Lp]
slotC = ['C', 'E', 'G', 'K', 'O', 'Q', 'S']
cm = ['-press enter-', Lp + Lp + Down + Lwp, Down + Lwp, Lwp, Dp + Lwp, Lw, Dp + Dp + Lwp]
cmr = ['-press enter-', Lw + Dp + Lp + Lp, Lw + Dp, Lw, Lw + Down, Lwp, Lw + Dp + Dp]
slotV = ['B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
vm = [Right + Right, Front + Front + Down, Front + Front, Fp + Down, Fp, Dp + Right, Front + Rp, Rp, Rp + Dp, Front + Front + Rp, Front, Rp + Front, Rp + Rp + Front, Right + Front, Right + Dp, Right, Down + Fp, Down, '-press enter-', Dp, Dp + Dp]
vmp = [Rp + Rp, Dp + Fp + Fp, Fp + Fp, Dp + Front, Front, Rp + Down, Right + Fp, Right, Down + Right, Right + Fp + Fp, Fp, Fp + Right, Fp + Rp + Rp, Fp + Rp, Down + Rp, Rp, Front + Dp, Dp, '-press enter-', Down, Dp + Dp]
for i in edges:
  if i == 'M' or i == 'B':
   edges.remove(i)
  else:
    print(i)
    try:
      pos = slotD.index(i)
      print(dm[pos])
      input()
      os.system('clear')
      print('Tperm:')
      Tperm()
      input()
      os.system('clear')
      print(dmp[pos])
      input()
      os.system('clear')
    except:
      pos = slotC.index(i)
      print(cm[pos])
      input()
      os.system('clear')
      print('JPerm:')
      Jperm()
      input()
      os.system('clear')
      print(cmr[pos])
      input()
      os.system('clear')
if len(edges)%2 == 1:
  print('Rperm:')
  Rperm()
for i in corners:
  pos = slotV.index(i)
  print(i)
  print(vm[pos])
  input()
  os.system('clear')
  print('Yperm')
  Yperm()
  input()
  os.system('clear')
  print(vmp[pos])
  input()
  os.system('clear')
print('Now solve it yourself, you lazy git')

print('\      ______     /      ')
print(' \    /_/_/_/\   /  /   ')
print('     /_/_/_/\/\    /     /')
print('\   /_/_/_/\/\/\    /   /')
print(' \  \_\_\_\/\/\/   /   ')
print('     \_\_\_\/\/       ')
print('  \   \_\_\_\/  / ')
print('   \           /     ')
