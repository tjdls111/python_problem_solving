chessboard=list([0]*8 for _ in range(8))
motions={'R':(0,1),'L':(0,-1),'B':(-1,0),'T':(1,0),'RT':(1,1),'LT':(1,-1),'RB':(-1,1),'LB':(-1,-1)}

king, rock, n = input().split()
movements = []
n=int(n)
for _ in range(n):
    tmp=input()
    movements.append(tmp)

king_x=ord(king[0])-64
king_y=int(king[1])

rock_x=ord(rock[0])-64
rock_y=int(rock[1])

for movement in movements:

    if 1<= king_x + motions[movement][1] <= 8 and 1<= king_y + motions[movement][0] <=8:
            king_x += motions[movement][1]
            king_y += motions[movement][0]
            
    if king_x == rock_x and king_y == rock_y:
            if 1<= rock_x+motions[movement][1] <=8 and 1 <= rock_y+motions[movement][0] <=8:
                rock_x += motions[movement][1]
                rock_y += motions[movement][0]
            else:
                king_x -= motions[movement][1]
                king_y -= motions[movement][0]

print(chr(king_x+64)+str(king_y))
print(chr(rock_x+64)+str(rock_y))

