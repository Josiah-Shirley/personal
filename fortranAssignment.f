        program FortranAssignmentJosiahShirley

        implicit none

        character(len=32) :: inputPrompt
        character(len=3) :: endSentence
        integer :: userInput
        integer :: ones
        integer :: tens
        integer :: hundreds
        integer :: thousands
        integer :: finalNum

        inputPrompt = "What number did the ex give you?"
        endSentence = "Use"

        print *, inputPrompt
        read(*,*) userInput

        thousands = mod(userInput, 10)*1000
        userInput = userInput-(thousands/1000)
        hundreds = mod(userInput, 100)*100
        userInput = userInput-(hundreds/100)
        userInput = userInput-(mod(userInput, 1000))
        tens = mod(userInput, 10000)/100
        userInput = userInput-(tens*100)
        userInput = userInput-(mod(userInput, 100000))
        ones = mod(userInput, 1000000)/100000

        finalNum = thousands + hundreds + tens + ones

        print *, endSentence, finalNum

        end program FortranAssignmentJosiahShirley