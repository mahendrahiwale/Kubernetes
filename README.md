# Test 1 

***Write a simple test script (using a tool of your choice) to verify the integration between the frontend and backend services***

Socket programming concept is used to test the backend and frontend service integration.

place the server.py file in the backend folder and build the respective docker file.

Place the client.py file in the frontend folder and build the respective docker file.

Run the server.py file.

Run the client.py file.

The responsed will be generated if the services are integrated succesfully.

# Test 2

***The test should check that the frontend correctly displays the message returned by the backend***

A simple and minimal selenium python script is added to test the greeting message fetched from the backend.
***Note :*** The script is made simple intentionally as to reduce the efforts of downloading n number of packages and softwares and setting them up.

Setup :
1) Install Python
2) Install Selenium
3) Download chrome driver
Setup the paths and keep the chrome driver in the project repo to avoid failures.

Once the setup is done deploy the application and pass the url to the testcase and run the testcase. If the greeting message fetched from the backend mismatched than the testcase will raise the error.

Script Name : frontend_webui.py
command to run : python frontend_webui.py or python3 frontend_webui.py
