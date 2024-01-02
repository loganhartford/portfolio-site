---
name: Hand Held Tic-Tac-Toe
tools: [Arduino, C++, SolidWorks]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704151028/portfolio-site/tic-tac-toe/ynk60hnefsxnzyidflem.jpg
description: A handheld PvP Tic-Tac-Toe console.
slug: tic-tac-toe-hardware
---

# Hand Held Tic-Tac-Toe Other
<p class="post-metadata text-muted">
  April 11th, 2021
</p>
***
The objective of this project was to create a physical version of the classic game, Tic Tac Toe. 

The project allows two players to play head to head in a game of tic tac toe. The on-board Arduino is the brains behind the game and automatically detects wins or ties and resets the game board.

{% include elements/video.html id="ZnFrRtN4N1A" %}

## Hardware Design
The game is co9ntrolled by an Arduino Nano and the game board is created using 9 RGB LEDs. Player one is by blue while player two is red. The cursor for selecting the next move is magenta.

To control the 18 diodes as well read the 6 buttons, the number of available outputs was increased using three 75HC595 shift registers. All of the diodes are controlled via the shift registers while the button’s statuses are read via the Arduino’s pins.  

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704151372/portfolio-site/tic-tac-toe/gwfbowpxcl0uigxuwcp0.jpg "Tic-Tac-Toe Hardware")

Each player has 3 control buttons, move left, move right and a select button. The device is powered using a rechargeable 9V battery which is mounted to the bottom game. 

## Code
The code was written without any reference to other projects as an exercise in writing more complex programs.

The game works by making use of 6 essential functions. The first function is the start function which is called at the start of each turn in order to reset the cursor. The next two functions are used to control the player cursor allowing the player to move left and right. 

```c++
// Player 1 is blue
  if (turn == 1) {
    start(turn);
    while (turn == 1) {
      // Reads all of the buttons to detect player input
      left1Read = digitalRead(left1);
      right1Read = digitalRead(right1);
      select1Read = digitalRead(select1);
      // Move left
      if (left1Read == 0) {
        delay(bdt);
        moveLeft(turn);
      }
      // Move right
      if (right1Read == 0) {
        delay(bdt);
        moveRight(turn);
      }
      // Make a selection
      if (select1Read == 0) {
        delay(bdt);
        select(turn);
        // Checks to see if selection resulted in a win condition
        if (winCheck(1)) {
          break;
        }
        // Checks to see if the game is a tie
        if (catsGameCheck()) {
         break; 
        }
      }
    }
  }
```

The fourth function is the select function which allows the player to make a selection. This function checks to see if the space on the board is taken, if available the move is made. 

The last two functions run at the end of each turn and check to see if the a player has won the game or if the game is a tie. Creating the win checker function was by far the most difficult part of the coding. The goal was to avoid using a brute force method to check for wins. This made the final  version of the win checker more succinct but also much more difficult to create.

{% include elements/button.html link="https://github.com/loganhartford/Project-Portfolio/blob/main/Multi-Disciplinary/TicTacToe/Firmware/Tic_Tac_Toe.ino" text="GitHub" style="primary" size="lg" %}

## Mechanical Design
The enclosure consists of three pieces, the base, the top and the game board.The protoboards snap into the base and then the top is glued on. The 9V battery slides into the cubby on the bottom of the base. The game board fits over the 9 LEDs creating the tic tac toe board and also serves to diffuse the LED’s light making the game state more clear.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704152385/portfolio-site/tic-tac-toe/i5ctfrzy1gqkdosyibaf.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704152385/portfolio-site/tic-tac-toe/ojxpfcez7olvphzfgwtj.jpg
{% endcapture %}
{% include elements/carousel.html %}

The game board was printed in 2 different plastics. The bottom 70% is printed in the opaque colour-change PLA while the  top 30% was printed in a more transparent white PLA. This prevents the colour from bleeding between game squares while also allowing the colour to show through the top of the game board clearly.

{% include elements/button.html link="https://grabcad.com/library/hand-held-tic-tac-tow-1" text="GrabCAD" style="primary" size="lg" %}

## Reflection
This project involved the most complicated circuitry and code of any of my projects to date.  This project was comfortably difficult and provided lots of opportunities for problem solving and learning.

If I were to do this project again I would definitely design a custom PCB. In order to fit all the necessary components on to ‘one’ board I had to hot glue 4 of my smaller proto-boards together. The wiring and soldering took an excessive amount of time to complete despite being a secondary focus for this project.

Lastly, I think adding auditory feedback to the game via a passive buzzer could really improve the UI of the game. I decided against adding one in as I was out of space on my board and it was not one of the features layed out in my planning phase of this project. Adding tones in response to button inputs is something that I already did in my Dopamine Box project so it would not have added an additional element of difficulty.

I really enjoyed completing this project. Creating a tic tac toe game is a common starting point for building programming portfolio and so integrating that with a physical interface was both challenging and very rewarding.