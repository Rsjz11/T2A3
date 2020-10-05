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

The application is structured to have the menu page as the point of access for the user which can then access the other files that contain the features of the application. 

The terminal application is quite simple as to what it does. The majority of the application is sending json requests to the corresponding URL to access the necessary information. The information is then received as parse data, which the application must engage with and navigate to ascertain the sought after information. The application then restructures the information using the array structure to re-format it into a more easily digestable format for the user. 

The porfolio section of the application offers an additional component as it is linked to the porfolio.md file which determines what currencies are to be tracked within the portfolio feature. The porfolio like the other sections of the app continuously engages with the API as it must update the hourly, daily and weekly figures. 

As stated in the requirements.txt page, the following external packages are utilised:
colorama 0.4.3 to have the colour effect on the porfolio table
prettytable 0.7.3 to have the asset data from portfolio.md to be structured within a table

The Terminal Application uses the following standard libraries:
json: to handle the API response
unittest: for automatic testing/continuous integration

## Flowchart
![Flowchart](\docs\Flowchart.PNG)

## Installation and use
Terminal Application was written using Python3.8 which can be installed using:
```
apt-get install python 3.8
```

To install the required packages to run this app, use the command:
```
pip install -r requirements.txt
```

From the root of the repository the app can be run using:
```
python3.8 src/main.py
```



