#######################
# Calvin Grant
# Program 2
# CFG
# 3/13/24
#######################
# Import statement 
import random

# class for CFG creation
class CFG:
    # to set the constructor 
    def __init__(self, prints, rules):
        self.prints = prints
        self.rules = rules
    
    # beginning the creation of the CFG
    # kinda think about it as the "push" in the PDA from the starting to ending state where all the rules are contained
    def generate(self):
        # extracting the starting symbol 'S' 
        start_symbol = list(self.rules.keys())[0]
        # relaying that to the actual function that decides what accepted string to produce 
        return self._generate(start_symbol)

    # printing and actually running through the rules 
    def _generate(self, symbol):
        # just saying if the symbol that the CFG is currently dealing with is present in the printable characters
        # that are in the specific part of a rule of the CFG return that symbol to be printed and continue 
        if symbol in self.prints:
            return symbol
        
        # randomly chose a rule
        # because all options of the CFG should be able to lead to an accepting state 
        rule = random.choice(self.rules[symbol])
        # recursive call of this function to do the same until reached end (reaches the end of the printable states) 
        return "".join([self._generate(s) for s in rule])


########
# MAIN #
########

# defining what values are "allowed" to be printed and the rules associated with each CFG
prints = ['a', 'b']
# Rules
# hope it is fine that I used my own variation of rules
# I did not know if you wanted the rules to come from user input 
npalindrome_rules = {'S': ['aSa', 'aSb', 'bSb', 'aSb', 'bSa', 'ab'],}
AnBn_rules = {'S' : ['aSb','ab'],}

# defining two separate CFG 'presentations' to show accepted strings by the two sets of rules
# described above
cfg = CFG(prints, npalindrome_rules)
cfg1 = CFG(prints, AnBn_rules)

# just formatting stuff (OCD)
Ocount = 2
count = 0

print("|CFG non-palindrome|\n")
print("---------------------------------\n")
#  strings from the CFG non-palindromes
for i in range(10):
    print(cfg.generate(), end= " ")
    count += 1
    if count == Ocount:
        print()
        count = 0
        
print("\n\n |CFG AnBn|\n")
print("---------------------------------\n")
# strings from the CFG A^nB^n
for i in range(10):
    print(cfg1.generate(), end= " ")
    count += 1
    if count == Ocount:
        print()
        count = 0