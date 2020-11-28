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
    print("do something")
    #you are almost home when it begins to rain
    #its slippery and you fall
    #the person catches up to you
    #
    #   eyes glint mysteriously
elif answer_1 == "c":
    print("hello scary person chasing me")
else:
    print("I don't recognize that response.")