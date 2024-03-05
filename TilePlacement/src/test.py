from main import main

def test():
    try:
        assert main("inputs/example.txt",False) == True
        #assert main("inputs/example.txt",False) == False
        print("all passed!")   
    except:    
        print('failed!')
     
test()

