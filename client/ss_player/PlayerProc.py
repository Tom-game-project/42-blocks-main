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
    # 頂点を自分のピースと共有している
    return

def is_edge_duplicate(board:np.array,order:np.ndarray) -> bool:
    return 


