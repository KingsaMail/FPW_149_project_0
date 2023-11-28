class Plaer:
    """Класс игрок."""
    
    def __init__(self, name, chip, position) -> None:
        self._name = name
        self._chip = chip
        self._position = position
        self._score = 0
        
    @property  
    def name(self):
        # Вывод имени игрока
        return self._name
    
    @name.setter
    def name(self, name):
        #Вввод имени игрока
        self._name = name
    
    @property
    def chip(self):
        #фишка которой игрок ходит
        return self._chip
    
    @chip.setter
    def chip(self, chip):
        #Назначение фишки игрока
        self._chip = chip
        
    @property
    def position(self):
        #фишка которой игрок ходит
        return self._position
    
    @position.setter
    def position(self, position):
        #Назначение фишки игрока
        self._position = position
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, ver):
        self._score += ver
        
        
class FieldOfGame:
    """Поле игры."""
               
    def __init__(self) -> None:                   
        self._field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    @property    
    def field(self):
        return self._field
           
    def field_set(self, poz, chip):
        self._field[(poz-1)] = chip
        
    def chek(self, chip):
        if any([
            self.field[0] == chip and self.field[3] == chip and self.field[6] == chip,
            self.field[1] == chip and self.field[4] == chip and self.field[7] == chip,
            self.field[2] == chip and self.field[5] == chip and self.field[8] == chip,
            self.field[0] == chip and self.field[1] == chip and self.field[2] == chip,
            self.field[3] == chip and self.field[4] == chip and self.field[5] == chip,
            self.field[6] == chip and self.field[7] == chip and self.field[8] == chip,
            self.field[2] == chip and self.field[4] == chip and self.field[6] == chip,
            self.field[0] == chip and self.field[4] == chip and self.field[8] == chip
        ]):
            return True
        
    def drow(self):
        
        print('  ', self._field[0], ' | ', self._field[1], ' | ', self._field[2])
        print(' ','-'*15)
        print('  ',self._field[3], ' | ', self._field[4], ' | ', self._field[5])
        print(' ','-'*15)
        print('  ',self._field[6], ' | ', self._field[7], ' | ', self._field[8])        
        return f""


if __name__ == '__main__':
    field = FieldOfGame()
    print(field.drow())