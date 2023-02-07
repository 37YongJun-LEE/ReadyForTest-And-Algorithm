def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:  # 캐시히트
            cache.remove(city)
            cache.append(city)
            answer += 1

        else:  # 캐시미스
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                cache.append(city)
                cache.pop(0)
            answer += 5

    return answer


