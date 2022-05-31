def response(hey_bob):
    bob_answer = None
    if hey_bob.isspace() == True or hey_bob == None or hey_bob == "":
        bob_answer = "Fine. Be that way!"
    elif hey_bob.isupper() == True and (hey_bob.strip())[-1] == "?":
        bob_answer = "Calm down, I know what I'm doing!"
    elif hey_bob.rstrip()[-1] == "?":
        bob_answer = "Sure."
    elif hey_bob.isupper() == True:
        bob_answer = "Whoa, chill out!"
    else:
        bob_answer = "Whatever."

    return bob_answer

