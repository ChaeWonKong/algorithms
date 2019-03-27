"""쿼드 트리 뒤집기

ID: QUADTREE
URL: https://algospot.com/judge/problem/read/QUADTREE

대량의 좌표 데이터를 메모리 안에 압축해 저장하기 위해 사용하는 여러 기법 중
쿼드 트리(quad tree)란 것이 있습니다. 
주어진 공간을 항상 4개로 분할해 재귀적으로 표현하기 때문에 
쿼드 트리라는 이름이 붙었는데, 이의 유명한 사용처 중 하나는 검은 색과 
흰 색밖에 없는 흑백 그림을 압축해 표현하는 것입니다. 
쿼드 트리는 2N × 2N 크기의 흑백 그림을 다음과 같은 과정을 거쳐 문자열로 압축합니다.

이 그림의 모든 픽셀이 검은 색일 경우 이 그림의 쿼드 트리 압축 결과는 
그림의 크기에 관계없이 b가 됩니다.
이 그림의 모든 픽셀이 흰 색일 경우 이 그림의 쿼드 트리 압축 결과는 
그림의 크기에 관계없이 w가 됩니다.
모든 픽셀이 같은 색이 아니라면, 쿼드 트리는 이 그림을 가로 세로로 각각 2등분해 
4개의 조각으로 쪼갠 뒤 각각을 쿼드 트리 압축합니다. 
이때 전체 그림의 압축 결과는 x(왼쪽 위 부분의 압축 결과)(오른쪽 위 부분의 압축 결과)
(왼쪽 아래 부분의 압축 결과)(오른쪽 아래 부분의 압축 결과)가 됩니다. 
예를 들어 그림 (a)의 왼쪽 위 4분면은 xwwwb로 압축됩니다.
그림 (a)와 그림 (b)는 16×16 크기의 예제 그림을 쿼드 트리가 
어떻게 분할해 압축하는지를 보여줍니다. 
이때 전체 그림의 압축 결과는 xxwww bxwxw bbbww xxxww bbbww wwbb가 됩니다.

쿼드 트리로 압축된 흑백 그림이 주어졌을 때, 
이 그림을 상하로 뒤집은 그림 을 쿼드 트리 압축해서 출력하는 프로그램을 작성하세요.

[입력]
첫 줄에 테스트 케이스의 개수 C (C≤50)가 주어집니다. 
그 후 C줄에 하나씩 쿼드 트리로 압축한 그림이 주어집니다. 
모든 문자열의 길이는 1,000 이하이며, 
원본 그림의 크기는 220 × 220 을 넘지 않습니다.

[출력]
각 테스트 케이스당 한 줄에 주어진 그림을 상하로 뒤집은 결과를 쿼드 트리 압축해서 출력합니다.

[예제 입력]
4
w
xbwwb
xbwxwbbwb
xxwww bxwxw bbbww xxxww bbbww wwbb

[예제 출력]
w
xwbbw
xxbwwbbbw
xxwbxwwxbbwwbwbxwbwwxwwwxbbwb
"""

def reversed_quadtree(s):
    def divide(s, l):
        for i in range(len(s)):
            
        return l

    def reverse():
        pass
    def merge():
        pass
    return divide(s, [])
print(reversed_quadtree("xxbwwbbbw"))

"""
def quadtree_upside_down(comp):
    SIZE = 4
    i = 0
    N = len(comp)

    def search_part():
        nonlocal i
        ret = []

        while len(ret) != SIZE and i < N:
        # while len(ret) != SIZE:
            if comp[i] in 'wb':
                ret.append(comp[i])
                i += 1
            else:
                i += 1
                ret.append('x' + search_part())

        if len(ret) == 4:
            ret[0], ret[2] = ret[2], ret[0]
            ret[1], ret[3] = ret[3], ret[1]


        return ''.join(ret)
    return search_part()"""


