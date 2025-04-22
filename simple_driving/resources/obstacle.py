import pybullet as p
import os

class Obstacle:
    def __init__(self, client, position):
        f_name = os.path.join(os.path.dirname(__file__), 'simplecylinder.urdf')
        self.obstacle = client.loadURDF(fileName=f_name, basePosition=[position[0], position[1], 0])
