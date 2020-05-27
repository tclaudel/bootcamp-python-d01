from datetime import datetime


class Book:
    def __init__(self, name):
        assert name and isinstance(name, str)
        self.name = name
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.recopies_list = {
            'starter': [],
            'lunch': [],
            'dessert': [],
        }

    def __str__(self):
        formatted_string = "{0} BOOK\n\tlast update\t: {1}\n\tcreation date\t: {2}\n\tstarter recipes\t:\n\n"
        for i in range(0, len(self.recopies_list["starter"])):
            formatted_string += "\t\t{3[" + str(i) + "]}\n"
        formatted_string = formatted_string[:len(formatted_string) - 1]
        formatted_string += "\n\tlunch recipes\t:\n\n"
        for i in range(0, len(self.recopies_list["lunch"])):
            formatted_string += "\t\t{4[" + str(i) + "]}\n"
        formatted_string = formatted_string[:len(formatted_string) - 1]
        formatted_string += "\n\tdessert recipes\t:\n\n"
        for i in range(0, len(self.recopies_list["dessert"])):
            formatted_string += "\t\t{5[" + str(i) + "]}\n"
        return formatted_string.format(self.name.upper(), self.last_update, self.creation_date,
                                       self.recopies_list["starter"], self.recopies_list["lunch"],
                                       self.recopies_list["lunch"])

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for element in self.recopies_list.values():
            for j in range(0, len(element)):
                if element[j].name == name:
                    return element[j]

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        return self.recopies_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            self.recopies_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        except (TypeError, AttributeError):
            print("TypeError:   recipe must be a Recipe type")
