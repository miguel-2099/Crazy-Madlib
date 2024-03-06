import random


def madlib():
    stories = [

        "📜 Once upon a time, a {adjective1} {noun1} decided to {verb1} to {place1}. \nAlong the way, they met a {adjective2} {noun2} who offered them a {noun3}. \nTogether 🙏, they {verb2} to the {place2} and lived {adverb1} ever after 🤗.",
        
        "In a {adjective1} kingdom 🏰, there lived a {noun1} who could {verb1} with \n{adjective2} {noun2}. One day 🌼, they stumbled upon a {adjective3} {noun3} and \ndecided to {verb2} it. Little did they know, it would lead them on an \n{adjective4} adventure filled with {noun4} and {noun5} 😮.",
        
        "Deep in the {adjective1} forest🌲🌳, there was a {adjective2} {noun1} who \n{verb1} all day long. One {noun2}, they discovered a {adjective3} {noun3} hidden 🫥 \nbehind a {noun4}. Inside, they found a {noun5} that granted them {adjective4} powers 💪. \nWith their newfound abilities, they {verb2} to {place1} and became {adverb1} famous 🤩😍."



    ]
    

    story = random.choice(stories)
    


    adjective1 = input("Enter an adjective 🤔: ")

    adjective2 = input("Enter another adjective 🤔: ")

    adjective3 = input("Enter one more adjective 🤔: ")

    adjective4 = input("Enter the last adjective 🤔: ")

    

    noun1 = input("Enter a noun 🤔: ")

    noun2 = input("Enter another noun 🤔: ")

    noun3 = input("Enter one more noun 🤔: ")

    noun4 = input("Enter yet another noun 🤔: ")

    noun5 = input("Enter the last noun 🤔: ")
    
    verb1 = input("Enter a verb 🤔: ")

    verb2 = input("Enter another verb 🤔: ")
    
    place1 = input("Enter a place🤔: ")

    place2 = input("Enter another place 🤔: ")
    
    adverb1 = input("Enter an adverb 🤔: ")
    


    madlib_story = story.format(adjective1=adjective1, adjective2=adjective2, adjective3=adjective3,
                                 
                                 adjective4=adjective4, noun1=noun1, noun2=noun2, noun3=noun3,
                                 
                                 noun4=noun4, noun5=noun5, verb1=verb1, verb2=verb2, place1=place1,
                                 
                                 place2=place2, adverb1=adverb1)
    


    print("\nYour crazy🤪 Madlib story is:\n")

    print(madlib_story)


if __name__ == "__main__":
    madlib()