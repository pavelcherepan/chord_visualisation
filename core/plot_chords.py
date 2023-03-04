from pathlib import Path
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from sklearn.linear_model import LinearRegression

from core.chord_shapes import ChordShapes


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
        1: (61, 78),
        2: (61, 100),
        3: (61, 122),
        4: (61, 150),
        5: (61, 173),
        6: (61, 195)
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
    BASE_IMG = 'images/fretboard_2.png'
    
    def __init__(self, chord_string: str) -> None:
        self._chord_string = chord_string
        self._converter = FretboardToCoord()
        self._shapes = ChordShapes()
        self.diags = self.get_note_locations()
        
    def _create_base_image(self, no_subplots: int) -> list[Axes]:
        _, axs = plt.subplots(no_subplots, figsize=(20, 5  * no_subplots), dpi=600)
        im: NDArray[np.int64] = plt.imread(self.BASE_IMG)
        if no_subplots == 1:
            axs.imshow(im)
            axs.set_axis_off()
            return axs
        else:
            base: list[Axes] = []
            for a in axs:
                a.imshow(im)
                a.set_axis_off()
                base.append(a)
            return base
    
    def _display_open_strings(self, ax: Axes, strings: list[int], fontsize: int = 5):
        coords = [FretboardToCoord.open_coords[i] for i in strings]
        for c in coords:
            ax.text(x=c[0], y=c[1], s="O", color='orangered', fontsize=fontsize)
            
    def _display_muted_strings(self, ax: Axes, strings: list[int], fontsize: int = 5):
        coords = [FretboardToCoord.open_coords[i] for i in strings]
        for c in coords:
            ax.text(x=c[0], y=c[1], s="X", color='orangered', fontsize=fontsize)
        
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
            
    def plot_all(self):
        axs = self._create_base_image(no_subplots=len(self.diags))
        for idx, i in enumerate(self.diags):
            self._display_open_strings(axs[idx], i.open_strings, fontsize=7 // len(self.diags))
            self._display_muted_strings(
                axs[idx], i.muted_strings, fontsize=9 // len(self.diags)
            )
            for note in i.shape_coords:
                axs[idx].scatter(note[0], note[1], color='orangered', s=0.05 / len(self.diags))
        plt.axis('off')
        plt.show()
        
    def plot_by_idx(self, idx: int, save: bool = False, save_path: Path | None = None):
        ax = self._create_base_image(no_subplots=1)
        chord_shape = self.diags[idx]
        self._display_open_strings(ax, chord_shape.open_strings)
        self._display_muted_strings(ax, chord_shape.muted_strings)
        for note in chord_shape.shape_coords:
            ax.scatter(note[0], note[1], color='orangered', s=70)
            ax.set_title(f"{self._chord_string} chord |  plot# [{idx}]")
        if not save:           
            plt.show()
        if save and save_path:
            plt.savefig(str(Path(save_path / f"{self._chord_string}_{idx}.png")))
        plt.close()
        
    def save_all_plots(self, save_path: str | Path | None = None):
        p = (
            Path(save_path)
            if save_path
            else Path().resolve() / "export" / f"{self._chord_string}"
        )
        if not p.is_dir():
            p.mkdir(parents=True, exist_ok=True)
        for i in range(len(self.diags)):
            self.plot_by_idx(idx=i, save=True, save_path=p)
        
        

if __name__ == '__main__':
    cp = ChordShapePlot('Dm')
    # cp.plot_by_idx(1)
    # cp.plot_all()
        