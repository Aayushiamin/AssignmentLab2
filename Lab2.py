def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Aayushi Amin',
        'student_id' : '10284516',
        'pizza_topings' : ['RED ONION','BELL PAPER','SPINACH'],
        'movies' : [
            {
                'title' : 'zindgi na milegi dobara',
                'genre' : 'comady-drama',
    
            },
            {
                'title' : 'bhool bhulaiya',
                'genre' : 'comedy',
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title':'yeh jawani hai diwani','genre':'romentic comedy-drama'})
    
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me,['zucchini','basil','thyme'])
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    
    First_Name = about_me['full_name'].split('')[0]
    print(f'My name is {about_me["full_name"]}, but you can acll me Ms. {First_Name}.')
    print(f'My student ID is {about_me["student_id"]}.')

    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, Add_toppings):

    about_me['pizza_topings'].extend(Add_toppings)
    about_me['pizza_topings'].sort()

    for P,toppings in enumerate(about_me['pizza_topings']):
        about_me['pizza_topings'][P] = toppings.lower()

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):

    print('\nMy favourite pizza toppings are: ')

    for toppings in about_me['pizza_topings']:
        print(f'-{toppings}')

    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    print(f'I like to watch', end='')
    Movie_Genres = [Genres[Movie_Genres]] 

    for Genres in about_me['movies'][:-1]:
        print(','.join(Movie_Genres), end='.\n')

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):

    print(f'Some of my favourite movies are', end='')
    Movie_Titles = [Titles['Movie_Titles'].title()]

    for Titles in movie_list['movies']:
        print(','.join(Movie_Titles), end='!\n')

    return
    
if __name__ == '__main__':
    main()