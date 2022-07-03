import subprocess
import os
                                                                                                                                                     
class Makefile:                                                                                                                                      
    def __init__(self,path):                                                                                                                         
        _ = False                                                                                                                                    
        for i in os.listdir(path):                                                                                                                   
            if i.lower() == "makefile":                                                                                                              
                self.abspath = os.path.join(path,i)                                                                                                  
                _ = True                                                                                                                             
                                                                                                                                                     
        assert _                                                                                                                                     
        self.instructions = []                                                                                                                       
        for l in open(self.abspath).readlines():                                                                                                     
            if ":" in l:                                                                                                                             
                self.instructions.append(l.split(":")[0])                                                                                            
                                                                                                                                                     
                                                                                                                                                     
def is_makefile(p):                                                                                                                                  
    try:                                                                                                                                             
        Makefile(p)                                                                                                                                  
        return True                                                                                                                                  
    except:                                                                                                                                          
        return False                                                                                                                                 
                                                                                                                                                     
                                                                                                                                                     
def make(path,instructions):                                                                                                                         
    assert is_makefile(path)                                                                                                                         
    os.chdir(path)                                                                                                                                   
    subprocess.call(instructions)
