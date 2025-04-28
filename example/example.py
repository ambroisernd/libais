import argparse
import sys
import ais.stream
    
def main():
    # Get command line arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="AIS input file"
    )
    args = parser.parse_args()
    f_in = args.input_file  # Input file
    out=sys.stdout

    with open(f_in) as f:
    	for msg in ais.stream.decode(f):
    	    out.write(str(msg))
    	    out.write('\n')
    	    out.write('\n')
    	    


if __name__ == '__main__':
    main()
