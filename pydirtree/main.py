from pathlib import Path
import argparse

# glob https://docs.python.org/3.8/library/glob.html

def path_is_hidden(path):
    """
    Return False if a part of a path begins with '.'. This excludes '..'.
    Originally glob.glob('*') excluded hidden files, but this is not 
    implemented in Path().glob nor Path().rglob().
    """
    for p in path.parts:
        if p != '..' and p[0] == '.':
            return True
    return False
    

def print_dir_tree(dir_path):
    """
    Print out the directory tree of a directory path excluding hidden files
    and directories.
    """
    top_path = Path(dir_path)
    if Path(top_path).exists() and Path(top_path).is_dir():
        print(f'+ {top_path}')
        paths = [p for p in sorted(top_path.rglob('*')) if not path_is_hidden(p)]
        for path in paths:
            depth = len(path.relative_to(top_path).parts)
            spacer = '  ' * depth
            print(f'{spacer}+ {path.name}')

    else:
        print("The path {} is not a directory.".format(dir_path))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print the directory tree for a given path.', add_help=True)
    parser.add_argument('dir', type=str, nargs=1, help='the path you want to query')
    args = vars(parser.parse_args())
    dir_path = args['dir'][0]
    print_dir_tree(dir_path)
