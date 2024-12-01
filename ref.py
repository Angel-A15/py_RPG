# PRINT is used to display the desired message on the console
# Has to be in double or single quotation marks

# Will print on one line
print("hello world")
# Add a comma will print multiple strings by using a comma, they all go on one line,
# and display in the same print statement

# Adding a second print will have it break into the next line
print("you can", "print multiple", "strings with commas")

#DATA TYPES

# STRING is anything that is surrounded in quotation marks  str = "" str = ''
str = "hello world" 
str = 'is this okay?'

# STRING CONCATINATION is equivelent to using commas in 
# a string but youre using + signs instead; youre adding strings together
print("you can" + "print multiple" + "strings with commas") #You may need to add space in string if it looks weird in terminal

# COMMENT is anything that is a note left by developers that typically describes what their code does
#  starts with a pound sign in python; anything as a comment will be ignored by the script

# Assignment Operator
# it assigns some value to some variable
name = input("hey")

# Equivelance Operator
# Will define if things are equal to one another and they have to be identical
# play = should_we_play == 'yes'
# 1 == 2 will return False
# 1 == 1.0 will return False

# IF STAtement
# If some codition is met, this code will run
# if play


# ELIF statements
# Are only allowed to be added after the if statement and can be added multiple times
#Elif statement only runs when if statement is false; typically used when if answer is similar
# but not identical to the condition, so it runs a similar backup action

    # if should_we_play == "yes": the user has to input yes with no caps
    #     print("We are going to play!")

    # elif should_we_play == "YES":  since they typed something similar as YES being the case, we run the same action
    #     print("WE ARE GONNA PLAY!")
    # elif should_we_play == "Yes":  since they typed something similar as Yes being the case, we run the same action
    #     print("WE ARE GONNA PLAY!")

# .lower() .upper()
# Will convert whatever input to lowercase/upper letters; this simplifies our code by
# reducing the amount of times we would need to include elsif statements

    # ex should_we_play = input("Do you want to play?").lower()
    # if should_we_play == "yes":
    #     print("We are going to play!")


# CHAIN CONDITIONALS
# AND, OR, NOT: check if things are true.
# AND needs to have two or more conditions to be true, otherwise statement is False
# OR needs to have one or the other condition to be true, otherwise statement is False
# NOT reverses a condition
# not(should_we_play == "y" or should_we_play == "yes")

# if should_we_play == "y" or should_we_play == "yes":
#     print("We are going to play!!")
# else:
#     print("We are not going to play...goodbye!")



# COMBINING CONDITIONS
# Simplifying our codestructure and reducing space by merging two similar conditions and allow us to skip an 
# unneccesary step

    # play = should_we_play == "yes"

    # if play:
    #    print("We are going to play!")

     # if should_we_play == "yes":  # We can combine conditions like so to codense space
    #   print("We are going to play!")

# ELSE statements
# Can only be added once after the if or elsif statement, run after the if statement being false

    # if play:
        # print("hi")
    # elif should_we_play == "YES":
        #     print("WE ARE GONNA PLAY!") #Elif statement only runs when if statement is false
    # else:
    #     print("We aren't going to play...") 

# INTEGER is any whole number
int = "12"
int = '10000'

# FLOAT is any number containing a decimal
float = '12.0'
float = "100.33333"

# BOOLEAN is a true or false statement and determine is things are t or f
# They have to be in all caps to work
# bool = true wouldnt work
# bool = TRUE
# bool = FALSE


#INPUT statements allow the user to enter data; input always converts into a string
# Whatever goes inside the () are known as arguments; tell it what to do
# A string will generally go inside; inside the terminal, the user will be able to add input
input("Hello, enter your name:")

# VARIABLES store any kind of value; we can access them or change them
# They have to be upper/lower case letters and numbers; they cant be specail
# characters, ONLY underscore "_". You can not have a space included for a variable
# name
r = 23.3
x = 3
y = 'hello'
# z = TRUE comment out to prevent error
hey_you = 45
hyNmj = 67

# You can also classify your variable with a type, which kinda acts like
# function by allowing you to reference it 
name: str = input("Hey tyoe your name:") 
print(name)