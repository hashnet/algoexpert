lenX, lenY = 0, 0

def riverSizes(matrix):
    global lenX, lenY
    lenY = len(matrix)
    lenX = len(matrix[0])

    visited = [[False if matrix[i][j] == 1 else True for j in range(lenX)] for i in range(lenY)]
    sizes = []
    for i in range(lenY):
        for j in range(lenX):
            if not visited[i][j]:
                sizes.append(visit(i, j, visited))

    return sizes


def visit(i, j, visited):
    visited[i][j] = True
    count = 1
    
    if i > 0 and not visited[i-1][j]:
        count += visit(i-1, j, visited)
    if i < lenY-1 and not visited[i+1][j]:
        count += visit(i+1, j, visited)
    if j > 0 and not visited[i][j-1]:
        count += visit(i, j-1, visited)
    if j < lenX-1 and not visited[i][j+1]:
        count += visit(i, j+1, visited)

    return count   


if __name__ == "__main__":
    print(riverSizes([[0]]))
    print(riverSizes([[1]]))
    print(riverSizes([[1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0]]))
    
    