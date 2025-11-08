def quick_steel_argon_cp(temperature, argon_pressure=1.0):
    """
    Быстрый расчет удельной теплоемкости стали в аргоновой атмосфере
    
    Args:
        temperature: температура в °C
        argon_pressure: давление аргона в атм (по умолчанию 1.0)
    
    Returns:
        effective_cp: эффективная удельная теплоемкость (Дж/кг·К)
    """
    
    if temperature <= 20:
        steel_cp = 450
    elif temperature <= 500:
        steel_cp = 450 + 0.3 * (temperature - 20)
    else:
        steel_cp = 600 + 0.2 * (temperature - 500)
    

    argon_contribution = 0.5 * (argon_pressure - 1)
    
    effective_cp = steel_cp + argon_contribution
    
    return effective_cp

if __name__ == "__main__":
    temp = 300
    pressure = 2
    
    cp = quick_steel_argon_cp(temp, pressure)
    print(f"Температура: {temp}°C")
    print(f"Давление аргона: {pressure} атм")
    print(f"Эффективная удельная теплоемкость: {cp:.1f} Дж/кг·К") 
