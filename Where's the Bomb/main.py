import Test
import math

speed_of_sound = 0.343

def get_same_point(points1, points2):
    if (points1[0] == points2[0] or points1[0] == points2[1]):
        return points1[0]
    elif (points1[1] == points2[0] or points1[1] == points2[1]):
        return points1[1]

def myround(x, prec=2, base=.001):
  return round(base * round(float(x)/base),prec)

def inter_points(circle1, circle2):
    a, b, r1, c, d, r2 = circle1[0], circle1[1], circle1[2] * speed_of_sound, circle2[0], circle2[1], circle2[2] * speed_of_sound
    if (r1 == 0):
        return [(a, b), (a, b)]
    elif (r2 == 0):
        return [(c, d), (c, d)]
    D = myround(dist(a, b, c, d))
    s1 = myround(D + r1 + r2)
    s2 = myround(D + r1 - r2)
    s3 = myround(D - r1 + r2)
    s4 = myround(r1 + r2 - D)
    e = math.sqrt(s1 * s2 * s3 * s4) / 4
    x1 = (a + c) / 2 + (c - a) * (r1 * r1 - r2 * r2) / (2 * D * D) + 2 * (b - d) * e / (D * D)
    x2 = (a + c) / 2 + (c - a) * (r1 * r1 - r2 * r2) / (2 * D * D) - 2 * (b - d) * e / (D * D)
    y1 = (b + d) / 2 + (d - b) * (r1 * r1 - r2 * r2) / (2 * D * D) - 2 * (a - c) * e / (D * D)
    y2 = (b + d) / 2 + (d - b) * (r1 * r1 - r2 * r2) / (2 * D * D) + 2 * (a - c) * e / (D * D)

    return [(round(x1), round(y1)), (round(x2), round(y2))]

def dist(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    d = math.sqrt(dx * dx + dy * dy)
    return d

def bomb(sensors):
    sensor1 = sensors[0]
    sensor2 = sensors[1]
    sensor3 = sensors[2]

    intersections1 = inter_points(sensor1, sensor2)
    intersections2 = inter_points(sensor1, sensor3)

    return get_same_point(intersections1, intersections2)


Test.assert_equals(bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]]), (21, 13))
Test.assert_equals(bomb([[18, 42, 35.558], [39, 16, 106.004], [7, 24, 32.202]]), (8, 35))
Test.assert_equals(bomb([[42, 19, 98.004], [3, 17, 122.484], [28, 29, 61.294]]), (29, 50))
Test.assert_equals(bomb([[46, 23, 89.434], [19, 8, 73.119], [17, 33, 0.0]]), (17, 33))
Test.assert_equals(bomb([[9, 39, 35.468], [15, 27, 44.407], [31, 18, 73.119]]), (21, 41))
Test.assert_equals(bomb([[3, 49, 127.815], [16, 27, 58.672], [11, 40, 92.792]]), (34, 18))
Test.assert_equals(bomb([[48, 40, 169.849], [18, 36, 105.683], [12, 42, 116.691]]), (3, 3))
Test.assert_equals(bomb([[10, 20, 38.013], [4, 18, 53.6], [36, 29, 55.7]]), (17, 31))
Test.assert_equals(bomb([[0, 0, 72.886], [0, 50, 72.886], [25, 25, 72.886]]), (0, 25))
Test.assert_equals(bomb([[5, 5, 0], [5, 5, 0], [5, 5, 0]]), (5, 5))
Test.assert_equals(bomb([[0, 50, 145.773], [50, 50, 206.154], [50, 0, 145.773]]), (0, 0))
