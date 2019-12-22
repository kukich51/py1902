import random

HANGMAN_PIGS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
 /|\  |
 / \  |
     ===''']

words = {'Животные':'животные:аист акула бабуин баран барсук бобр бык волк воробей выдра голубь гусь'.split(),
         'Фрукты':'яблко арбуз дыня клубника яжевика банан кокос ананас земляника малина шилковица'.split(),
         'Страны':'украина франция германия россия молдова беларусь испания греция польша швеция'.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    #print(wordKey)
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    #print(wordDict[wordKey][wordIndex])
    return wordDict[wordKey][wordIndex]


#print(getRandomWord(words))


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PIGS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву: ')
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print('Пожалуйста, введите одну букву')
        elif guess in alreadyGuessed:
            print('Вы уже вводили данную букву. Введите другой символ.')
        elif guess not in 'абвгдеёжзиклмнопрмстуфхцчшщъьыюя':
            print('пожалуйста, введите БУКВУ')
        else:
            return guess

def playAgain():
    print('Хотите сыграть еще? (да?\нет?)')
    return input().lower().startswith('да')

print('H A N G M A N')

difficulty = ''

while difficulty not in 'ЛСТ':
    print('выберите уровень сложности: Л-легкий С-средний Т-тяжёлый')
    difficulty = input().upper()

if difficulty == 'C':
    del HANGMAN_PIGS[8]
    del HANGMAN_PIGS[7]
if difficulty == 'Т':
    del HANGMAN_PIGS[8]
    del HANGMAN_PIGS[7]
    del HANGMAN_PIGS[5]
    del HANGMAN_PIGS[3]


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
secretSet = secretWord
gameIsDone = False

while True:
   #print('Секретное слово из набора : '+ secretSet)
   displayBoard(missedLetters, correctLetters, secretWord)
   guess = getGuess(missedLetters + correctLetters)
   if guess in secretWord:
       correctLetters = correctLetters + guess
       foundAllLetters = True
       for i in range(len(secretWord)):
           if secretWord[i] not in correctLetters:
               foundAllLetters = False
               break
       if foundAllLetters:
           print('Сукретное слово - "' +secretWord+'"! Вы угадали!')
           gameIsDone= True
   else:
      missedLetters = missedLetters + guess

      if len(missedLetters) == len(HANGMAN_PIGS)-1:
          displayBoard(missedLetters, correctLetters, secretWord)
          print('Вы исчерпали все попытки!\n было загадано слово:"'+secretWord+'".')
          gameIsDone = True

      if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            secretSet = getRandomWord(words)
            gameIsDone = False
        else:
            break