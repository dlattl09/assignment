**기본적인 Python 코딩 및 자료구조 코드**
<br/><br/><br/>1. Tic-Tac-Toe 게임

tic-tac-toe는 두명의 player가 돌아가며 1~9의 position을 선택하는 게임이다. player가 선택한 포지션은 X,O 로 표시가 되며, 선택된 포지션은 다시 선택할 수 없다.게임의 그리드는 3 by 3이다. 
<br/><br/>
2. Dijkstra short path algorithm

v1부터 vn까지 n개의 정점(vertex)로 구성된 가중치 graph가 nxn 인접행렬로 표현되어 있을 때 출발 정점 vi에서 나머지 모든 정점까지의 최단 경로를 구하는 Dijkstra 알고리즘을 구현한다. 이 때 에지가 없는 경우 가중치는 MAX_INT(=2^31-1)로 가정한다. 이때 graph는 주어진 6개의 txt 파일을 코드에서 읽어와서 사용한다.
입력자료 형식은 아래와 같다.
<br/>########################
<br/>% 입력.txt
<br/>4 1   % 정점의 개수 (n) = 4, 출발 정점(vi) = v1
<br/>0 1 3 1 % nxn = 4x4 인접 행렬
<br/>1 0 8 9
<br/>3 8 0 5
<br/>2 9 5 0
<br/>########################
<br/>마찬가지로 출력자료의 형식은 아래와 같다.
<br/>########################
<br/>(1) 입력파일 graphn.txt
<br/>정점 v1(으)로부터 각 정점까지의 최단경로 = ( 0, 1, 3, 2)
<br/>########################
<br/>node의 개수가 총 n개라고 가정했을 때 가장 바깥 부분의 for문에서 총 n번 전체 계산이 돌아 가게 된다. 내부에 존재하는 for문을 살펴보면 for i in range(self.node)에서 최대 n번 계산을 하 게 되며 다음 for문인 for v in range(self.node)를 살펴보면 마찬가지로 최대 n번 계산을 하게 된 다. 포문 안에서의 시간복잡도 T(n)을 계산하면 n*(n+n)=n2가 됨을 알 수 있다. 따라서 해당 알 고리즘은 Θ(n2)의 시간복잡도를 갖는다.

