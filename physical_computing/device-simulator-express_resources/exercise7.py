from adafruit_clue import clue
from random import *
from time import *

clue_data = clue.simple_text_display( text_scale=2, title= "REACTION GAME")


while True:
    
    clue_data[0].text = "Instructions:"
    clue_data[0].color = clue.GREEN
    clue_data[1].text = "Player A presses A"
    clue_data[1].color = clue.WHITE
    clue_data[2].text = "Player B presses B"
    clue_data[2].color = clue.WHITE
    clue_data[3].text = "Press if the number"
    clue_data[3].color = clue.SKY
    clue_data[4].text = " is divisible by 2"
    clue_data[4].color = clue.SKY
    clue_data[5].text = "Maximum score of 5"
    clue_data[5].color = clue.YELLOW
    
    for i in range (3, 0, -1):
        clue_data[6].text = "Starts in " + str(i)
        clue_data[6] .color = clue.RED
        sleep(1)

        scoreA = 0;
        scoreB = 0
        if i == 1:
            while True:
                num =  randint(1, 100)
                clue_data[0].text = ""
                clue_data[1].text = ""
                clue_data[2].text = ""
                clue_data[3].text = ""
                clue_data[4].text = ""
                clue_data[5].text = "Player A Score: " + str(scoreA)
                clue_data[5].color = clue.GREEN
                clue_data[6].text = "Player B Score: " + str(scoreB)
                clue_data[2].text = "        " + str(num)

                time1 = time()
                time2 = time()
                ctr = 1

                while ctr > 0:
                    if time2 - time1 >= 1:
                        ctr = 0
                    else:
                        time2 = time()
                    
                    if clue.button_a:
                        print("Button A clicked!")
                        if num % 2 == 0:
                            scoreA +=1
                        else: 
                            if scoreA < 1:
                                scoreA = 0
                            else:
                                scoreA -=1
                        break

                    if clue.button_b:
                        if num % 2 == 0:
                            scoreB +=1
                        else:
                            if scoreB < 1:
                                scoreB = 0
                            else:
                                scoreB -=1
                        break
                

                if scoreA == 5:
                    clue_data[5].text = "Player A Score: 5"
                    clue_data[0].text = ""
                    clue_data[0].text = "PLAYER A WINS!"
                    clue_data[0].color = clue.RED
                    sleep(1)
                    break
                        
                if scoreB == 5:
                    clue_data[5].text = "Player B Score: 5"
                    clue_data[0].text = ""
                    clue_data[0].text = "PLAYER B WINS!"
                    clue_data[0].color = clue.RED
                    sleep(1)
                    break
       
        clue_data.show()
