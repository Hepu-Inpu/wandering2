from wandering import ComunWandering
from track import  track
from location import location

from bokeh.plotting import figura, output_file, show


def walking(location, wandering, step):
    beginning = location.get_location(wandering)

    for _ in range (step):
        location.move_wandering(wandering)

    return beginning.distancia(location.get_location(wandering))




