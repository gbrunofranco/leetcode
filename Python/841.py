from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        entered = set()
        while len(keys) > 0:
            for room in rooms[keys[0]]:
                if room not in entered:
                    keys.append(room)
            entered.add(keys.pop(0))
        if len(entered) == len(rooms):
            return True
        return False


if __name__ == "__main__":
    ex = Solution()

    assert ex.canVisitAllRooms([[1], [2], [3], []]) is True
    assert ex.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False
