class track:

    def __init__ (self,x,y):
        self.x = x
        self.y = y
        def mover(self,delta_x,delta_y):
            return track(self.x + delta_x, self.y + delta_y)

        def distancia(self, other_track):
            delta_x = self.x -  other_track.x
            delta_y = self.y -  other_track.y
            return track(delta_x**2 + delta_y**2)**0,5