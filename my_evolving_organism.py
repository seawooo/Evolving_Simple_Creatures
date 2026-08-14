#------------------------------------------------------------------------------+
#
# Evolving Simple Organisms
# Inspired by Nathan Rooy's evolving simple organisms.
# Data classes and function names originally by Nathan Rooy
# rest by Shao Liang
#------------------------------------------------------------------------------+

from math import atan2, cos, degrees, floor, radians, sin, sqrt
from random import randint, random, sample, uniform
from collections import defaultdict
import operator
import numpy as np

settings = {
    'pop_size': 50,
    'food_num': 100,
    'gens': 50,
    'elitism': 0.20,
    'mutate': 0.10,

    'gen_time': 100,
    'dt': 0.04,
    'dr_max': 720,
    'v_max': 0.5,
    'dv_max': 0.25,
    'x_min': -2.0, 'x_max': 2.0,
    'y_min': -2.0, 'y_max': 2.0,

    'inodes': 1,
    'hnodes': 5,
    'onodes': 2,
}


# ---------------------------------------------------------------------------
# Sensing
# ---------------------------------------------------------------------------

def calc_heading(org, food):
    """
    Return a float in roughly [-1, 1]: the turn needed for `org` to face
    `food`, relative to org's current heading (org.r, degrees). 
    [-1, 1] for ease of training

    org, food: objects with .x, .y attributes. org also has .r (degrees).
    """
    dx = food.x - org.x 
    dy = food.y - org.y
    theta = degrees(atan2(dy, dx)) - org.r # atan2 produce the theta between two objects in a range between (-180, 180]

    if abs(theta) > 180: theta += 360 # thus theta will be between (-540, 180] we add 360 to adjust
    return theta/180 


# ---------------------------------------------------------------------------
# Physics
# ---------------------------------------------------------------------------

def update_r(org, settings):
    """
    Mutate org.r in place based on org.nn_dr (a decision in [-1, 1]),
    settings['dr_max'] (max degrees/sec), and settings['dt'].
    Keep org.r wrapped into [0, 360).
    """
    change = org.nn_dr * settings['dr_max'] * settings['dt']
    org.r = (org.r + change) % 360
    



def update_vel(org, settings):
    """
    Mutate org.v in place based on org.nn_dv (a decision in [-1, 1]),
    settings['dv_max'], settings['dt']. Clamp into [0, settings['v_max']].
    """
    change = org.nn_dv * settings['dv_max'] * settings['dv_max']
    if org.v + change < 0:
        org.v = 0
    elif org.v + change > settings['v_max']: 
        org.v = settings['v_max']
    else:
        org.v += change
    



def update_pos(org, settings):
    """
    Mutate org.x, org.y in place based on org.v, org.r, settings['dt'].
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------------------
# Neural network
# ---------------------------------------------------------------------------

def think(org):
    """
    Forward pass. Sets org.nn_dv and org.nn_dr (each a float in (-1, 1))
    based on org.r_food (float input), org.wih (shape: hnodes x inodes),
    org.who (shape: onodes x hnodes).
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------------------
# Simulation loop
# ---------------------------------------------------------------------------

def simulate(settings, organisms, foods, gen):
    """
    Run settings['gen_time'] / settings['dt'] timesteps.
    Each timestep: update nearest-food sensing + handle eating, then
    call think() / update_r() / update_vel() / update_pos() per organism.
    Return the (mutated) organisms list.
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------------------
# Genetic algorithm
# ---------------------------------------------------------------------------

def evolve(settings, organisms_old, gen):
    """
    Return (new_organisms, stats).
    stats: dict-like with at least 'BEST', 'WORST', 'AVG' fitness values
    from organisms_old.
    new_organisms: same length as organisms_old, built via elitism +
    selection + crossover + mutation on .wih / .who.
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------------------
# Data classes 
# ---------------------------------------------------------------------------

class food():
    def __init__(self, settings):
        self.x = uniform(settings['x_min'], settings['x_max'])
        self.y = uniform(settings['y_min'], settings['y_max'])
        self.energy = 1

    def respawn(self, settings):
        self.x = uniform(settings['x_min'], settings['x_max'])
        self.y = uniform(settings['y_min'], settings['y_max'])
        self.energy = 1


class organism():
    def __init__(self, settings, wih=None, who=None, name=None):
        self.x = uniform(settings['x_min'], settings['x_max'])
        self.y = uniform(settings['y_min'], settings['y_max'])
        self.r = uniform(0, 360)
        self.v = uniform(0, settings['v_max'])

        self.d_food = 100
        self.r_food = 0
        self.fitness = 0

        self.wih = wih
        self.who = who
        self.name = name

        # set by think(), consumed by update_r/update_vel
        self.nn_dv = 0.0
        self.nn_dr = 0.0


def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

def run(settings):
    # TODO: create foods, create organisms (random wih/who), loop gens times
    # calling simulate() then evolve(), print stats each generation.
    pass


if __name__ == '__main__':
    run(settings)