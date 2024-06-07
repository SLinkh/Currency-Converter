import pygame

class Image Or Print Options:

# Set Image Or Print Options
options = ImageOrPrintOptions()
# set Horizontal resolution
options.setHorizontalResolution(200)
# set Vertica Resolution
options.setVerticalResolution(300)

# Instantiate Workbook
book = Workbook("Book2.xlsx")
# Save chart as Image using ImageOrPrint Options
book.getWorksheets().get(3).getCharts().get(0).toImage("chart.png", options)