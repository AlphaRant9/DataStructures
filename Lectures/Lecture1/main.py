from random import randint

def main():
    outcomeCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outcomeChances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1000):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        outcome = die1 + die2
        outcomeCounts[outcome] += 1
        outcomeChances[outcome] += 1
    for i in range(len(outcomeCounts)):
        outcomeCounts[i] = outcomeCounts[i]/10
    for i in range(11):
        print(f'Outcomes resulting in {i+2}:',outcomeCounts[i+2])
    for i in range(11):
        print(f'Percent chance of resulting outcome {i+2}: {outcomeCounts[i+2]}%')

main()