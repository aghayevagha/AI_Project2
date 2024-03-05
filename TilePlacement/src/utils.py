import math
#do not forget to change the this function in first place, it's name and etc
# func to extract all the required data from the file
def read_file( file_name):
    land = []
    areas = []
    tiles = {}
    target = {}
    with open(file_name, 'r') as file:
    #getting the inital landscape
        for line in file:
            if "Landscape" in line:
                break
        else: raise ValueError(f"could not find landscape")
        count = 0
        for line in file:
            count += 1
            line = list(line)[:-1]
            line = list(map(lambda x: x.replace(' ', '0'), line))
            line = list(map(lambda x: int(x), line))
            line = [value for index, value in enumerate(line) if index%2 == 0]
            land.append(line)
            if count > len(line)-1:
                break
        for i in range(0, len(land), 4):
            for j in range(0, len(land[0]), 4):
                area = [row[j:j+4] for row in land[i:i+4]]
                areas.append(area)
        # getting the number of tiles
        for line in file:
            if "Tiles" in line:
                break
        else: raise ValueError("could not find tiles")
        line = file.readline()
        line = line.strip("{}\n")
        line = line.split(", ")
        for pair in line:
            key, value = pair.split("=")
            tiles[key] = int(value)
        # getting the final count of bushes
        for line in file:
            if "Targets" in line:
                break
        else: raise ValueError("could not find targets")
        for _ in range(4):
            temp = file.readline()
            temp = temp.strip()
            temp = temp.split(":")
            target[int(temp[0])] = int(temp[1])
    return areas, tiles, target 

def check(area, current_state, path):
    #calculate the number of tiles of each type
    count_L = path.count('L_1') + path.count('L_2') + path.count('L_3') + path.count('L_4')
    count_full = path.count('Full_block')
    count_out = path.count('Outer_block')
    if (count_L > area.tiles['EL_SHAPE']) or (count_full > area.tiles['FULL_BLOCK']) or (count_out > area.tiles['OUTER_BOUNDARY']):
      return False

    #calculate the visible bushes difference from goal state
    difference = {key: area.targets[key] - current_state[key] for key in area.targets if key in current_state}
    goal = True
    for value in difference.values():
      if value != 0:
        goal = False
        break
    #reached the goal 
    if goal:
     return True
    # uncovered too many bushes
    if min(difference.values()) < 0:
      return False
   
    return None

def MRV(area, current_index, current_sum, functions):  

    # check if reached the final state
    if current_index == len(area.landscapes):
      if check(area,current_sum, area.path) == True :           
        return True
      else: return False
    
    #applying MRV heuristic
    else:
      all_functions = [f for f in functions]
      all_functions = sorted(all_functions, key=lambda f: len([v for v in f(area.landscapes[current_index]).values() if v > 0]))
      
      for func in all_functions:
        area.path.append(func.__name__)
        applied_area = func(area.landscapes[current_index])
          
        current_bushes = {}
        for key in applied_area:
          if key in current_sum:
            current_bushes[key] = current_sum[key] + applied_area[key]
            
        # check constraints
        if check(area,current_bushes, area.path) == False:
          area.path.pop()
          continue
                          
        solution = MRV(area,current_index + 1, current_bushes, functions)
                
        if solution: return True
        else: area.path.pop()

      return False
    
#transform the land if there is a solution
def convert(land):
  for index, tile in enumerate(land.path):
    temp = getsquare()
        
    if tile == 'Full_block':
      land.landscapes[index] = temp
    elif tile == 'Outer_block':
      restore_inside(land.landscapes[index], temp, "outer")
      land.landscapes[index] = temp
    elif tile in ['L_1', 'L_2', 'L_3', 'L_4']:
      restore_inside(land.landscapes[index], temp, tile)
      land.landscapes[index] = temp
    else:
      raise ValueError("tile type is not recognized")  
  return counter(land)

#4*4 matrix
def getsquare():
      return [[0 for _ in range(4)] for _ in range(4)]
      
def restore_inside(source, dest, tile):
  if tile == "outer":
    rows, cols = slice(1, -1), slice(1, -1)
  elif tile.startswith("L"):
    if tile == "L_1":
      rows, cols = slice(None, -1), slice(1, None)
    elif tile == "L_2":
      rows, cols = slice(1, None), slice(1, None)
    elif tile == "L_3":
      rows, cols = slice(None, -1), slice(None, -1)
    elif tile == "L_4":
      rows, cols = slice(1, None), slice(None, -1)

  for r_dest, r_source in zip(dest[rows], source[rows]):
          r_dest[cols] = r_source[cols]

def counter(land):
  target_bushes = {1:0, 2:0, 3:0, 4:0}
  for area in land.landscapes:
    for row in area:
      for i in range(1,4):
        target_bushes[i] += row.count(i)    
  return target_bushes


  