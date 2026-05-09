class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # map position to speed
        pos_speed_map = dict(zip(position, speed))

        # sort position by descending order
        position.sort(reverse=True)

        # compute time taken to reach the target
        time = []
        for i, pos in enumerate(position):
            t = (target - pos) / pos_speed_map.get(pos)
            if len(time) == 0:
                time.append(t)
            if time[-1] < t:
                time.append(t)

        # 1-1 map from t stack to sorted pos

        
        return len(time)
        