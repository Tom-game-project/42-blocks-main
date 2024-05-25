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
    # 行列のなかで0以外の要素をすべて1に変換する
    board[board != 0] = 1
    # orderで受け取った列をボードに足す
    board += order
    # 2以上の要素があるかどうかをチェックする
    return not np.any(board >= 2)


def is_vertex_duplicate(board:np.array,order:np.ndarray) -> bool:
    return

def is_edge_duplicate(board:np.array,order:np.ndarray) -> bool:
    return 


