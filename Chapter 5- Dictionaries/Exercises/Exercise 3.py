glossary = {
    'comment': 'A note that you can put in a code that will bypass the interpreter.',
    'list': 'A number of items in brackets.',
    'string': 'A function that allows user to put words and sentences.',
    'dictionary': 'A list of key:value pairs.',
    'variables': 'Variables are letters or words that let us store value in them.',
    'int': 'A function that makes the output an integer',
    'float': 'A function that produces a decimal output',
    'value': 'A value are things thtat are assigned on certain variables.',
    'pop': 'A function that lets you remove a value from a list',
    'insert': 'A fuction that lets you insert a value in a list',

}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)