# json_to_csv

A command line utility (developed for personal need initially) to convert a file containing json objects to CSV file using python3.

The scipt can take either 1 or more file names as command line arguments OR "all" argument to consider all .json or .text files in current directory. The files must contain valid json objects where each object contains the same keys.

The current version just goes to just 2 levels down from the top level.. 

Will make changes to consider any number of levels within json objects in next version.

Eg: 
{
"name" : "John",

"phone" : { "work": XXXXXX, "personal": YYYYYY },

"email" : "foo@bar.com"

}

will be processed by the program where the output CSV is ( with keys as column names in ascending order ) :


     email        name     phone_personal   phone_work
--------------------------------------------------------------------
  foo.bar@com &nbsp;&nbsp;&nbsp;&nbsp;        John &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;       YYYYYY &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              &nbsp;&nbsp; XXXXXX
