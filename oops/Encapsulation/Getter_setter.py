class Bank:
    def get_value(self):
        print(self.__balance)
    def set_value(self,balance):
        self.__balance=balance    
        
  
Sbi =Bank()
Sbi.set_value(5000)
Sbi.get_value()
      