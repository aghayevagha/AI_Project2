import math
class TilePlacement:

  def __init__(self, areas, tiles, target):
    self.path = []
    self.landscapes = areas
    self.tiles = tiles
    self.targets = target

  def print_land(self):
    rows = int(math.sqrt(len(self.landscapes)))
    areas = ""
    for i in range(0, len(self.landscapes), rows):
      area=self.landscapes[i:i+rows]
      result = ""
      for k in range(4):
        temp = ""
        for x in area:
          row_str = str(x[k]).strip("[]")
          row_str = row_str.replace(',', '')
          row_str = row_str.replace('0', ' ')
          temp = temp + row_str+" " 
        result = result + temp + "\n"
      areas += result 
    print(areas)

