import numpy as np
import Block, BlockRotation, BlockType
import copy

# putable
def putable(board:np.ndarray,strorder:str) -> bool:
    # 命令が有効
    check,order = genarr(strorder)
    if not check:
        return False
    if not is_piece_duplicate(board, order):
        return False
    if not is_vertex_duplicate(board, order):
        return False 
    if is_edge_duplicate(board, order):
        return False 
    return True


def genarr(strorder:str) -> tuple[bool, np.ndarray]:
    # U034
    bt = BlockType.BlockType(strorder[0])     # 一文字目
    br = BlockRotation.BlockRotation(int(strorder[1])) # 二文字目
    x = "123456789ABCDE".find(strorder[2])
    y = "123456789ABCDE".find(strorder[3])
    block = Block.Block(bt,br).block_map
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

def is_piece_duplicate(board:np.ndarray,order:np.ndarray) -> bool:
    # 行列のなかで0以外の要素をすべて1に変換する
    tmpboard = copy.deepcopy(board)
    tmpboard[tmpboard!= 0] = 1
    # orderで受け取った列をボードに足す
    tmpboard += order
    # 2以上の要素があるかどうかをチェックする
    return not np.any(tmpboard >= 2)


def is_vertex_duplicate(board:np.ndarray,order:np.ndarray) -> bool:
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
                    # print(result)
                    return True
    
    # print(result)
    return False


def is_edge_duplicate(board:np.ndarray,order:np.ndarray) -> bool:
    # result2 = []
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
                    # result2.append((i, j))
                    return True
    
    # return result2
    # print(result2)
    return False



def ordergen():
    type_ = [chr(i) for i in range(65,86)]
    rotate_ = [str(i) for i in range(8)]
    x_ = "123456789ABCDE"
    y_ = "123456789ABCDE"

    for i in type_:
        for j in rotate_:
            for k in x_:
                for l in y_:
                    yield i + j + k + l


# 使用例

if __name__ == "__main__":
    board = np.array([
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
    rlist = []
    # print(lst[0:100])
    # for i in ordergen():
    #     # print(board)
    #     if putable(board, i):
    #         rlist.append(i)
    rlist = filter(lambda i:putable(board, i),ordergen())
    #print(rlist)
    for i in rlist:
        print(i,end=",")
    # print("Q054" in lst)
    # print("putable",putable(board,"Q054"))
    # print("putable",putable(board,"Q054"))