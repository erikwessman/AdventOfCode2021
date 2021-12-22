file = open("day21/input.txt", "r")

array = file.read().splitlines()

p1 = int(array[0][-1]) - 1
p2 = int(array[1][-1]) - 1

game_states = {}

#u/jonathan_paulson
def solve(p1,p2,s1,s2):
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    if (p1, p2, s1, s2) in game_states:
        return game_states[(p1, p2, s1, s2)]
    ans = (0,0)
    for d1 in [1,2,3]:
        for d2 in [1,2,3,]:
            for d3 in [1,2,3]:
                new_p1 = (p1+d1+d2+d3)%10
                new_s1 = s1 + new_p1 + 1

                x1,y1 = solve(p2, new_p1, s2, new_s1)
                ans = (ans[0]+y1, ans[1]+x1)

    game_states[(p1,p2,s1,s2)] = ans
    return ans

print(max(solve(p1,p2, 0, 0)))