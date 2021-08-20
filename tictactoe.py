#tic tac toe 게임
import time

board=[' ']*9
#게임 보드 그리는 함수
def drawBoard():
    print(" %c | %c | %c "%(board[0],board[1],board[2]))
    print("---|---|---")
    print(" %c | %c | %c "%(board[3],board[4],board[5]))
    print("---|---|---")
    print(" %c | %c | %c "%(board[6],board[7],board[8]))
    print("   |   | ")

#이겼는지, 비겼는지, 게임을 지속해야 하는지 검사
def checkWin():
    #수평선상으로 같은 마크가 있는지 검사
    
    if(board[0]==board[1] and board[1]==board[2] and board[0]!=' '):
        winner(0)
    elif(board[3]==board[4] and board[4]==board[5] and board[3]!=' '):
        winner(3)
    elif(board[6]==board[7] and board[7]==board[8] and board[6]!=' '):
        winner(6)
        
    #수직선상에 같은 마크가 있는지 검사
        
    elif(board[0]==board[3] and board[3]==board[6] and board[0]!=' '):
        winner(0)
    elif(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        winner(1)
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        winner(2)
        
    #대각선상으로 이겼는지 검사
        
    elif(board[0]==board[4] and board[4]==board[8] and board[4]!=' '):
        winner(4)
    elif(board[2]==board[4] and board[4]==board[6] and board[4]!=' '):
        winner(4)
        
    #비긴 경우
        
    elif(board[0]!=' 'and board[1]!=' 'and board[2]!=' 'and board[3]!=' 'and board[4]!=' '
         and board[5]!=' 'and board[6]!=' 'and board[7]!=' 'and board[8]!=' '):
        print("무승부")
        global game
        game=True
    else:
        print("")

def winner(i):                      #이긴 선수 판별
    if board[i]=='X':
            print("선수 1 승리")
    else:
            print("선수 2 승리")
    global game
    game= True                      #게임 종료
    
player=1
game=False
    
###############################

#게임 준비

print("Tic-Tac-Toe 게임 시작 ")
print("선수1 [X] --- 선수2 [0]\n")
print()
print()
print("준비중입니다...")
time.sleep(3)

drawBoard()

#게임 로직 작성
while game==False:
    if player%2==1:
        print("선수1 차례")
        mark='X'
    elif player%2==0:
        print("선수2 차례")
        mark='0'
    position=input("마크하기를 원하는 위치(1-9)를 선택하세요:")
    idx=int(position)-1
    board[idx]=mark
    drawBoard()
    checkWin()
    player+=1
    
