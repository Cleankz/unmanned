def Unmanned(L, N,track):
    time = L
    l_time = 0
    for i in range(L):
        for j in range(N):
            if i == track[j][0] and j == 0:
                if i > track[j][1] and i < track[j][1] + track[j][2]:
                    break
                elif i <= track[j][1]:
                    time = time + abs(track[j][1] - i)
                    l_time = l_time + abs(track[j][1] - i)
                    break
                elif abs((track[j][1] + track[j][2]) - i) < track[j][1]:
                    time = time + abs(track[j][1] - i)
                    l_time = l_time + abs(track[j][1] - i)
                    break
                elif abs((track[j][1] + track[j][2]) - i) > track[j][1] and abs((track[j][1] + track[j][2]) - i) < track[j][2] :
                    break
            elif i == track[j][0] and j > 0:
                if (i + l_time) > track[j][1] and (i + l_time) < track[j][1] + track[j][2]:
                    break
                elif (i + l_time) < track[j][1]:
                    time = time + abs(track[j][1] - i)
                    l_time = l_time + abs(track[j][1] - i)
                    break
                elif abs((track[j][1] + track[j][2]) - (i + l_time)) < track[j][1]:
                    time = time + abs(track[j][1] - i)
                    l_time = l_time + abs(track[j][1] - i)
                    break
                elif abs((track[j][1] + track[j][2]) - (i + l_time)) > track[j][1] and abs((track[j][1] + track[j][2]) -(i + l_time)) < track[j][2] :
                    break
                elif abs((track[j][1] + track[j][2]) - (i + l_time)) > track[j][1] + track[j][2]:
                    rem = abs(2* (track[j][1] + track[j][2]) - (i + l_time)) 
                    if rem > track[j][1] and rem < track[j][2] + track[j][1]:
                        break
                    elif rem <= track[j][1]:
                        time = time + abs(track[j][1] - rem)
                        l_time = l_time + abs(track[j][1] - rem)
                        break
    return time
