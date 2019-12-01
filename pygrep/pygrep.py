# file pygrep.py

from pathlib import Path
import re
import argparse

# features
# highlight match
# case in/sensitive option
# recursive option
# only display file names
# display line numbers
# ignore paths in file/.gitignore

def format_green(str):
    """
    Render a string in the color green in the terminal.
    """
    return "\033[92m{}\033[00m".format(str)
    
def match_format_green(matchobj):
    """
    Set the first matching result in a regex to green.
    """
    return format_green(matchobj.group(0))

def get_path(path, regex_str):
    """
    Provide a directory path whose contents you want to query.
    """
    regex = re.compile(regex_str, flags=re.IGNORECASE)

    if Path(path).exists() and Path(path).is_dir():
        dirs = [Path(path)]
        for dir in dirs:
            files = [f for f in dir.iterdir() if f.is_file()]
            for f in files:
                with f.open() as fstream:
                    for i, line in enumerate(fstream.readlines()):
                        line = line.rstrip('\n')
                        if regex.search(line):
                            relative_path = str(f)
                            highlighted_line = regex.sub(match_format_green, line)
                            print('{}:{}: {}'.format(relative_path, i+1, highlighted_line))
            
            dirs.extend([d for d in dir.iterdir() if d.is_dir()])

# __name__ is __main__ if it is the intial entry point
# otherwise it is the name of the module
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for PATTERN in each FILE or standard input.', add_help=True)
    parser.add_argument('query', type=str, nargs=2, help='the regexp query')
    # vars() returns __dict__
    args = vars(parser.parse_args())
    
    file_path =  args['query'][0]
    query = args['query'][1]
    get_path(file_path, query)
