# cli for task4
countries=[]
class Country:
    def __init__(self, name):
        self.name = name
        self.states = []
        self.UTs=[]
    
    def add_state(self, state):
        self.states.append(state)

    def add_UT(self, UT):
        self.UTs.append(UT)
    
    def get_state(self):
        return [state for state in self.states]
    
    def get_UT(self):
        return [UT for UT in self.UTs]


class State:
    def __init__(self, name):
        self.name = name
        self.districts = []
    
    def add_district(self, district):
        self.districts.append(district)
    
    def get_district(self):
        return [district for district in self.districts]
    
    def __str__(self) -> str:
        return 



class District:
    def __init__(self, name):
        self.name = name
        self.cities = []
    
    def add_city(self, city):
        self.cities.append(city)
    
    def get_city(self):
        return [city for city in self.cities]


class City:
    def __init__(self, name):
        self.name = name


class UT:
    def __init__(self, name):
        self.name = name

while True:
    if len(countries)==0:
        print(f"Current list of countries {countries}")
        input1=input("Press n for new country and e for exit ")
    else:
        for country in countries:
            print(country.name)
            for state in country.get_state():
                print(f"    {state.name}")
                for district in state.get_district():
                    print(f"        {district.name}")
                    for city in district.get_city():
                        print(f"            {city.name}")
            for ut in country.get_UT():
                print(f"    {ut.name}")


    if input1.lower()=="n":
        country=Country(input("Enter the country name "))
        countries.append(country)
        print(f"Current list of countries {[country.name for country in countries]}")

        no_states=int(input("enter the number of states you want to enter "))
        for i in range(no_states):
            country.add_state(State(input(f"Enter the state {i+1} ")))
        print([state.name for state in country.get_state()])

        for state in country.get_state():
            qty=int(input(f"please enter the number of district in {state.name} "))
            for i in range(qty):
                state.add_district(District(input(f"Enter the district {i+1} ")))
            print([district.name for district in state.get_district()])

            for district in state.get_district():
                qty=int(input(f"please enter the number of city in {district.name} "))
                for i in range(qty):
                    district.add_city(City(input(f"Enter the city {i+1} ")))
                print([city.name for city in district.get_city()])

        

            



        no_ut=int(input("enter the number of UT's you want to enter"))
        for i in range(no_ut):
            country.add_UT(UT(input(f"Enter the UT {i+1} ")))
        print([ut.name for ut in country.get_UT()])

    elif input1.lower()=="e":
        break;
    else:print("enter a valid input")

