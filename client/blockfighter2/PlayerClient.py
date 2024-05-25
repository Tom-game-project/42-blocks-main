from __future__ import annotations
import asyncio
import websockets
import random
import blockfighter.PlayerProc as PlayerProc
import numpy as np

class PlayerClient:
    def __init__(self, player_number: int, socket: websockets.WebSocketClientProtocol, loop: asyncio.AbstractEventLoop):
        self._loop = loop
        self._socket = socket
        self._player_number = player_number
        self.p1turn = 0
        self.p2turn = 0
        self.p1pieces = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'][::-1]
        self.p2pieces = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'][::-1]
        #random.shuffle(self.p1pieces)
        #random.shuffle(self.p2pieces)
    @property
    def player_number(self) -> int:
        return self._player_number

    async def close(self):
        await self._socket.close()

    async def play(self):
        while True:
            board = await self._socket.recv()
            action = self.create_action(board)
            await self._socket.send(action)
            if action == 'X000':
                raise SystemExit
    
    def string_to_2d_array(self, string):
        # 行に分割
        rows = string.split("\n")
        # 最初の行を無視
        rows = rows[1:]
        # 各行の最初の文字を無視して二次元配列を作成
        array_2d = [list(row[1:]) for row in rows]
        return array_2d

    def create_action(self, board):
        actions: list[str]
        turn: int

        board_2d = self.string_to_2d_array(board)
        # print(board_2d)
        # filter(lambda i:PlayerProc.putable(board, i),PlayerProc.ordergen())
        actions = []
        if self.player_number == 1:
            board_2d = np.array([
                [0 if i == "." else 1 if i == "o" else 2 if i == "x" else None for i in j]
                for j in board_2d
            ])
            # actions = self.p1Actions
            print("player 1",board_2d,actions)
            turn = self.p1turn
            if turn == 0:
                actions.append("R055")
                self.p1pieces.remove("R")
            else:
                actions = list(
                filter(
                lambda i:PlayerProc.putable(board_2d, i),
                PlayerProc.ordergen(
                    # [chr(i) for i in range(65,86)][::-1][self.p1turn]
                    self.p1pieces.pop(0)
                )
            )
            )
                print("actions1",actions)
            self.p1turn += 1
        else:
            board_2d = np.array([
                [0 if i == "." else 2 if i == "o" else 1 if i == "x" else None for i in j]
                for j in board_2d
            ])
            # actions = self.p2Actions
            turn = self.p2turn
            if turn == 0:
                actions.append("R088")
                self.p2pieces.remove("R")
            else:
                actions = list(
                filter(
                    lambda i:PlayerProc.putable(board_2d, i),
                    PlayerProc.ordergen(
                        #[chr(i) for i in range(65,86)][::-1][self.p1turn]
                        self.p2pieces.pop(0)
                )
            )
            )
                print("actions2",actions)
            self.p2turn += 1

        if len(actions) != 0:
            if self.player_number == 1:
                return actions[-1]
            else:
                return actions[0]
        else:
            # パスを選択
            return 'X000'
    
    @staticmethod
    async def create(url: str, loop: asyncio.AbstractEventLoop) -> PlayerClient:
        socket = await websockets.connect(url)
        print('PlayerClient: connected')
        player_number = await socket.recv()
        print(f'player_number: {player_number}')
        return PlayerClient(int(player_number), socket, loop)
