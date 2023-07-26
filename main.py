from graphic import SectorGraph

pie = SectorGraph(
    labels = ["C", "Rust", "Python", "Ruby", "C++", "PHP", "JavaScript", "Java", "C#"],
    sizes = [3.2, 8.4, 27.5, 5.3, 13.7, 1.5, 20.6, 16.0, 3.8],
    resolution = (780, 512),
    radius = 250,
    center = (520, 256),
    legend = False
)

pie.draw_legend(
    padding = 10,
    box_size = 20,
    font_size = 18,
    outline = 0,
    vertical_gaps = 10
)

pie.save("output.png")
