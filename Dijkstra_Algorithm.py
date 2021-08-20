# Dijkstra_Algorithm

class Graph():    
    def __init__(self, node):
        self.node = node
        self.graph = []

    def dijkstra(self, start):
        int_max=2**31-1                    

        dist = [int_max] * self.node                           # 거리(가중치) 초기화  
        dist[start] = 0                                        # start vertex에서 start vertex까지의 거리는 0

        tree = [False] * self.node
        # 지금까지 구성된 최단 경로 트리 내의 집합 (현재는 shortest path tree에 속한 node가 없다)
 

        for j in range(self.node):
            # v1부터 vn까지의 값 for문을 이용하여 구한다.

            min_dist=int_max
            # edge가 없는 경우 가중치는 MAX_INT
            
            for i in range(self.node):                         
                if dist[i]<min_dist and dist[i]>=0 and tree[i]==False: # 해당 노드까지의 거리가 min_dist보다 작을때 
                    min_dist=dist[i]                           
                    min_index=i                                # min_dist와 min_index값 업데이트

            tree[min_index] = True                             # min_dist의 node를 트리정점에 집어넣는다.
            
            for v in range(self.node):
                
                if self.graph[min_index][v] >= 0 and tree[v] == False \
                   and dist[v] > dist[min_index] + self.graph[min_index][v]:
                    
                       dist[v] = dist[min_index] + self.graph[min_index][v] 
                        # v가 트리 정점 min_index에 대해 인접 정점인 경우
            
        print("("+str(file_num)+")"+" 입력파일 graph"+str(file_num)+".txt")
        print ("    정점 v"+str(split[1])+"(으)로부터 각 정점까지의 최단 경로 :", tuple(dist)) # 리스트를 튜플로 변환
        print("\n")

        
for i in range(6):                       # graph1.txt~graph6.txt 불러오기
    file_num=i+1
    distance=[]

    file=open('C:\\ProgrammingReport#1_TestData\\graph'+str(file_num)+'.txt','rt')
    read=file.read()
    split=read.split()                   # 파일을 리스트(문자열)로 읽어오기
    split=[int (n) for n in split]       # 읽어온 리스트를 정수형으로 변환

    num_vertex=split[0]                  # node의 개수 
    start_vertex=split[1]-1              # start_node가 존재하는 index 위치

    graph=[]
    graph_line=[]
    k=0

    for i in range(num_vertex):     
        for j in range(num_vertex):
            graph_line.append(split[2+k])
            k+=1
        graph.append(graph_line)
        graph_line=[]                    # split를 2차원의 배열(graph)로 저장

    g  = Graph(num_vertex)               # graph의 node개수를 부여하며 graph 형태 초기화
    g.graph = graph                      
    g.dijkstra(start_vertex);            
