import sys

if len(sys.argv) != 3:
    print("Usage: python BMI.py <weight_in_kg> <height_in_meters>")
else:
    weight = float(sys.argv[1])
    height = float(sys.argv[2])

    bmi = weight / (height ** 2)

    print(f"BMI: {bmi:.2f}")
