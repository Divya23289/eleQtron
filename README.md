# eleQtron
Task_Assignment

**CustomerPreference.py**:
The purpose of the code is to generate Customer Preferences and saving a file as an input file in Text format which I have used as a input for main function.The script first randomly decides how many "hops" are considered. 
Where H = 3 → There are 3 island hops in total.
      num_customers = 5 → We are creating preferences for 5 people.
      filename = "input_250.txt" → The output will be saved in a file named input_250.txt.

After running the script, preferences are created, the script saves as text file format. The file starts with the total number of hops, then the number of customers, and finally one line for each customer's preferences.

In this script, I explored all possible transport combinations for the given 250 customer preferences. However, it seems there are certain constraints or limitations in the combinations that prevent a fully satisfying itinerary for all customers.

**Itenary.py**:
In this, script reads input_250.txt file containing travel preferences from several customers and finds the best possible travel itinerary for an island hopping journey. Each hop between islands can either be by airborne (air travel) or by-sea (boat/ferry).
The main goal of the script is to find a route that keeps every customer happy, while using the fewest possible airborne hops, since airborne travel may be more expensive or less desirable. and If there is no possible itinerary that satisfies all customers,it say "NO ITINERARY".


**Note**: while running the script, please take "CustomerPreference.py" file as a first script and make sure the input_250.txt file is generated in same python project folder, then run the "Itenary.py" Python file. It will analyze the input and print the best itinerary directly to the screen.
