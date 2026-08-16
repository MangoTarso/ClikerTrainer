import random as rd

phrases = [
    " HOW CLOSE YOU ARE",
    " KEEPING THE EDGE",
    " THAT TINGLING SENSATION ALL OVER",
    " HOW BAD YOU WANT TO CUM",
    " HOW YOUR SEX FEELS",
    " GOONING GOONING GOONING",
    " FALLING DEEPER",
    " PUMPING",
    " PUMP PUMP PUMP",
    " HOW GOOD PORN FEELS",
    " HOW GOOD YOU FEEL",
    " DROOLING DUMB",
    " GETTING WORSE",
    " EDGING",
    " LEAKING",
    " LETTING YOUR JUICES FLOW",
    " GETTING LOUDER",
    " BREATHING IN, HOLDING IT, THEN BREATHING OUT",
    " THE SOUNDS YOU'RE MAKING",
    " NOT THINKING",
    " YOUR BRAIN GOING DUMBER",
    " YOU BECOMING PORN",
    " PORN",
    " THAT TINGLING",
    " THE MOANS",
    " GOONING",
    " THE PLEASURE",
    " YOUR ADDICTION",
    " YOUR TRIGGERS"
    ]

actions = [
    "CLENCH",
    "PUMP",
    "LEAK",
    "BUCKLE YOUR HIPS",
    "KEEP THE RHYTHM",
    "GO FASTER",
    "SLOW DOWN NICELY",
    "RUB GENTLY",
    "FUCK YOUR HAND"
    ]

predicate = [
    "FOCUS ON",
    "THINK ABOUT",
    "LET YOUR MIND WANDER ON",
    "FOCUS ONLY ON",
    "THINK ABOUT ONLY",
    "LET YOUR MIND WANDER ONLY ON"
]

say = "\tSAY \"I'M A GOOD GOONER\""

def PhrasePicker(chance):
    ra = rd.random()

    phrase = f"\t{rd.choice(actions)} AND {rd.choice(predicate)}{rd.choice(phrases)}"

    if chance >= 0.75:
        return rd.choices([phrase, say], weights=[4,1], k=1)[0]

    return phrase

if __name__ == "__main__":
    s = 0
    while s < 1:
        print(PhrasePicker(s))
        s += rd.random()
    input()