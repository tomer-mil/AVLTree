import inspect
import ast
import importlib.util


def extract_function_definitions(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    function_definitions = []
    lines = source_code.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith("def"):
            function_definitions.append(line[4:])
        if line.startswith("Complexity:"):
            function_definitions.append(line)
            function_definitions.append("")

    return function_definitions



file_path2 = '/Users/tomermildworth/Documents/University/Year_3/Semester_b/Data Structures/AVLTree/AVLTree.py'
functions = extract_function_definitions(file_path2)

output_file = '/Users/tomermildworth/Documents/University/Year_3/Semester_b/Data Structures/AVLTree/functions.txt'

with open(output_file, 'w') as file:
    for function in functions:
        file.write(function + '\n')
