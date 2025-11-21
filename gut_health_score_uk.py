# gut_health_score_uk.py
# Enhanced Gut Health Score Calculator with UK NDNS Data
# By Rachel E. (MSc Food Sciences, unibz) - Inspired by polyphenol-gut research

def get_uk_ndns_benchmarks():
    """Return UK averages from NDNS for context."""
    return {
        'fiber_g': 19,  # g/day (NDNS Years 9-11)
        'fermented_portions': 0.5,  # portions/week (estimated from low dairy/veg ferments)
        'polyphenols_mg': 800,  # mg/day (from tea/fruit sources)
        'processed_energy_pct': 54  # % of calories from ultra-processed (NDNS 2019-2023)
    }

def calculate_gut_score():
    print("=== UK Gut Health Quick Check (NDNS Data-Driven) ===\n")
    print("Based on National Diet and Nutrition Survey (NDNS) - UK Averages\n")
    
    score = 0
    tips = []
    uk_data = get_uk_ndns_benchmarks()
    
    # Q1: Fiber intake (NDNS avg: 19g/day, rec: 30g)
    fiber_input = input(f"How many grams of fiber do you eat daily? (UK avg: {uk_data['fiber_g']}g): ")
    try:
        fiber = float(fiber_input)
        if fiber >= 30:
            score += 25
            tips.append("Excellent! You're beating the UK average.")
        elif fiber >= 20:
            score += 15
            tips.append("Good start – aim higher than UK avg.")
        else:
            score += 5
            tips.append(f"UK avg is {uk_data['fiber_g']}g – try oats or beans for a boost!")
    except ValueError:
        score += 5
        tips.append(f"Assuming low – UK avg fiber: {uk_data['fiber_g']}g")
    
    # Q2: Fermented foods (NDNS: low, ~30% eat weekly)
    fermented = input("Do you eat fermented foods (yogurt, kimchi, kefir) 2+ times/week? (UK: ~30% do): (y/n): ")
    if fermented.lower() == 'y':
        score += 25
        tips.append("Fantastic! Most UK adults eat <1 portion/week.")
    else:
        score += 10
        tips.append("Add yogurt or sauerkraut – only 30% of UK hits this.")
    
    # Q3: Polyphenol-rich foods (NDNS proxy: 4.3 fruit/veg portions; avg ~800mg/day)
    poly = input("Do you eat berries, dark chocolate, or green tea daily? (UK avg polyphenols: 800mg): (y/n): ")
    if poly.lower() == 'y':
        score += 25
        tips.append("Gut superfood win! UK avg is low at 800mg/day.")
    else:
        score += 10
        tips.append("Try blueberries – UK fruit/veg avg: 4.3 portions/day (rec: 5+).")
    
    # Q4: Processed food limit (NDNS: 54% energy from ultra-processed)
    processed = input("Do you keep ultra-processed foods <20% of meals? (UK avg: 54% energy): (y/n): ")
    if processed.lower() == 'y':
        score += 25
        tips.append("Impressive – UK diets are 54% ultra-processed.")
    else:
        score += 10
        tips.append("Swap snacks for whole foods – NDNS shows high risk for gut health.")
    
    # Results
    print(f"\n=== Your Results ===")
    print(f"Gut Health Score: {score}/100")
    if score >= 80:
        print("🌟 Excellent! Your gut is thriving – better than most UK adults.")
    elif score >= 60:
        print("👍 Good foundation, but let's optimize.")
    else:
        print("📈 Opportunity to improve – common in UK diets per NDNS.")
    
    print("\n=== UK NDNS Comparison ===")
    print(f"- Fiber: UK avg {uk_data['fiber_g']}g/day (you: {fiber_input or 'N/A'}g)")
    print(f"- Fermented: UK ~0.5 portions/week (you: {'Yes' if fermented.lower()=='y' else 'No'})")
    print(f"- Polyphenols: UK avg 800mg/day (you: {'Yes' if poly.lower()=='y' else 'No'})")
    print(f"- Processed: UK 54% energy (you: {'Low' if processed.lower()=='y' else 'High'})")
    
    print("\n=== Personalized Tip (from NDNS Insights) ===")
    print(tips[0] if tips else "Focus on fiber-rich foods like lentils.")
    print("\nSource: UK NDNS Reports (2016-2023) – For more, visit gov.uk/ndns")

# Run the tool
if __name__ == "__main__":
    calculate_gut_score()