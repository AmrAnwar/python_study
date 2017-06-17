class Student:
    def __init__(self, name, **kargs):
        self.name = name
        for key, value in kargs.items() :
            setattr(self, key, value)
        
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()
