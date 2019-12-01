# PROGRAMING_TASK

## web scraping programming using regular expression 
This program is a Python 3.6.3  Web scraping programming task, which scraps the a configured grouped list of urls based on the given 
regular expersion codes as an input_file and save the fetched content as a result_file.text form.

## Task_Requirement 
- Python programing language 
- Script must work on Linux
- Input file for lists of urls and regular expression codes in order to fetch data based on the given file
- The results of the check must be stored somehow for later analysis, at bare minimum must contain the time of check, response time and possible error if check was not successful
- The process must be able to run continuously doing the checks periodically. It must be able to deal with large number of urls without exploding, it must always respond to user input (ctrl-c for example in case of CLI script) within one second and clean up any resources gracefully on exit. 

## How to run the program 
In order to run this program you need to download the whole package of the folder (at least web1_scraper.py and input_file.yaml)
and onpen terminal/command prompt from the folder directory and run the down script
               
               python web1_scraper.py input_file.yaml 
               
once you run the above command the program will start running continuously and in order to stop the program 

               press CTRL - C 
Once the program stoped the results of the check/fetched content will be stored as Result_file for later analysis, which contain the time of check, response time and possible error if check was not successful

## Input_file.yaml sample 

      URLs:
        - https://www.hs.fi
        - https://www.cgi.fi/fi
        - https://www.freertos.org/
        - https://www.bbc.com/
      RegEx: 
        - <title>(.*?)</title>
        - (\w+@\w+\.{1}\w+)
        
## Result_file.text sample 
    #################################

    Date: 01-12-2019 Time: 01:25:41:606431_AM  | URL:  https://www.hs.fi  | Response Time:  0.87 s https://www.hs.fi  | Contents:  Uutiset | HS.fi
    Date: 01-12-2019 Time: 01:25:41:606431_AM  | URL:  https://www.hs.fi  | Response Time:  0.87 s https://www.hs.fi  | Contents:  online@hs.fi
    Date: 01-12-2019 Time: 01:25:41:606431_AM  | URL:  https://www.hs.fi  | Response Time:  0.87 s https://www.hs.fi  | Contents:  online@hs.fi
    Date: 01-12-2019 Time: 01:25:42:525863_AM  | URL:  https://www.cgi.fi/fi  | Response Time:  1.21 s https://www.cgi.fi/fi  | Contents:  IT- ja liiketoimintakonsultoinnin palvelut | CGI FI
    Date: 01-12-2019 Time: 01:25:42:525863_AM  | URL:  https://www.cgi.fi/fi | content not found with this regex:  (\w+@\w+\.{1}\w+)
    Date: 01-12-2019 Time: 01:25:43:752099_AM  | URL:  https://www.freertos.org/  | Response Time:  2.25 s https://www.freertos.org/  | Contents:  FreeRTOS - Market leading RTOS (Real Time Operating System) for embedded systems with Internet of Things extensions
    Date: 01-12-2019 Time: 01:25:43:752099_AM  | URL:  https://www.freertos.org/  | Response Time:  2.25 s https://www.freertos.org/  | Contents:  info@freertos.org
    Date: 01-12-2019 Time: 01:25:46:006994_AM  | URL:  https://www.bbc.com/  | Response Time:  2.43 s https://www.bbc.com/  | Contents:  BBC - Homepage
    Date: 01-12-2019 Time: 01:25:46:006994_AM  | URL:  https://www.bbc.com/ | content not found with this regex:  (\w+@\w+\.{1}\w+)

    #################################



