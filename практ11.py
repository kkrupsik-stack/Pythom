import math

def time_to_travel_around_planet(robot_speed, planet_diameter):
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"

    circumference = math.pi * planet_diameter  
  
    time = circumference / robot_speed
    return time

def main():
    robot_name = "Igor_bot V.2.0"
    planet_name = "Земля"
    robot_speed = 10  #
    planet_diameter = 12742  
    
    calculation_1 = time_to_travel_around_planet(robot_speed, planet_diameter)
    if isinstance(calculation_1, float):
        print(f"Роботу {robot_name} необходимо {calculation_1:.2f} часов, чтобы объехать вокруг планеты {planet_name}.")
    else:
        print(calculation_1)
    
    print("\n" + "="*60 + "\n")
    

    calculation_2 = time_to_travel_around_planet(15, 1000)
    if isinstance(calculation_2, float):
        print(f"Роботу необходимо {calculation_2:.2f} часов.")
    else:
        print(calculation_2)
    
    print("\nПроверка обработки ошибок:")
    
    result = time_to_travel_around_planet(-5, 1000)
    print(f"Скорость -5 км/ч, диаметр 1000 км: {result}")

    result = time_to_travel_around_planet(10, 0)
    print(f"Скорость 10 км/ч, диаметр 0 км: {result}")

    result = time_to_travel_around_planet(0, -100)
    print(f"Скорость 0 км/ч, диаметр -100 км: {result}")

def time_to_travel_around_planet_exact(robot_speed, planet_diameter):
    """
    Версия с точным соответствием примеру (использует π = 3.14159)
    """
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"

    PI = 3.14159
    circumference = PI * planet_diameter
    time = circumference / robot_speed
    
    return time
def example_exact():
    print("\n" + "="*60)
    print("Пример с точным значением π = 3.14159:")
    
    robot_name = "Igor_bot V.2.0"
    planet_name = "Земля"
    robot_speed = 10
    planet_diameter = 12742
    
    calculation = time_to_travel_around_planet_exact(robot_speed, planet_diameter)
    print(f"Роботу {robot_name} необходимо {calculation:.2f} часов, чтобы объехать вокруг планеты {planet_name}.")


if __name__ == "__main__":
    main()
    example_exact()
