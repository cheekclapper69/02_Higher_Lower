# HL component 6 - Statement Gen


def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()
    return ""

# Main routine

too_low = hl_statement("^^ Too low, try a higher number.     |   "
                       "Guesses left 3 ^^", "^")
print()
too_high = hl_statement("vv Too high, try a lower number.     |    "
                        "Guesses left 2 vv", "v")
print()
duplicate = hl_statement("!! you already guesses that # Please try again.     |    ")

print()
well_done = hl_statement("*** well done! you got it in 3 guesses ***", "*")

print()
start__round = hl_statement("### round 1 of 3 ###", "#")
