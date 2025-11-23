# ledger.py - This file handles reading and writing to the text file
# I am using basic file I/O operations here

def expense(all_expenses):
    # 'w' mode overwrites the file to keep it updated
    with open("my_expenses.txt", "w") as f:
        for item in all_expenses:
            # Format: "Amount|Category"
            # converting amount to string so we can write it
            line = str(item['amt']) + "|" + item['cat'] + "\n"
            f.write(line)

def history():
    data_list = []
    
    try:
        # 'r' mode is for reading
        with open("my_expenses.txt", "r") as f:
            lines = f.readlines()
            
            for line in lines:
                clean_line = line.strip()
                
                # safety check for empty lines
                if not clean_line:
                    continue
                
                parts = clean_line.split("|")
                
                # Rebuilding the dictionary
                # 'amt' is amount, 'cat' is category
                # IMPORTANT: We must save 'amt' as an integer for math later!
                entry = {'amt': int(parts[0]), 'cat': parts[1]}
                
                data_list.append(entry)
                
    except FileNotFoundError:
        # Return empty list if file doesn't exist (first run)
        return []

    return data_list
