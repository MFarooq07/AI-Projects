from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# knowledge0 = And(Or(AKnight, AKnave),Or(BKnight, BKnave), Or(CKnight, CKnave))
A_said = And(AKnight, AKnave)
rules = And(Biconditional(Not(AKnight), AKnave), Biconditional(Not(BKnight), BKnave), Biconditional(Not(CKnight), CKnave))

knowledge0 = And(
    rules,
    Biconditional(AKnight, A_said)
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_said = And(AKnave, BKnave)
rules = And(Biconditional(Not(AKnight), AKnave), Biconditional(Not(BKnight), BKnave), Biconditional(Not(CKnight), CKnave))

knowledge1 = And(rules, Biconditional(AKnight, A_said))

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_said = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_said = Or(And(AKnight, BKnave), And(AKnave, BKnight))
rules = And(Biconditional(Not(AKnight), AKnave), Biconditional(Not(BKnight), BKnave), Biconditional(Not(CKnight), CKnave))

knowledge2 = And(rules, Biconditional(AKnight, A_said), Biconditional(BKnight, B_said))

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

rules = And(Biconditional(Not(AKnight), AKnave), Biconditional(Not(BKnight), BKnave), Biconditional(Not(CKnight), CKnave))
A_said = Or(AKnight, AKnave)
B_said = And(Implication(A_said, AKnave), CKnave)
C_said = AKnight
knowledge3 = And(rules, Biconditional(AKnight, A_said), Biconditional(BKnight, B_said), Biconditional(CKnight, C_said))



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    # print(BKnight.formula())
    # print("hello")
    main()
