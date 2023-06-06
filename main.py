import os
import random

def read_places(filename):
    places = []
    with open(filename, 'r') as file:
        for line in file:
            name, country, priority, visited = line.strip().split(',')
            places.append({
                'name': name,
                'country': country,
                'priority': int(priority),
                'visited': visited == 'v'
            })
    return places

def write_places(filename, places):
    with open(filename, 'w') as file:
        for place in places:
            line = f"{place['name']},{place['country']},{place['priority']},{'v' if place['visited'] else 'n'}\n"
            file.write(line)

def display_places(places):
    unvisited_count = 0
    for idx, place in enumerate(places, 1):
        visited_marker = " " if place['visited'] else "*"
        print(f"{visited_marker}{idx}. {place['name']} in {place['country']} {place['priority']}")
        if not place['visited']:
            unvisited_count += 1
    print(f"{len(places)} places. You still want to visit {unvisited_count} places.")

def add_place(places):
    while True:
        name = input("Name: ").strip()
        if name:
            break
        print("Input can not be blank")
    while True:
        country = input("Country: ").strip()
        if country:
            break
        print("Input can not be blank")
    while True:
        try:
            priority = int(input("Priority: "))
            if priority > 0:
                break
            print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    places.append({
        'name': name,
        'country': country,
        'priority': priority,
        'visited': False
    })
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")

def mark_visited(places):
    display_places(places)
    while True:
        try:
            idx = int(input("Enter the number of a place to mark as visited\n>>> "))
            if idx > 0:
                if idx <= len(places):
                    if not places[idx - 1]['visited']:
                        places[idx - 1]['visited'] = True
                        print(f"{places[idx - 1]['name']} in {places[idx - 1]['country']} visited!")
                    else:
                        print("You have already visited", places[idx - 1]['name'])
                else:
                    print("Invalid place number")
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")
        if idx > 0:
            break

def recommend_place(places):
    unvisited = [place for place in places if not place['visited']]
    if unvisited:
        recommended = random.choice(unvisited)
        print(f"Not sure where to visit next?\nHow about... {recommended['name']} in {recommended['country']}?")
    else:
        print("No places left to visit!")

def main():
    filename = "places.csv"
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

    places = read_places(filename)
    print("Travel Tracker 1.0 - by ALLAHISRABB")
    print(f"{len(places)} places loaded from places.csv")
    while True:
        print("\nMenu:")
        print("L - List places")
        print("R - Recommend random place")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            places.sort(key=lambda x: (x['visited'], -x['priority']))
            display_places(places)
        elif choice == 'a':
            add_place(places)
        elif choice == 'm':
            mark_visited(places)
        elif choice == 'r':
            recommend_place(places)
        elif choice == 'q':
            write_places(filename, places)
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    main()