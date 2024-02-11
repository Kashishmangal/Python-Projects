movies = []

"""
movie={
    'name':... (str),
    'director':... (str),
    'year':... (int)
}
"""


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your your movies, 'f' to find a movie, 'q' to quit.")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command- Please try again.')
        user_input = input("\nEnter 'a' to add a movie, 'l' to see your your movies, 'f' to find a movie, 'q' to quit.")


def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the director name: ')
    year = input('Enter the release year: ')

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()