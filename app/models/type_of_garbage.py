

class TypeOfGarbage:

    plastic = {"name_pt": "Plástico", "color": "red", "name": "Plastic"}
    glass = {"name_pt": "Vidro", "color": "green", "name": "Glass"}
    organic = {"name_pt": "Orgânico", "color": "brown", "name": "Organic"}
    paper = {"name_pt": "Papel", "color": "blue", "name": "Paper"}
    metal = {"name_pt": "Metal", "color": "yellow", "name": "Metal"}

    def get_type(self, type_name):
        if self.__getattribute__(type_name):
            return self.__getattribute__(type_name)
        return {}
