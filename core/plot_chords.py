import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from chord_shapes import ChordShapes


class FretboardToCoord:
    fret_x_coord: dict[int, int] = {    
        0: 65, 1: 168, 2: 273, 3: 373,
        4: 466, 5: 557, 6: 640, 7: 717,
        8: 790, 9: 861, 10: 927, 11: 985,
        12: 1044, 13: 1096, 14: 1150, 15: 1195
    }
    
    string_reg_data: dict[int, dict[str, NDArray[np.int64]]] ={
        1: {
        'x': np.array([[86, 1485]]).reshape(-1, 1),
        'y': np.array([70, 54])
        },
        2: {
        'x': np.array([[85, 1479]]).reshape(-1, 1),
        'y': np.array([93, 84])
        },
        3: {
        'x': np.array([[83, 1479]]).reshape(-1, 1),
        'y': np.array([116, 115])
        },
        4: {
        'x': np.array([[81, 1479]]).reshape(-1, 1),
        'y': np.array([140, 146])
        },   
        5: {
        'x': np.array([[81, 1479]]).reshape(-1, 1),
        'y': np.array([162, 176])
        },
        6: {
        'x': np.array([[81, 1479]]).reshape(-1, 1),
        'y': np.array([187, 207])
        }
    }
    
    def get_fretboard_coords(self, string: int, fret: int) -> tuple[int, int]:
        reg = LinearRegression().fit(self.string_reg_data[string]['x'],
                                     self.string_reg_data[string]['y'])
        x_coord: int = self.fret_x_coord[fret]
        y_coord: int = int(reg.predict(np.array([x_coord]).reshape(-1, 1))[0])
        return  x_coord, y_coord  
    

class ChordShapePlot:
    BASE_IMG = '/home/pav/python/chord_reverse/images/fretboard_2.png'
    # CHORD_COLORS = {
    #     0: 'slateblue',  1: 'orangered',
    #     2: 'orange',
    #     3: 'cyan',
    #     4: 'olive',
    #     5: 'purple',
    #     6: 'white', 
    #     7: 'red',
    #     8: 'yellow', 
    #     9: 'lightgreen',
    #     10: 'lime',
    #     11: 'fuchsia', 
    #     12: 'azure', 
    #     13: 'silver',
    #     14: 'darkgray',
    #     15: 'khaki'
    # }
    
    def __init__(self, chord_string: str) -> None:
        self._chord_string = chord_string
        self._converter = FretboardToCoord()
        self._shapes = ChordShapes()
        
    def _create_base_image(self):
        fig, ax = plt.subplots(figsize=(20, 5))
        im: NDArray[np.int64] = plt.imread(self.BASE_IMG)
        ax.imshow(im)
        # ax.scatter(100, 100, color='orangered')
        # plt.show()
        return ax
        
    def get_note_locations(self) -> list[list[tuple[int, int]]]:
        locations: list[list[tuple[int, int]]] = []
        for shape in self._shapes.get_shapes(self._chord_string):
            full_shape = []
            for note in shape: 
                x, y = self._converter.get_fretboard_coords(note[0], note[1])
                full_shape.append((x, y))
            locations.append(full_shape)
        return locations
            
    def plot(self):
        loc = self.get_note_locations()
        ax = self._create_base_image()           
        for idx, i in enumerate(loc):
            if idx < 15:
                for note in i:
                    ax.scatter(note[0], note[1], color = self.CHORD_COLORS[idx])
        plt.show()
        
    def plot_by_idx(self, idx: int):
        loc = self.get_note_locations()
        ax = self._create_base_image() 
        chord_shape = loc[idx]
        for note in chord_shape:
            ax.scatter(note[0], note[1], color='orangered')            
        plt.show()
        
        

if __name__ == '__main__':
    # c = ChordShapes()
    cp = ChordShapePlot('Am')
    cp.plot_by_idx(5)
    # cp.create_base_image()
        