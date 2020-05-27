class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        """Constructor of recipes"""
        assert name and isinstance(name, str), "name id missing or name isn't a str"
        assert cooking_lvl and isinstance(cooking_lvl, int) and 5 >= cooking_lvl >= 1,\
            "cooking should be an integer and between 1 and 5 "
        assert cooking_time and isinstance(cooking_time, int) and (cooking_time > 0), "cooking time should be a " \
                                                                                      "positive integer "
        assert ingredients and isinstance(ingredients, list), "ingredients should be a list"
        assert isinstance(description, str)
        assert recipe_type and isinstance(recipe_type, str) and\
            (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"),\
            "recipe type should be an str and a starter/lunch/dessert"
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        # print(self)

    def __str__(self):
        """Return the string to print with the recipe info"""
        formatted_string = "{0} RECIPE:\n\tcooking lvl\t\t: {1}/5\n\tcooking time ( min )\t: {2}\n\tingredients\t\t: "
        for i in range(0, len(self.ingredients)):
            formatted_string += "{3[" +str(i) + "]}, "
        formatted_string = formatted_string[:len(formatted_string) - 2]
        formatted_string += "\n\tdescription\t\t: {4}\n\trecipe type\t\t: {5}\n"
        return formatted_string.format(self.name.upper(), self.cooking_lvl, self.cooking_time, self.ingredients,
                                       self.description, self.recipe_type)

