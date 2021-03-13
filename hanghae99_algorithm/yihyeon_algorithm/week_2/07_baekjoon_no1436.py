# 백준 1436번(영화감독 숌)

n = int(input())

diehard = "666"
series = str(n-1)
list = []

if n > 1:
    list.append(series)
    list.append(diehard)
    film = "".join(list)
    print(film)
else:
    print(diehard)


