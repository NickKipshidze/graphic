from PIL import Image, ImageDraw, ImageFont

class Graph:
    def __init__(self, resolution: tuple[int]) -> None:
        self.resolution: tuple[int] = resolution
        self.image: Image = Image.new("RGB", resolution, "white")
        self.draw: ImageDraw = ImageDraw.Draw(self.image)
    
    def circle(self, center: tuple[int], radius: int, 
               fill: str = "#000000") -> None:
        self.draw.ellipse(
            (
                center[0] - radius, center[1] - radius, 
                center[0] + radius, center[1] + radius
            ),
            fill = fill
        )
    
    def segment(self, center: tuple[int], radius: int, start_angle: int, 
                end_angle: int, fill: str = "#000000") -> None:
        self.draw.arc(
            (
                center[0] - radius, center[1] - radius, 
                center[0] + radius, center[1] + radius
            ),
            start_angle - 90, end_angle - 90,
            fill = fill,
            width = radius
        )
                
    def line(self, start: tuple[int], end: tuple[int], fill: str = "#111111", 
             width: int = 2) -> None:
        self.draw.line([start, end], fill = fill, width = width)
    
    def rect(self, position: tuple[int], size: tuple[int], fill: str = "#ffffff",
             outline: str = "#000000", width: int = 4) -> None:
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

    def text(self, position: tuple[int], text: str, font: str, size: int = 32, 
             color: str = "#000000") -> None:
        self.draw.text(
            position, text, fill = color,
            font = ImageFont.truetype(font, size)
        )

    def save(self, filename: str = "output.png") -> None:
        self.image.save(filename)
