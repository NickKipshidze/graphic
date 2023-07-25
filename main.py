from graphic import SectorChart

# "I always use numbers that are power of two as constants"
#                                   - Nick Kipshidze - 2023

pie = SectorChart(
    labels = ["Sleep", "Programming", "Rest"],
    sizes = [5, 85, 10],
    resolution = (1024, 512),
    radius = 250
)

pie.save("output.png")
