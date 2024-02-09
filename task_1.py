def main():
    from pulp import LpProblem, LpMaximize, LpVariable

    model = LpProblem("Maximize_Production", LpMaximize)

    x1 = LpVariable("Lemonade_units", lowBound=0, cat="Integer")
    x2 = LpVariable("Fruit_Juice_units", lowBound=0, cat="Integer")

    model += x1 + x2, "Total_Production"

    model += 2 * x1 + x2 <= 100, "Water_constraint"
    model += x1 <= 50, "Sugar_constraint"
    model += x1 <= 30, "Lemon_Juice_constraint"
    model += 2 * x2 <= 40, "Fruit_Puree_constraint"

    model.solve()

    print(f"Optimal production of Lemonade: {int(x1.value())} units")
    print(f"Optimal production of Fruit Juice: {int(x2.value())} units")
    print(f"Total production: {int(x1.value()) + int(x2.value())} units")

if __name__ == "__main__":
    main()