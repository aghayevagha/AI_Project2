from utils import *
from TilePlacement import TilePlacement
from shapes import shapes
       
def main(file_name,printing = True):
    areas, tiles, target = read_file(file_name)  
    land=TilePlacement(areas, tiles, target)
    if(printing):
        land.print_land()
        print("----------------------------------------")
    solution = MRV(land,0, {1:0, 2:0, 3:0, 4:0}, shapes())
    if solution:
        if(printing):
            convert(land)
            land.print_land()
            print('Found the solution!')
            print("Target: ", land.targets,"\n")
            print("Final Path:")
            for i in range(len(land.path)):
                print(i,":" , land.path[i])
        return True
    else:
        print("No path!")
        return False



if __name__ == "__main__":
    #adjust the file name
    file_name="inputs/example.txt"
    main(file_name)    