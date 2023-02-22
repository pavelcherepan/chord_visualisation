from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
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
    
    open_coords: dict[int, tuple[int, int]] = {
        1: (64, 76),
        2: (64, 98),
        3: (64, 122),
        4: (64, 146),
        5: (64, 169),
        6: (64, 192)
    }
    
    def get_fretboard_coords(self, string: int, fret: int) -> tuple[int, int]:
        reg: LinearRegression = LinearRegression().fit(self.string_reg_data[string]['x'],
                                                       self.string_reg_data[string]['y'])
        x_coord: int = self.fret_x_coord[fret]
        y_coord: int = int(reg.predict(np.array([x_coord]).reshape(-1, 1))[0])
        return  x_coord, y_coord 
    
    
@dataclass
class CoordinateDiagram:
    shape_coords: list[tuple[int, int]]
    open_strings: list[int]
    muted_strings: list[int] 
    

class ChordShapePlot:
    BASE_IMG = '/home/pav/Coding/python/chord_reverse/images/fretboard_2.png'
    
    def __init__(self, chord_string: str) -> None:
        self._chord_string = chord_string
        self._converter = FretboardToCoord()
        self._shapes = ChordShapes()
        
    def _create_base_image(self, no_subplots: int) -> list[Axes]:
        _, axs = plt.subplots(no_subplots, figsize=(20, 5))
        im: NDArray[np.int64] = plt.imread(self.BASE_IMG)
        if no_subplots == 1:
            axs.imshow(im)
            return axs
        else:
            base: list[Axes] = []
            for a in axs:
                a.imshow(im)
                base.append(a)
            return base
    
    def _display_open_strings(self, ax: Axes, strings: list[int]):
        coords = [FretboardToCoord.open_coords[i] for i in strings]
        for c in coords:
            ax.text(x=c[0], y=c[1], s="O", color='orangered')
            
    def _display_muted_strings(self, ax: Axes, strings: list[int]):
        coords = [FretboardToCoord.open_coords[i] for i in strings]
        for c in coords:
            ax.text(x=c[0], y=c[1], s="X", color='orangered')
        
    def get_note_locations(self) -> list[CoordinateDiagram]:
        diagrams: list[CoordinateDiagram] = []
        for diagram in self._shapes.get_chord_diagram(self._chord_string):
            full_shape = []
            for note in diagram.shape: 
                x, y = self._converter.get_fretboard_coords(note[0], note[1])
                full_shape.append((x, y))
            diagrams.append(
                CoordinateDiagram(
                    shape_coords=full_shape, 
                    open_strings=diagram.open_strings,
                    muted_strings=diagram.muted_strings
                    )
                )
        return diagrams
            
    def plot(self):
        diags = self.get_note_locations()
        axs = self._create_base_image(no_subplots=len(diags))           
        for idx, i in enumerate(diags):
            self._display_open_strings(axs[idx], i.open_strings)
            self._display_muted_strings(axs[idx], i.muted_strings)
            for note in i.shape_coords:
                axs[idx].scatter(note[0], note[1])
        plt.show()
        
    def plot_by_idx(self, idx: int):
        diags = self.get_note_locations()
        ax = self._create_base_image(no_subplots=1) 
        chord_shape = diags[idx]
        self._display_open_strings(ax, chord_shape.open_strings)
        self._display_muted_strings(ax, chord_shape.muted_strings)
        for note in chord_shape.shape_coords:
            ax.scatter(note[0], note[1], color='orangered')            
        plt.show()
        
        

if __name__ == '__main__':
    # c = ChordShapes()
    cp = ChordShapePlot('F')
    cp.plot_by_idx(-2)
    # cp.create_base_image()
        