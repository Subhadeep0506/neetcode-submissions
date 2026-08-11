class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_speed_position = sorted([(p, s) for p, s in zip(position, speed)], key=lambda x : x[0], reverse=True)
        res = []
        for i in range(len(sorted_speed_position)):
            travel_distance = target - sorted_speed_position[i][0]
            curr_speed = sorted_speed_position[i][1]
            time_taken = travel_distance / curr_speed
            if res and res[-1] >= time_taken:
                res.append(max(time_taken, res.pop()))
            else:
                res.append(time_taken)
        return len(res)

        # [6, 8, 10]
        # [1, 3, 2 ]
        # [6, 2.8,5]

        # []