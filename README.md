# T2A3 - Cryptocurrency Information Platform
---
## Description

I have created a Terminal application that accesses information from an API called https://alternative.me/crypto/api. My terminal app is comprised of six files.
1. Main menu.
2. A menu conerning global cryptocurrency data like marketcap.
3. Comprehensive list of more than 3000 currencies.
4. A list that enables the user to receive comprehenisve informaton regarding the cryptocurrency of their choice. 
5. A list that enables the user to select a section according to rank with the result provided in a currency of the user's choice.
6. Creates a porfolio from a .md file that provides hourly, daily and weekly updates of the price of the user's selected currency. 
        
When the user accesses the app, they will enter the main menu. At this point the user will be able to choose from 6 options. By simply entering a number 1 to 6, then user will be sent to their area of choice. 
```
 [1] Enter 1 to retrieve global cryptocurrency information.
 [2] Enter 2 for an entire list of cryptocurrencies.
 [3] Enter 3 to retrieve specific cryptocurrency information.
 [4] Enter 4 to retrieve multiple cryptocurrencies in a list.
 [5] Enter 5 to retrieve porfolio information.
 [6] Press 6 to exit
```
This terminal application makes frequent requests to the alternative.me/crypto/api API. The information is updated every five minutes and therefore can be assumed to be reliable. 

The terminal application is quite simple as to what it does. The majority of the application is sending json requests to the corresponding URL to access the necessary information. The information is then received as parse data, which the application must engage with and navigate to ascertain the sought after information. The application then restructures the information using the array structure to re-format it into a more easily digestable format for the user. 

The porfolio section of the application offers an additional component as it is linked to the porfolio.md file which determines what currencies are to be tracked within the portfolio feature. The porfolio like the other sections of the app continuously engages with the API as it must update the hourly, daily and weekly figures. 

## Flowchart
![Flowchart](/docs/Flowchart.PNG)


The Solution Must:
- describe how input and output will be handled
-detail how the solution will be structured in terms of classes, functions and other entities
- illustrate how the algorithm will function
- list the Python dependencies required and state what each will be used for (this includes Python standard libraries as well as third-party packages)

It is strongly suggested that you have an educator review the draft of this question before you move on to any of the other requirements. If you solution does not cover the points above sufficiently or does not have sufficient detail or complexity, the mark awarded may be limited.

Note: “two way flow of communication” is very open-ended concept and requires you to present an algorithmic solution that can be implemented in Python. For example, a two-way chat application would have an algorithm that facilitates sending and receiving of messages between two users, a multiplayer game requires an algorithm to handle the way game state is tracked and communicated between clients, a file sharing application requires an algorithm to direct the handling of packets or chunks of files.




# Description
Welcome to an exciting new Cryptocurrency information platform! 
My platform uses the public API key from https://alternative.me/crypto/api/#terms 
For this API is public, it is not necessary to create an account. This API was created after coinmarketcap announced that they were ceasing their public API. 

From experience the API from https://alternative.me is easier to digest and navigate compared to the updated Coinmarketcap API documentation. 
