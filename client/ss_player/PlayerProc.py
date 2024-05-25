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
    # ピースが被っている True
    # ピースが被っていない False
    return

def is_vertex_duplicate(board:np.array,order:np.ndarray) -> bool:
    # 頂点を自分のピースと共有している
    return

def is_edge_duplicate(board:np.array,order:np.ndarray) -> bool:
    return 


