print("================================")
print("    EARTHING RESISTANCE CALCULATOR")
print("================================")

resistivity = float(input("Enter soil resistivity (Ω·m): "))
length = float(input("Enter electrode length (m): "))
area = float(input("Enter electrode cross-sectional area (m²): "))

if resistivity <= 0 or length <= 0 or area <= 0:
    print("\nPlease enter positive values.")
else:
    resistance = (resistivity * length) / area

    print("\n------------- RESULTS -------------")
    print(f"Soil Resistivity    : {resistivity:.2f} Ω·m")
    print(f"Electrode Length    : {length:.2f} m")
    print(f"Electrode Area      : {area:.6f} m²")
    print(f"Earthing Resistance : {resistance:.2f} Ω")
    print("-----------------------------------")
