import requests
import json

url = "http://localhost:8000/api/recipes/"
data = {
    "food_name": "Spaghetti Carbonara",
    "preparation_time": "15 mins",
    "cooking_time": "20 mins",
    "total_time": "35 mins",
    "course": "Main Course",
    "cuisine": "Italian Cuisine",
    "servings": 4,
    "calories": 500,
    "preparation_instructions": 
        "1. Boil water with a pinch of salt and cook the spaghetti until al dente.\n2. In a bowl, whisk together eggs, cheese, salt, and pepper.\n3. Fry pancetta in a pan until crispy.\n4. Drain spaghetti, reserving some pasta water.\n5. Mix hot spaghetti with pancetta, then quickly stir in the egg mixture, adding reserved pasta water as needed for creaminess.\n6. Serve immediately, topped with more grated cheese and black pepper.",
    "ingredients": [
        {
            "name": "Spaghetti",
            "quantity": "400 g"
        },
        {
            "name": "Eggs",
            "quantity": "4 large"
        },
        {
            "name": "Grated Pecorino Romano cheese",
            "quantity": "100 g"
        },
        {
            "name": "Pancetta",
            "quantity": "150 g"
        },
        {
            "name": "Salt",
            "quantity": "to taste"
        },
        {
            "name": "Black pepper",
            "quantity": "to taste"
        }
    ]
}


response = requests.post(url, json=data)

# Check status code
if response.status_code == 201:  # HTTP 201 Created
    print("Recipe created successfully")
    print(response.json())
else:
    print(f"Failed to create recipe. Status code: {response.status_code}")
    # print(response.text)  # Print the raw response to help debug
