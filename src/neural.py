from turtle import *
import random

bgcolor("black")
tracer(0)

drawer = Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.width(1)

NUM_NODE = 50
NODE_SIZE = 0.5
CONNECTION_DISTANCE = 120
MOVE_SPEED = 0.3

nodes = []
for _ in range(NUM_NODE):
    node = Turtle()
    node.shape("circle")
    node.shapesize(NODE_SIZE)
    node.color("cyan")
    node.penup()
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    node.goto(x, y)

    dx = random.uniform(-MOVE_SPEED, MOVE_SPEED)
    dy = random.uniform(-MOVE_SPEED, MOVE_SPEED)

    nodes.append({'turtle': node, 'dx' : dx, 'dy': dy})

while True:
    drawer.clear()

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            pos1 = nodes[i]['turtle'].pos()
            pos2 = nodes[j]['turtle'].pos()
            distance = nodes[i]['turtle'].distance(nodes[j]['turtle'])

            if distance < CONNECTION_DISTANCE:
                opacity = 1 - (distance / CONNECTION_DISTANCE)
                grey_value = int(100 * opacity)
                drawer.color(
                    grey_value / 100.0,
                    grey_value / 100.0,
                    grey_value / 100.0,
                )
                drawer.penup()
                drawer.goto(pos1)
                drawer.pendown()
                drawer.goto(pos2)

    for node_data in nodes:
        t = node_data['turtle']
        x, y = t.pos()
        new_x = x + node_data['dx']
        new_y = y + node_data['dy']

        if not (-window_width() / 2 < new_x < window_width() / 2):
            node_data['dx'] *= -1
        if not (-window_width() / 2 < new_y < window_width() / 2):
            node_data['dy'] *= -1

        t.goto(new_x, new_y)

    update()