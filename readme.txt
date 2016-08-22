
Project: cleanjason
this project run in Python3.5

1.python file: "print_neat_json.py",
read the local jason file "messydata.json", parse the file by chunks , and save
the JSON objects in neat style into "neatdata.json".
    Input: messy JSON file,example

        {"one": "this is the first object"}{}{"two": "this is the second object", "empty_list": []}{"three": 3}

    Output: neat JSON file,example
        A good JSON stream is almost the same as an ugly JSON stream, with these differences:
            The objects are separated by line breaks.
            Line breaks may not appear within an object; they may only be used to separate objects.
            Neat JSON streams are much easier to decode than ugly ones.

    This is an example of an neat JSON stream

    {"one": "this is the first object"}
    {}
    {"two": "this is the second object", "empty_list": []}
    {"three": 3}


2.Test file: "test.py"
 A unitest file, it test the main function parse_by_chunk() in print_neat_json.py by
using a local file named "testdata.json"


