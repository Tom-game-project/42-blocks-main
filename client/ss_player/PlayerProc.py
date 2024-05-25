import numpy as np
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

    return 

def is_piece_duplicate(board:np.array,order:np.ndarray) -> bool:
    # ピースが被っている True
    # ピースが被っていない False
    return

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
    