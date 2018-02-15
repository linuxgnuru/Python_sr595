import shiftpi.shiftpi as SP
import sys

#  --      A
# |  |   F   B
#  --      G
# |  |   E   C
#  --  .   D    dp


#  G   E   D   A   C  dp   B   F
segments = [
[ -1,  1,  2,  3,  4, -1,  6,  7 ], # 0
[ -1, -1, -1, -1,  4, -1,  6, -1 ], # 1
[  0,  1,  2,  3, -1, -1,  6, -1 ], # 2
[  0, -1,  2,  3,  4, -1,  6, -1 ], # 3
[  0, -1, -1, -1,  4, -1,  6,  7 ], # 4
[  0, -1,  2,  3,  4, -1, -1,  7 ], # 5
[  0,  1,  2,  3,  4, -1, -1,  7 ], # 6
[ -1, -1, -1,  3,  4, -1,  6, -1 ], # 7
[  0,  1,  2,  3,  4, -1,  6,  7 ], # 8
[  0, -1,  2,  3,  4, -1,  6,  7 ]] # 9

SP.shiftRegisters(4)


if len(sys.argv) == 1:
     digit = 4
     col = 0
elif len(sys.argv) == 2:
     digit = int(sys.argv[1])
     col = 0
else:
     digit = int(sys.argv[1])
     col = int(sys.argv[2])
if digit > 9 or digit < 0:
     SP.digitalWrite(SP.ALL, SP.LOW)
     sys.exit("invalid digit")
if col < 0 or col > 3:
     SP.digitalWrite(SP.ALL, SP.LOW)
     sys.exit("invalid col")
try:
     for i in range(0, 8):
          if segments[digit][i] != -1:
               SP.digitalWrite((abs(segments[digit][i] - 31) - (col * 8)), SP.HIGH)
except KeyboardInterrupt:
     pass

