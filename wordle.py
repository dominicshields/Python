import random
from wordle_dict import init_word_list
from wordle_dict import init_target_list

def main():
    full_list = init_word_list()
    target_list = init_target_list()
    random.seed()
    upper = len(target_list)
    target = target_list[random.randrange(0, upper-1)]
    hangman = "_____"
    hanglist = list(hangman)
    notusedlist = []
    usedlist = []
    c = 0
    while c < 6:
        print(f"Try no {c+1}: Input a valid 5 letter word")
        guess = input().upper()
        err = False
        if guess not in full_list and guess not in target_list:
            print("Error, you must input a five letter word the game recognises")
            err = True
        else:
            if(guess == target):
                print(f"Try no {c+1}: Correct")
                break
            else:
                for i, (x, y) in enumerate(zip(guess, target)):
                    if x == y:
                        hanglist[i] = x
                        hangman = ''.join(hanglist)
                        print(f'Letter {x} is correct in position {i+1}')
                        usedlist.append(x)
                    else:
                        if x in target:
                            print(f'Letter {x} is in the word not position {i+1}')
                            usedlist.append(x)
                        else:
                            notusedlist.append(x)
        if not err:
            notusedlist = list(set(notusedlist))
            sortedlist = sorted(notusedlist)
            print(f"Letters not in word: {sortedlist}")
            usedlist = list(set(usedlist))
            sortedlist = sorted(usedlist)
            print(f"Letters in word: {sortedlist}")
            print(f'Hangman pattern : {hangman}')
            c+=1
    print("Target Word =",target)

if __name__ == "__main__":
    main()