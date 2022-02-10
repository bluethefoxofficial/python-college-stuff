
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def quiz():
    cls()
    incorrect = 0
    correct = 0
    print("GCSE quiz for maths english and science")
    name = input("Enter your name: ")
    print("welcome "+name+"to the GCSE quiz")
    print("please answer the following questions note these are case sensitive")
    
    print("1. what is the chemical formula for Water? ")
    print("a) H2O")
    print("b) H4SO4")
    print("c) SHO4")
    
    
    
    awnserone = input("answer: ")
    
    if(awnserone == "a"):
        print("correct")
        correct+=1
    else:
        print("incorrect")
        incorrect+=1
        
        
        
        
        
    print("2. what is the term called for adding human emotions to weather in writing? ")
    print("a)anthropermorthism")
    print("b)personification")
    print("c)metaphor")
    print("d)metaphorism")
    
    awnsertwo = input("answer: ")
    
    if(awnsertwo == "b"):
        print("correct")
        correct +=1
        
    else:
        print("incorrect")
        incorrect +=1
        
        
    print("3. what is the awnser to (3x7) x 23? ")
        
    print("a)254")
    print("b)123")
    print("c)24")
    print("d)483")
    
    awnserthree = input("answer: ") 
    
    if(awnserthree == "d"):
        print("correct")
        correct +=1
        
    else:
        print("incorrect")       
        incorrect +=1
        
        
        
    print("4. what is the awnser to the force that keeps us down on the ground? ")
    
    print("a) gravity")
    print("b) physics")
    print("c) collision")
    print("d) 42")
    
    awnserfour = input("answer: ")
    
    if(awnserfour == "a"):
        print("correct!")
        correct += 1
    else:
        print("incorrect!")
        incorrect += 1
        
        
        
        
    print("5. what is 25% of 120? ")
    
    print("a)25")
    print("b)30")
    print("c)50")
    print("d)100")
    print("e)0")
    
    final = input("answer: ")
    
    if(final == "b"):
        
        print("correct!")
        correct += 1
    else:
        print("incorrect!")
        incorrect += 1
        
        
    
    
            
    
        
    
    
    input("---PRESS ANY KEY TO GET RESULTS---")
    cls()
    
    print("Correct: "+str(correct))
    print("incorrect: "+str(incorrect))
    print("total of questions: "+str(correct+incorrect))
    
    total = correct+incorrect
    
    
    percentage = correct / total * 100
    print(str(percentage)+"%")
    
quiz()