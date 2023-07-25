from PIL import Image, ImageDraw, ImageFont
import random

class Graph:
    def __init__(self, resolution: tuple[int]) -> None:
        self.image = Image.new("RGB", resolution, "white")
        self.draw = ImageDraw.Draw(self.image)
    
    def circle(self, center: tuple[int], radius: int, fill: str = "#000000") -> None:
        self.draw.ellipse(
            (
                center[0] - radius, center[1] - radius, 
                center[0] + radius, center[1] + radius
            ),
            fill = fill
        )
    
    def segment(self, center: tuple[int], radius: int, start_angle: int, end_angle: int, fill: str = "#000000"):
        self.draw.arc(
            (
                center[0] - radius, center[1] - radius, 
                center[0] + radius, center[1] + radius
            ),
            start_angle - 90, end_angle - 90,
            fill = fill,
            width = radius
        )
                
    def line(self, start: tuple[int], end: tuple[int], fill: str = "#111111", width: int = 2) -> None:
        self.draw.line([start, end], fill = fill, width = width)
    
    def rect(self, position: tuple[int], size: tuple[int], fill: str = "#ffffff", outline: str = "#000000", width: int = 4) -> None:
        self.draw.rectangle(
            [
                position, 
                (
                    position[0] + size[0],
                    position[1] + size[1]
                )
            ],
            fill = fill,
            outline = outline, 
            width = width
        )

    def text(self, position: tuple[int], text: str, font: str, size: int = 32) -> None:
        self.draw.text(
            position, text, fill="black",
            font = ImageFont.truetype(font, size)
        )

    def save(self, filename: str = "output.png") -> None:
        self.image.save(filename)

class SectorChart(Graph):
    def __init__(self, labels: list[str], sizes: list[int], colors: list[any] = None, radius: int = 250, resolution: tuple[int] = (512, 512)) -> None:
        super().__init__(resolution)
        
        self.labels: list[str] = labels
        self.sizes: list[int] = sizes
        
        if not colors:
            self.colors: list[tuple[int]] = self.randcolors(amount = len(labels))
        else:
            self.colors = colors
        
        self.radius = radius
        self.resolution = resolution
        
        self.draw_segments()
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
    
    def draw_legend(self, offset: tuple[int] = (0, 0), size: int = 32) -> None:
        for index, label in enumerate(self.labels):
            self.rect(
                (10 + offset[0], index * (size + 10) + 10 + offset[1]), (size, size),
                fill = self.colors[index], width = 0
            )
            self.text(
                (size + 20 + offset[0], index * (size + 10) + 10 + offset[1]), 
                label, "Hermit-Regular.otf", size - 7
            )
    
    def draw_segments(self) -> None:
        start_angle: int = 0
        
        for index, size in enumerate(self.sizes):
            self.segment(
                (
                    self.resolution[0]/2, 
                    self.resolution[1]/2
                ),
                self.radius, start_angle, start_angle + size * 3.6,
                fill = self.colors[index]
            )
            start_angle += size * 3.6
