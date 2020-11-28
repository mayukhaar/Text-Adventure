print("It’s dark earlier than you expected. You’re walking home, and \nare nearly there until, suddenly, you hear footsteps behind you.")
print("You glance back, but you see no one there. The footsteps draw closer. \nWhat do you do?")
walk = "a) Walk away quickly. \n"
run = "b) Start running home. \n"
still = "c) Stay still and wait for whoever it is to catch up to you. \n"
print("You have three options. \n" + str(walk) + str(run) + str(still))
answer_1 = input("What do you do?: ")
if answer_1 == "a":
    print("The footsteps quicken with yours. Your walk turns to jogging, ")
    print("which quickly becomes running as fast as you possibly can. You")
    print("see a dark alley nearby and duck in to escape. ")

    #nearby alley
    #duck in to escape
    #fall down a hole
    #see a circus performing in front of you


elif answer_1 == "b":
    print("You are almost home when it begins to rain. The road becomes")
    print("slippery, and you fall. The person chasing you catches up to")
    print("you. You are expecting it to be someone ominous, but you are")
    print("relieved to see that it is one of your friends. Strangely though")
    print("they're eyes seem to glow bright red in the darkness.")
    #add another option somewhere around her talking about the
    # slippery road and what you do then
    ignore = "a) Ignore it and start walking home again, this time with them. \n"
    glow = "b) Ask them why their eyes glowed. \n"
    ask = "c) Ignore their eye color and ask why they were following you. \n"
    print("You have three options: " + str(ignore) + str(glow) + str(ask))
    answer_2 = input("What do you do?: ")
    if answer_2 == "a":
        print("You reach home safely, but your friend's eyes glint strangely")
        print("again the second you reach the door. You regret not asking")
        print("them why they were following you. ")
    elif answer_2 == "b":
        print("")
    elif answer_2 == "c":
        print("something ")
    else:
        print("I don't recognize this response.")
    #you are almost home when it begins to rain
    #its slippery and you fall
    #the person catches up to you
    #   eyes glint mysteriously
    #       ignore it and start walking home again
    #       "Did your eyes just glow?" make them confess and tell you why
    #       "Why were you following me?"
elif answer_1 == "c":
    print("hello scary person chasing me")

else:
    print("I don't recognize that response.")