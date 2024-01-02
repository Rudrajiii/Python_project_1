import sys
import subprocess
from typing import List,Dict
import time 

# arg: List[str] = sys.argv
# print(arg)

def main() -> None:
        """Entrypoint of program run as code"""
        args: Dict[str, str] = read_args()
        # print(args)
        results: List[str] = search_file(args["file_path"], args["keyword"])
        # print(results)
        show_results(args["file_path"],args["keyword"],results)
        # print(len(results))
        
def read_args() -> Dict[str, str]:
        """check for a valid CLI argument and return them in a dictionary"""
        if len(sys.argv) != 3:
            print(f"ERROR : PROJECTS--/rptd_wrd_cli.py [file] [keyword] needed to be proceed further") 
            sys.exit()
        return {
            "file_path": sys.argv[1],
            "keyword": sys.argv[2]
        }
def search_file(file_path:str,keyword:str) -> List[str]:
        """Open and Reads file_path & return a list of lines & keywords"""
        matches: List[str] = []
        line_x: List[str] = []
        file_handle = open(file_path, 'r', encoding='utf-8')
        for line in file_handle:
            if keyword in line:
                matches.append(keyword)
        file_handle.close()

        # print(targets)
        return matches
def get_lines(file_path:str,keyword:str):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()
                lines = [value for value in content if keyword in value]
                for line in lines:
                    print(line.strip())
def show_results(file_path:str,keyword:str,matches:List[str]) -> None:
        """Prints the matching lines and total number of matches"""
        get_lines(file_path,keyword)
        print(f'Total no of matches --> {len(matches)}')
        print('\n')
        print("Also the Line Numbers are:")
        print("Loading data....")
        time.sleep(4)
        print('\n')
        with open("output.txt", "w") as f:
            save=subprocess.run(['type', 'data_of_ipl.txt'],
                            capture_output=True,
                            text=True, shell=True)
        
        # f.write(save.stdout)
        
            expose=subprocess.run(['findstr', '/n', 'Virat'],
                            capture_output=True,
                            text=True, shell=True,
                            input=save.stdout)
        
            f.write(expose.stdout)
        print(expose.stdout)
            
if __name__ == "__main__":
        main()




