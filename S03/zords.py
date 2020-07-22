class DinoZord:
    '''Clase base ejemplo.
    
    Tiene asociadas las propiedades: pilot, name y ability. Los demás atributos
    Son privados y DEBEN ser entregados al momento de instanciar un objeto. La
    excepción es el atributo _color que es protegido. El método principal 
    es attack. 
    '''
    
    def __init__(self, attribute_dict, construction_dict):
        self.pilot = None
        self.name = attribute_dict['name']
        self._color = attribute_dict['color']
        self.ability = attribute_dict['ability']
        self.__length = construction_dict['length']
        self.__weight  = construction_dict['weight']
        self.__speed = construction_dict['speed']
    
    # Propiedades
    @property
    def pilot(self):
        return self.__pilot

    @pilot.setter
    def pilot(self, pilot):
        self.__pilot = pilot
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def ability(self):
        return self.__ability

    @ability.setter
    def ability(self, ability):
        self.__ability = ability
    
    #Getter
    def get_attr(self):
        return self.__length, self.__weight, self.__speed
    
    # Método de ataque
    def attack(self):
        print(self.name + ' ataca usando ' + self.ability + '!!')
        
        
# Se Fabrican 5 clases que heredan de DinoZord
class Tyrannosaurus(DinoZord):
    '''Clase derivada - Herencia simple'''

    # Atributos estaticos de la clase - privatizados sin setter ni getter!
    __construction_dict = {'length': 45, 'weight': 96, 'speed': 120}

    __attribute_dict = {
        'name': 'Tyrannosaurus Dinozord',
        'color': 'red',
        'ability': 'fire energy blasts',
    }

    # Se utililiza el método constructor directamente desde la clase base
    def __init__(self):
        DinoZord.__init__(self, self.__attribute_dict, self.__construction_dict)

    # Método protegido de ensamblaje
    def _modo(self):
        if self.pilot:
            print(self.pilot + ' dice: ensamblando torso y cabeza')

    def boost_dexterity(self):
        print('Zord con destreza mejorada')

class Mastodon(DinoZord):
    '''Clase derivada - Herencia simple'''

    # Atributos estaticos de la clase - privatizados sin setter ni getter!
    __construction_dict = {'length': 24.7, 'weight': 108, 'speed': 120}

    __attribute_dict = {
        'name': 'Mastodon Dinozord',
        'color': 'black',
        'ability': 'frigid blasts of cold air',
    }

    # Se utililiza el método constructor directamente desde la clase base
    def __init__(self):
        DinoZord.__init__(self, self.__attribute_dict, self.__construction_dict)

    # Método protegido de ensamblaje
    def _modo(self):
        if self.pilot:
            print(self.pilot + ' dice: ensamblando espalda y brazos')

    def boost_strength(self):
        print('Zord con fuerza mejorada')

class Triceratops(DinoZord):
    '''Clase derivada - Herencia simple'''

    # Atributos estaticos de la clase - privatizados sin setter ni getter!
    __construction_dict = {'length': 37.3, 'weight': 141, 'speed': 140}

    __attribute_dict = {
        'name': 'Triceratops Dinozord',
        'color': 'blue',
        'ability': 'laser shots',
    }

    # Se utililiza el método constructor directamente desde la clase base
    def __init__(self):
        DinoZord.__init__(self, self.__attribute_dict, self.__construction_dict)

    # Método protegido de ensamblaje
    def _modo(self):
        if self.pilot:
            print(self.pilot + ' dice: ensamblando pierna izquierda')

    def boost_endurance(self):
        print('Zord con resistencia mejorada')


class Sabertooth(DinoZord):
    '''Clase derivada - Herencia simple'''

    # Atributos estaticos de la clase - privatizados sin setter ni getter!
    __construction_dict = {'length': 37.3, 'weight': 141, 'speed': 150}

    __attribute_dict = {
        'name': 'Sabertooth Tiger Dinozord',
        'color': 'yellow',
        'ability': 'large yellow laser',
    }

    # Se utililiza el método constructor directamente desde la clase base
    def __init__(self):
        DinoZord.__init__(self, self.__attribute_dict, self.__construction_dict)

    # Método protegido de ensamblaje
    def _modo(self):
        if self.pilot:
            print(self.pilot + ' dice: ensamblando pierna derecha')

    def boost_agility(self):
        print('Zord con agilidad mejorada')

class Pterodactyl(DinoZord):
    '''Clase derivada - Herencia simple'''

    # Atributos estaticos de la clase - privatizados sin setter ni getter!
    __construction_dict = {'length': 21, 'weight': 84, 'speed': 'match 2.5'}

    __attribute_dict = {
        'name': 'Pterodactyl Dinozord',
        'color': 'pink',
        'ability': 'twin lasers',
    }

    # Se utililiza el método constructor directamente desde la clase base
    def __init__(self):
        DinoZord.__init__(self, self.__attribute_dict, self.__construction_dict)

    # Método protegido de ensamblaje
    def _modo(self):
        if self.pilot:
            print(self.pilot + ' dice: ensamblando pecho')

    def boost_defense(self):
        print('Zord con defensa mejorada')
        

class MegaZord(Tyrannosaurus, Mastodon, Triceratops, Sabertooth, Pterodactyl):
    '''Clase derivada - Ejemplo herencia multiple'''

    # Valores de Dinozord, clase base heredada de cada clase base
    __construction_dict = {'length': 67, 'weight': 570, 'speed': 140}

    __attribute_dict = {
        'name': 'Mega Zord',
        'color': 'Multicolor',
        'ability': 'Power Sword',
    }
    
    
    # Constructor
    def __init__(self, tyrannosaurus, mastodon, triceratops, sabertooth,
                 pterodactyl):
        
        # Secuencia de ensamblaje
        tyrannosaurus._modo()
        mastodon._modo()
        triceratops._modo()
        sabertooth._modo()
        pterodactyl._modo()
        
        '''
        Constructor de caracteristicas base usando la clase base DinoZord, 
        observe que no se declaro explicitamente como clase base al definir
        MegaZord, sin embargo sus atributos se heredan.
        
        ''' 
        
        DinoZord.__init__(self, self.__attribute_dict, self.__construction_dict)
        
        # variables de la clase
        self.__components = (tyrannosaurus, mastodon, triceratops, sabertooth,
                             pterodactyl)
        self.__mode = 'tank_mode'
        
        # asignación de piloto
        self.pilot = [zord.pilot for zord in  self.__components]
        
        # Fin secuencia de construcción
        print()
        print('Megazord activado en ' + self.__mode + '!' )
    
    ''' Métodos: overriding y métodos nuevos.'''
    
    # method overriding
    def _modo(self):
        return self.__mode
    
    # Nueva funcionalidad: wrapper de métodos heredados por herencia multiple
    def boost(self):
        self.boost_dexterity()
        self.boost_defense()
        self.boost_agility()
        self.boost_endurance()
        self.boost_strength()
    
    # Nueva funcionalidad: cambio de modo
    def change_mode(self):
        if self.__mode == 'battle_mode':
            print('Cambiando a Tank Mode')
            self.__mode = 'tank_mode'
            
        else:
            print('Cambiando a Battle Mode')
            self.__mode = 'battle_mode' 

