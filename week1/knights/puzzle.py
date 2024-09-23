from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A, B, C could either be a knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A is knight, then he is both knight and a knave.
    Implication(AKnight, And(AKnight, AKnave)),  # AKnight => AKnight AND AKnave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A, B, C could either be a knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A, B, C could either be a knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # Solution 1
    # In this case, if a is knave, then what a says is false, and b says is true.
    # if b is knave, then what b says is false, and a says is true.
    Implication(AKnave, BKnight),
    Implication(BKnave, AKnight)
    # Solution 2
    # Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B, C could either be a knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    # B is a knight means everything he said is true. Which means A indeed said B is a knave, and there are two possible cases
    # which is Or(Implication(AKnave, BKnight), Implication(AKnight, BKnave))
    # B also said C is a Knave, so everything B said encoded into And(Or(Implication(AKnave, BKnight), Implication(AKnight, BKnave)), CKnave)
    Implication(
        BKnight,
        And(Or(Implication(AKnave, BKnight), Implication(AKnight, BKnave)), CKnave),
    ),
    Implication(
        BKnave,
        Not(And(Or(Implication(AKnave, BKnave), Implication(AKnight, BKnave)), CKnave)),
    ),
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
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
    main()
