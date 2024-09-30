import random

def Slagsmålsspel(fighter_A, fighter_B, hp_A, hp_B):

    while hp_A > 0 and hp_B > 0:
        input("Tryck på Enter för att fortsätta till nästa runda...")

        damage_to_B = random.randint(1, 20)
        damage_to_A = random.randint(1, 20)
        
        hp_B -= damage_to_B
        hp_A -= damage_to_A
        
        print(f"{fighter_A} slår {fighter_B} och gör {damage_to_B} skada. {fighter_B} har {max(hp_B, 0)} hp kvar.")
        print(f"{fighter_B} slår {fighter_A} och gör {damage_to_A} skada. {fighter_A} har {max(hp_A, 0)} hp kvar.")
        print('-' * 40)
        
    if hp_A <= 0 and hp_B <= 0:
        print("Båda slagskämparna föll samtidigt. Det blev oavgjort!")
    elif hp_A <= 0:
        print(f"{fighter_B} vann striden!")
    else:
        print(f"{fighter_A} vann striden!")

Slagsmålsspel("Slagskämpe A", "Slagskämpe B", 100, 100)