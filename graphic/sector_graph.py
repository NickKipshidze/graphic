from .graph import Graph
import random

class SectorGraph(Graph):
    def __init__(self, labels: list[str], sizes: list[int], colors: list = None, 
                 radius: int = 250, center: tuple[int] = None,
                 resolution: tuple[int] = (512, 512), legend: bool = True) -> None:
        super().__init__(resolution)
        
        self.labels: list[str] = labels
        self.sizes: list[int] = sizes
        
        if not colors:
            self.colors: list[tuple[int]] = self.randcolors(amount = len(labels))
        else:
            self.colors = colors
            
        if not center:
            self.center: tuple[int] = (resolution[0]/2, resolution[1]/2)
        else:
            self.center: tuple[int] = center
        
        self.radius = radius
        
        self.draw_segments()
        
        if legend:
            self.draw_legend()
    
    def randcolor(self) -> tuple[int]:
        return tuple(random.choice(range(0, 255, 32)) for _ in range(3))
    
    def randcolors(self, amount: int) -> list[tuple[int]]:
        colors: list[tuple[int]] = []
        
        while len(colors) < amount:
            color: tuple[int] = self.randcolor()
            if color not in colors:
                colors.append(color)
        
        return colors
    
    def draw_legend(self, color: str = "#000000", background: str = "#cccccc",
                    vertical_gaps: int = 20, horizontal_gaps: int = 20, 
                    padding: int = 15, margin: int = 10, box_size: int = 35,
                    font_size: int = 28, font: str = "DejaVuSans.ttf", 
                    outline: int = 1) -> None:
        offset: tuple[int] = (margin, margin)
        
        self.rect(
            (offset[0], offset[1]),
            (
                len(max(self.labels, key=len)) * font_size + horizontal_gaps + padding*2 + box_size,
                len(self.labels) * (box_size + vertical_gaps) - vertical_gaps + padding*2
            ),
            fill = background,
            width = outline
        )
        
        for index, label in enumerate(self.labels):
            self.rect(
                (
                    offset[0] + padding,
                    index * (box_size + vertical_gaps) + padding + offset[1]
                ), 
                (box_size, box_size),
                fill = self.colors[index], 
                width = 0
            )
            self.text(
                (
                    box_size + padding + horizontal_gaps + offset[0], 
                    index * (box_size + vertical_gaps) + padding + offset[1]
                ), 
                label, font, font_size, color
            )
    
    def draw_segments(self) -> None:
        start_angle: int = 0
        
        for index, size in enumerate(self.sizes):
            self.segment(
                self.center, self.radius, start_angle, start_angle + size * 3.6,
                fill = self.colors[index]
            )
            start_angle += size * 3.6
