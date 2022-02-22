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


    def main(distances_walk, number_attempts, type_wandering):
        average_walking_distance = []

        for steps in distances_walk:
            distances = simulate_walk(step, number_attempts, type_wandering)
            middle_distance = round(sum[distamces] / len(distances),4)
            max_distances = max(distances)
            min_distances=min(distances)
            average_walking_distance.append(middle_distanec)
            print(f'{type_wandering.__name__}.caminatta aleatoria de {steps} pasos')
            print(f'media = {niddle_distance}')
            print(f'max = {max_distances}')
            print(f'min = {min_distances}')
            graph(distances_walk, average_walking_distance)


    if __name__=='__main__':

        distances_walk = [10, 100 , 1000, 10000]
        number_attempts = 100
        main(distences_walk, number_attempts, ComunWandering)












