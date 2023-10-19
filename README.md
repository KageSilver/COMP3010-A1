# COMP 3010 Assignment 1 - Tara Boulanger (7922331)

## Compilation details:
The webserver does not require compilation.

To compile the scraper.c file type: `make compile`.

## Running details
For part 1, you can run the server and specified site by typing `make runSite1Single` or `make runSite1Multi` depending on if you want it to be multi- or single- threaded. Then you can simply replace the 1 by 2 or even by 3. Please note that the stretch goal wasn't actually finished.
Or, you could also type `python3 website.py 8680 site1 -m`. I was using ports 8680-8684 as they were assigned to me.

To run the scraper.c file, you simply have to type: `make run`.

### Other notes:
In the testingServer.py file, a few lines needed to be edited to change which site number it was testing and whether it would be writing to my single or multi .csv webserver. 