def chickens_and_rabbits(cnthead, cntleg):
    for chickens in range(cnthead+1):
        rabbits = 35 - chickens
        if 2 * chickens + 4 * rabbits == cntleg:
            return f"chickens: {chickens}, rabbits: {rabbits}."
        
print(chickens_and_rabbits(35, 94))