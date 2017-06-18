class RaceCar:
  
    def __init__(self,color,fuel_remaining,**kargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0  #to avoid..>>RaceCar.laps=10..etc 
        for key, value in kargs.items():
            setattr(self,key,value)
    
    def run_lap(self,length):
        self.fuel_remaining -= (length * .125) 
        self.laps += 1 