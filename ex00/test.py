from book import Book
from recipe import Recipe


bread = Recipe("bread", 4, 60, ["flavor", "water"], "french bread", "starter")
carbonara = Recipe("Carbonara", 4, 60, ["pasta", "bacon", "eggs"], "Pastas with bacon and eggs", "lunch")
basics = Book("basics")
basics.add_recipe(bread)
basics.add_recipe(carbonara)

print(basics)
