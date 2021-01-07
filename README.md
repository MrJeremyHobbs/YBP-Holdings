# YBP Holdings
This script takes a .CSV file of ISBNS from Alma Analytics and turns it into a single column .TXT file of ISBNS to send to GOBI.
This will allow you to see if you already own an item before ordering it in GOBI.

# How it works
YBP Holdings uses the isbnlib python library to validate isbn's, this allows you to disregard any pseudo ISBNS or other identification numbers that may be in the ISBN field.
YBP Holdings also takes only the first valid ISBN from each row of ISBNS.
When it finds a valid ISBN, it attempts to convert it to ISBN-13, if it isn't already in that format.

# How to Use
-Click on YBPHoldings.exe
-Select a CSV file of ISBNS from Alma Analytics. This file must be a single column of data, ISBNS only.
-Wait a moment.
-When the process is done, a message will appear: "Done."
-A TXT file called YBP_HOLDINGS.txt" will appear in the same directory as the program.

# Downloading
You can download the latest version in the "Releases" tab above.

# Troubleshooting
If your anti-virus software won't allow you run this EXE, you can run the install python 3 and run the raw script instead.
This should allow you to bypass most anti-virus issues.

You will need the following modules:

isbnlib
easygui

You can do so by running the pip command:

`pip install isbnlib`

`pip install easygui`