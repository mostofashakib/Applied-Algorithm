"""
Problem statement: Calculate the angle between hour hand and minute hand

Link: https://www.techiedelight.com/angle-between-hour-minute-hand/
Written by: Mostofa Adib Shakib
Language: Python
"""


def findAngle(hour, min):

    # find position of hour's hand
    h = (hour * 360) // 12 + (min * 360) // (12 * 60)

    # find position of minute's hand
    m = (min * 360) // (60)

    # calculate the angle difference
    angle = abs(h - m)

    # consider shorter angle and return it
    if angle > 180:
        angle = 360 - angle

    return angle



if __name__ == '__main__':

    hour = 5
    min = 30

    print(findAngle(hour, min))
