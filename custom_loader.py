path = " "

def load(path, info = True):
    
    import pandas as pd
    import io
    import numpy as np
    
    read = None

    if path.endswith(".csv"):
        read = pd.read_csv(path)
    elif path.endswith(".xlsx"):
        read = pd.read_excel(path)
    elif path.endswith(".txt"):
        read =  pd.read_csv(path, delimiter='\s+')
    elif path.endswith(".json"):
        read = pd.read_json(path)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv, .xlsx, .txt, or .json file.")
    
    
    if info:
        if len(read) > 0:
            print("# Data imported!")
            print("# ------------------------------------", "\n")
        
            print("# DIMENSIONS -------------------------")
            print("Rows:", read.shape[0], "\n" "Column:", read.shape[1], "\n")
    
            print("# DTYPES -----------------------------")
            if len(read.select_dtypes("object").columns) > 0:
                print("Object Variables:", "\n", "# of Variables:", 
                      len(read.select_dtypes("object").columns), "\n", 
                      read.select_dtypes("object").columns.tolist(), "\n")
    
            if len(read.select_dtypes("integer").columns) > 0:
                print("Integer Variables:", "\n", "# of Variables:", 
                      len(read.select_dtypes("integer").columns), "\n", 
                      read.select_dtypes("integer").columns.tolist(), "\n")
    
            if len(read.select_dtypes("float").columns) > 0:
                print("Float Variables:", "\n", "# of Variables:", 
                      len(read.select_dtypes("float").columns), "\n", 
                      read.select_dtypes("float").columns.tolist(), "\n")
    
            if len(read.select_dtypes("bool").columns) > 0:
                print("Bool Variables:", "\n", "# of Variables:", 
                      len(read.select_dtypes("bool").columns), "\n", 
                      read.select_dtypes("bool").columns.tolist(), "\n")
    
            print("# MISSING VALUE ---------------------")
            print("Checking for missing values... \n ", np.where(read.isnull().values.any() == False, 
                                                            "No missing values detected", "Data includes missing value!"), "\n")
            
            # Duplicate rows
            duplicate_count = read.duplicated().sum()

            if duplicate_count > 0:
                print("# DUPLICATE ROWS ---------------------")
                print(f"Number of duplicate rows: {duplicate_count}\n")
            else:
                print("# DUPLICATE ROWS ---------------------")
                print("No duplicate rows found.\n")
                
            print("# DATA TYPES OF EACH COLUMN ----------")
            print(read.dtypes, "\n")


            buf = io.StringIO()
            read.info(buf=buf)
            info = buf.getvalue().split('\n')[-2].split(":")[1].strip()
            print("# MEMORY USAGE ---------------------- \n", info)
          
        else:
            print("# Import Failed")


    return read
    
#ab = load(path, info = True)
#ab.head()