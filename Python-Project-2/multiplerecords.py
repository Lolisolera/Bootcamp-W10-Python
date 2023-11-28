from connect import *

def multiple_insert():
   
    recipeData = [
        ('Chocolate Cake', ('Flour', 'Sugar', 'Cocoa Powder', 'Eggs', 'Milk'), '1. Mix dry ingredients. 2. Add wet ingredients. 3. Bake at 350°F.'),
        ('Chicken Alfredo Pasta', ('Chicken', 'Fettuccine', 'Alfredo Sauce', 'Garlic'), '1. Cook chicken. 2. Boil pasta. 3. Mix with Alfredo sauce.'),
        ('Vegetarian Stir-Fry', ('Broccoli', 'Bell Peppers', 'Carrots', 'Tofu', 'Soy Sauce'), '1. Sauté vegetables. 2. Add tofu. 3. Stir in soy sauce.'),
        ('Spaghetti Bolognese', ('Ground Beef', 'Tomatoes', 'Onion', 'Garlic', 'Spaghetti'), '1. Brown beef. 2. Sauté onions and garlic. 3. Add tomatoes. 4. Serve over spaghetti.'),
        ('Greek Salad', ('Cucumbers', 'Tomatoes', 'Feta Cheese', 'Olives', 'Olive Oil'), '1. Chop vegetables. 2. Toss with feta and olives. 3. Drizzle with olive oil.'),
        ('Chicken Caesar Salad', ('Grilled Chicken', 'Romaine Lettuce', 'Croutons', 'Caesar Dressing'), '1. Grill chicken. 2. Toss with lettuce, croutons, and dressing.'),
        ('Vegetable Curry', ('Potatoes', 'Cauliflower', 'Peas', 'Curry Sauce'), '1. Boil potatoes. 2. Sauté cauliflower and peas. 3. Simmer in curry sauce.'),
        ('Homemade Pizza', ('Pizza Dough', 'Tomato Sauce', 'Cheese', 'Toppings of choice'), '1. Roll out dough. 2. Spread sauce and add toppings. 3. Bake until crust is golden.'),
        ('Oatmeal Breakfast Bowl', ('Oats', 'Almond Milk', 'Berries', 'Nuts', 'Honey'), '1. Cook oats with almond milk. 2. Top with berries, nuts, and a drizzle of honey.'),
        ('Grilled Salmon', ('Salmon Fillets', 'Lemon', 'Garlic', 'Herbs'), '1. Marinate salmon in lemon, garlic, and herbs. 2. Grill until cooked through.'),
        ('Avocado Toast', ('Whole Wheat Bread', 'Avocado', 'Salt', 'Pepper', 'Red Pepper Flakes'), '1. Toast bread. 2. Mash avocado on top. 3. Season with salt, pepper, and red pepper flakes.'),
        ('Chocolate Chip Cookies', ('Flour', 'Butter', 'Sugar', 'Eggs', 'Chocolate Chips'), '1. Cream butter and sugar. 2. Mix in eggs and flour. 3. Fold in chocolate chips. 4. Bake until golden.')
    ]
    
    # Convert tuple to string for Ingredients column
    recipeData = [(name, ', '.join(ingredients), instructions) for name, ingredients, instructions in recipeData]

    dbCursor.executemany("INSERT INTO recipeBook (RecipeName, Ingredients, Instructions) VALUES(?,?,?)", recipeData)

    # Commit the change
    dbCon.commit()

    print(recipeData[1], "Added to recipeBook table")

multiple_insert()
