import requests
import time

search_history = []
def main():
    global search_history
    load_search_history()
    while True:
        print('\n' * 20)
        print("Choose an option:")
        time.sleep(0.6)
        print("1. Search for a favorite food")
        time.sleep(0.6)
        print("2. View search history")
        time.sleep(0.6)
        print("3. Quit")
        time.sleep(0.6)
        choice = input("Enter the option number: ")
        if choice == '1':
            favorite_food = input("Please enter your favorite food: ")
            response = get_ingredients(favorite_food)
            if response is not None:
                meals = response.get('meals', [])
                if meals:
                    ingredients = []
                    for ingredient_number in range(1, 21):
                        ingredient_key = f'strIngredient{ingredient_number}'
                        ingredient = meals[0].get(ingredient_key)
                        if ingredient:
                            ingredients.append(ingredient)
                        else:
                            break

                    if ingredients:
                        ingredients = [ingredient.capitalize() for ingredient in ingredients]
                        ingredients.sort()
                        print("Ingredients for", favorite_food, " (alphabetically sorted):")
                        for ingredient in ingredients:
                            print(ingredient)
                            time.sleep(0.4)
                        time.sleep(3)
                        search_history.append(favorite_food)
                        save_search_history()
                    else:
                        print("No ingredients found for", favorite_food)
                else:
                    print("No information found for", favorite_food)
            else:
                print("Failed to retrieve data from the API.")
        elif choice == '2':
            print('\n' * 10)
            print("Search History:")
            for i, search in enumerate(search_history, start=1):
                print(f"{i}. {search}")
                time.sleep(0.4)
            time.sleep(3)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
def get_ingredients(food_name):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php"
    params = {'s': food_name}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return None
def save_search_history():
    with open("search_history.txt", "w") as file:
        for search in search_history:
            file.write(search + "\n")
def load_search_history():
    global search_history
    try:
        with open("search_history.txt", "r") as file:
            search_history = [line.strip() for line in file]
    except FileNotFoundError:
        search_history = []

if __name__ == '__main__':
    main()
