import numpy as np
from client.ss_player import Block, BlockRotation
from client.ss_player import BlockType
import copy

# putable
def putable(board:np.ndarray,strorder:str) -> bool:
    # 命令が有効
    check,order = genarr(strorder)

    if not check:
        return False
    if not is_piece_duplicate(board, order):
        return False
    if is_vertex_duplicate(board, order):
        return False 
    if not is_edge_duplicate(board, order):
        return False 
    return True


def genarr(strorder:str) -> tuple[bool, np.ndarray]:
    # U034
    bt = BlockType(strorder[0])     # 一文字目
    br = BlockRotation(strorder[1]) # 二文字目
    x = "123456789ABCDE".find(strorder[2])
    y = "123456789ABCDE".find(strorder[3])
    block: np.ndarray = Block(bt,br).block_map()
    height,width = block.shape
    if 14 < y + height or 14 < x + width:
        return False,None
    block_lst = block.tolist()
    return True,np.array([
        [
            block_lst[i - y][j - x]
            if x <= j < x + width and y <= i < y + height
            else
                0
            for j in range(14)
        ]
        for i in range(14)
    ])        

def is_piece_duplicate(board:np.array,order:np.ndarray) -> bool:
    # 行列のなかで0以外の要素をすべて1に変換する
    board[board != 0] = 1
    # orderで受け取った列をボードに足す
    board += order
    # 2以上の要素があるかどうかをチェックする
    return not np.any(board >= 2)


def is_vertex_duplicate(board:np.array,order:np.ndarray) -> bool:
    result = []
    # 頂点を自分のピースと共有している
    for i in range(14):
        for j in range(14):
            if order[i, j] == 0:
                # Check diagonal directions for '1'
                diagonal_1 = (
                    (i > 0 and j > 0 and order[i-1][j-1] == 1) or
                    (i > 0 and j < 14 - 1 and order[i-1][j+1] == 1) or
                    (i < 14 - 1 and j > 0 and order[i+1][j-1] == 1) or
                    (i < 14 - 1 and j < 14 - 1 and order[i+1][j+1] == 1)
                )
                
                # Check if there's no '1' in the four adjacent cells
                no_adjacent_1 = (
                    (i <= 0 or order[i-1][j] != 1) and  # up
                    (i >= 14 - 1 or order[i+1][j] != 1) and  # down
                    (j <= 0 or order[i][j-1] != 1) and  # left
                    (j >= 14 - 1 or order[i][j+1] != 1)  # right
                )
                
                flag = (board[i][j] == 1)
                
                if diagonal_1 and no_adjacent_1 and flag:
                    result.append((i, j))
                    return True
    
    return result


def is_edge_duplicate(board:np.array,order:np.ndarray) -> bool:
    result2 = []
    # 辺を自分のピースと共有している
    for i in range(14):
        for j in range(14):
            if order[i, j] == 0:
                # Check if there's no '1' in the four adjacent cells
                has_adjacent_1 = (
                    (i > 0 and order[i-1][j] == 1) or  # up
                    (i < 14 - 1 and order[i+1][j] == 1) or  # down
                    (j > 0 and order[i][j-1] == 1) or  # left
                    (j < 14 - 1 and order[i][j+1] == 1)  # right
                )
                flag = (board[i][j] == 1)
                
                if has_adjacent_1 and flag:
                    result2.append((i, j))
                    return False
    
    return result2



# 使用例

if __name__ == "__main__":
    order2 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    )
    order = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    )
    result = is_vertex_duplicate(order,order2)
    result2 = is_edge_duplicate(order,order2)
    print(result)
    print(result2)
    