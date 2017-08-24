import re

class Regex:

    def __init__(self , pattern):

        self.pattern = re.compile(pattern , re.MULTILINE)


    def get_matches_from(self , text):

        matches = self.pattern.findall(text)
        return matches


    def substitude_text(self , text , sub):

        return self.pattern.sub(sub, text )

def main():

    reg = "(\.\/)?.*\..*(png|jpg|ttf)$"


    text = " Hey !! my name is Musa.Nice to meet you all.Lets just talk and have some  fun.Cause i am bored."

    # gone match all the words !!

    regex = Regex(r'(\w+)')
    matches = regex.get_matches_from(text)

    print("All the match words..")
    for match in matches:print(match , end = " " )
    print('\n\n\n')



    print("Substitution..substitude all the numbers")

    print("Before substitution..")
    text2 = "12 Musa 34 Khan"
    print(text2)
    reg2 = Regex("\d")
    print("After substition")
    text2_sub = reg2.substitude_text(text2 , "-")
    print(text2_sub)

if __name__ == "__main__":
    main()





