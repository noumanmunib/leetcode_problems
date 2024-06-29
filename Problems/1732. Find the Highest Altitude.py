def largestAltitude(gain):
        maxAltitude = 0
        curAltitude = 0

        for g in gain:
            curAltitude += g
            maxAltitude = max(maxAltitude, curAltitude)

        return maxAltitude