class Country:
    def __init__(self, name):
        self.name = name
        self.states = []
        self.UTs=[]
    
    def add_state(self, state):
        self.states.append(state)

    def add_UT(self, UT):
        self.UTs.append(UT)
    
    def get_state_names(self):
        return [state.name for state in self.states]
    
    def get_UT_names(self):
        return [UT.name for UT in self.UTs]


class State:
    def __init__(self, name):
        self.name = name
        self.districts = []
        self.cities = []
    
    def add_district(self, district):
        self.districts.append(district)
    
    def get_district_names(self):
        return [district.name for district in self.districts]



class District:
    def __init__(self, name):
        self.name = name
        self.cities = []
    
    def add_city(self, city):
        self.cities.append(city)
    
    def get_city_names(self):
        return [city.name for city in self.cities]


class City:
    def __init__(self, name):
        self.name = name


class UT:
    def __init__(self, name):
        self.name = name

india = Country("India")
delhi = UT("Delhi")
pondicherry = UT("pondicherry")
india.add_UT(delhi)
india.add_UT(pondicherry)
maharashtra = State("Maharashtra")
uttar_pradesh=State("Uttar pradesh")
india.add_state(maharashtra)
india.add_state(uttar_pradesh)
thane = District("thane")
pune = District("Pune")
nagpur = District("Nagpur")
maharashtra.add_district(thane)
maharashtra.add_district(pune)
maharashtra.add_district(nagpur)
badlapur=City("badlapur")
kalyan=City("kalyan")
maval=City("maval")
bhor=City("bhor")
thane.add_city(kalyan)
thane.add_city(badlapur)
pune.add_city(maval)
pune.add_city(bhor)
print(f"the country name is {india.name}")
print(f"These are the states of {india.name}->{india.get_state_names()}")

print(f"These are the Union Territories->{india.get_UT_names()}")

print(f"These are the district of maharashtra->{maharashtra.get_district_names()}")

print(f"These are the city of thane->{thane.get_city_names()}")  

print(f"These are the city of pune->{pune.get_city_names()}")  

print(f"These are the city of nagpur->{nagpur.get_city_names()}")
