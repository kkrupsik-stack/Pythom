def Constructor(details, figures, cars, trees):

    required_details = 72
    required_figures = 4
    required_cars = 2
    required_trees = 7

    possible_details = details // required_details
    possible_figures = figures // required_figures
    possible_cars = cars // required_cars
    possible_trees = trees // required_trees

   
    total_sets = min(possible_details, possible_figures, possible_cars, possible_trees)

    return total_sets

print(Constructor(144, 8, 4, 14))  
print(Constructor(10000, 16, 6, 2))  
