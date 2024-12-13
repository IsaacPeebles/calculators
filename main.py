import math

# Area of a Polygon Calulator
# - Negative side length bug needs fixed
def calculate_triangle_area():
    try:
        base = float(input('Enter the length of the base: '))
        height = float(input('Enter the height: '))
        return .5 * base * height
    except base <= 0 or height <= 0:
        print('ERROR: Please enter an interger greater than 0.')
        return
    except ValueError:
        print('ERROR: Invalid input.')
        return

def calculate_quadrilateral_area():
    try:
        base = float(input('Enter the length of the base: '))
        height = float(input('Enter the height: '))
    except base <= 0 or height <= 0:
        print('ERROR: Please enter an interger greater than 0.')
    except ValueError:
        print('ERROR: Invalid input.')
    return base * height

def calculate_regular_polygon(sides):
    try:
        side_length = float(input(f'Enter the length of the sides for the {sides}-sided polygon: '))
    except side_length <= 0:
        print('ERROR: Please enter an interger greater than 0.')        
    except ValueError:
        print('ERROR: Invalid input.')        
    if sides == 5:
        # Pentagon
        print('WARNING: This calculator is intended for regular pentagons ONLY.')
        return .25 * math.sqrt(5 * (5+(2 * math.sqrt(5)))) * (side_length ** 2)
    if sides == 6:
        # Hexagon
        return ((3 * math.sqrt(3)) / 2 ) * (side_length ** 2)
    if sides == 8:
        # Octagon
        return 2 * (1 + math.sqrt(2)) * (side_length ** 2)
    
def poly_area_calc():
    shape = input('Choose a Shape: Triangle, Quadrilateral, Pentagon, Hexagon, or Octagon: ').lower()
    if shape == 'triangle':
        area = calculate_triangle_area()
    elif shape == 'quadrilateral':
        area = calculate_quadrilateral_area()
    elif shape in ['pentagon', 'hexagon', 'octagon',]:
        sides = {'pentagon': 5, 'hexagon': 6, 'octagon': 8}[shape] 
        area = calculate_regular_polygon(sides)
    else:
        print('Invalid Shape. Please choose a valid option.')
        return
    print(f'The area of the {shape} is: {area}')
                   
# Pythagorean Theorem Calculator
def pythagorean_theorem_calc():
    unknown = input('Which side is unknown: A, B, or C? ').lower()
    try:
        if unknown == 'a':
            b = float(input('Enter the length of side B of the triangle: ')) 
            c = float(input('Enter the length of side C of the triangle: '))
            a = math.sqrt(c ** 2 - b ** 2)
            print(f'{a}')
        elif unknown == 'b':
            a = float(input('Enter the length of side A of the triangle: ')) 
            c = float(input('Enter the length of side C of the triangle: '))
            b = math.sqrt(c ** 2 - a ** 2)
            print(f'{b}')
        elif unknown == 'c':       
            a = float(input('Enter the length of side A of the triangle: ')) 
            b = float(input('Enter the length of side B of the triangle: '))
            c = math.sqrt(a ** 2 + b ** 2)
            print(f'{c}')
        else:
            print('Invalid option. Please choose A, B, or C.')
    except ValueError:
        print('ERROR: Invalid input or sides do not form a triangle.')
        
# Function Calculator 
def quadratic_equation():
    print('WARNING: This calculator is intended for quadratic functions ONLY.\nA quadratic function is ax^2 + bx + c = 0')
    try:
        function_a = float(input('Enter \'a\': '))
        function_b = float(input('Enter \'b\': '))
        function_c = float(input('Enter \'c\': '))
        
        discriminant = (function_b ** 2) - (4 * function_a * function_c)
        
        if discriminant < 0:
            print('The equation has no real roots')
        elif discriminant == 0:
            root = -function_b / (2 * function_a)
            print(f'This equation has one real root: {root}')
        else:
            root1 = (-function_b + math.sqrt(discriminant)) / (2 ** function_a)
            root2 = (-function_b - math.sqrt(discriminant)) / (2 ** function_a)
            print(f'This equation has two real roots: {root1}, {root2}')
    except ValueError:
        print('ERROR: Invalid input for quadratic equation.')

def simple_invest_calc(principal, interest_rate, length_of_invest):
    interest = principal * interest_rate * length_of_invest
    print(f'You will earn {interest} dollars from a {length_of_invest} year simple interest investment with {interest_rate * 100}% interest rate.')
    
def compound_invest_calc(principal, interest_rate, length_of_invest):
    try:
        times_applied_per_year = float(input('How many times per year is interest applied: '))
        if times_applied_per_year <= 0:
            raise ValueError
    except ValueError:
        print('ERROR: Invalid Input.')  
    amount = principal * (1 + (interest_rate / times_applied_per_year)) ** (times_applied_per_year * length_of_invest)
    interest = amount - principal
    print(f'You will earn {interest} dollars from a {length_of_invest} year compounded interest investment with {interest_rate * 100}% interest rate.')
    
def invest_calculator():
    type_of_calc = input('This calculator can calculate both simple and compound interest.\nEnter 1 for simple and 2 for compond: ')
    
    try:
        principal = float(input('What is the principal amount: '))
        interest_rate = float(input('What is the interest rate (in percent): ')) / 100
        length_of_invest = float(input('What is the length of the investment in years: '))
    except ValueError:
        print('ERROR: Invalid Input.')
    if type_of_calc == '1':
        simple_invest_calc(principal, interest_rate, length_of_invest)
    if type_of_calc == '2':
        compound_invest_calc(principal, interest_rate, length_of_invest)
    else: 
        print('ERROR: This is not a valid input, please select either 1 or 2.')        

def main():
    while True:
        calculator = input('Choose a calculator: (1) Area of a Polygon Calculator, (2) Pythgorean Theorem Calculator, (3) Quadratic Equation Calculator, or (4) Investment Calculator: ').lower()   
        if calculator == '1' or calculator == 'area of a polygon calculator':
            poly_area_calc()
        elif  calculator == '2' or calculator == 'pythgorean theorem calculator':
            pythagorean_theorem_calc()
        elif calculator == '3' or calculator == 'quadratic equation calculator':
            quadratic_equation()
        elif calculator == '4' or calculator == 'investment calcualator':
            invest_calculator()
        else:
            print('ERROR: Invalid Choice, please enter the name of the calculator or corresponding number.')

if __name__ == '__main__':
    main()
