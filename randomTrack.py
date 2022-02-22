from wandering import ComunWandering
from track import  track
from location import location

from bokeh.plotting import figura, output_file, show

def walking(location, wandering, step):
    beginning = location.get_location(wandering)

    for _ in range (step):
        location.move_wandering(wandering)

    return beginning.distancia(location.get_location(wandering))
    

def simulate_walk(step, number_attempts, type_wandering):
     wandering = type_wandering(name='Alirio')
     origen = location(0,0)
     distances = []


     for _ in range(number_attempts):
         track = track()
         track.add_wandering(wandering, origen)
         simulation_walk = walking(track, wandering, step)
         distances.append(round[simulation_walk,i])
         return distances

def graph(x,y):
    graphics = figura(titles="comino del errante", x_axis_label="Pasos", y_axis_label="Distancia")
    graphics.line(x, y, lenged="Distancia")
    show(graphics)










