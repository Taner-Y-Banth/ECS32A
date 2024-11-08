# dog.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# Dog walking instructions

condition = input("Enter weather condition (rainy/sunny/snowy/cloudy):")
instructions = "" # intializes variable

if condition == "rainy":
    
    instructions = "The dog should be taken for a short walk with an umbrella."
    
elif condition == "sunny":

    temperature = float(input("Enter temperature:"))
    
    if 80 < temperature <= 114:
        instructions = "The dog should be taken for a walk in the shade and given water."
    elif 45 < temperature <= 80:
        instructions = "The dog can enjoy a regular walk."
    elif -14 < temperature <= 45:
        instructions = "Dress the dog warmly for a walk."
    else:
        instructions = "Invalid weather condition."
        
elif condition == "snowy":
    instructions = "Take the dog for a short walk and ensure they stay warm."
elif condition == "cloudy":
    instructions = "Enjoy a regular walk with your dog."
else:
    instructions = "Invalid weather condition."

print("Instructions for the walk:")
print(instructions)