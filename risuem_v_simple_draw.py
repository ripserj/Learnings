import random

import simple_draw as sd

sd.resolution = (1200, 600)
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)
    x = random.randint(1, 10)
