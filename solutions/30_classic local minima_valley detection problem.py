def detectValleys(temperature: list[int]) -> list[int]:
    if not temperature or len(temperature) < 3:
        return []
    valley = []
    for i in range(1 , len(temperature) - 1):
        if temperature[i] < temperature[i - 1] and temperature[i] < temperature[i + 1]:
            valley.append(i)
    return valley

print(detectValleys([30, 25, 20, 25, 30]))  # Output: [2]