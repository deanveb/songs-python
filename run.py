import sqlite3
from sys import argv
from pandas import read_sql_query

def main():
    connection : sqlite3.Connection = sqlite3.connect("songs.db")
    for i in range(1, 9):
        try:
            with open(rf'ans(do not look)\{i}.sql', 'r') as file:
                sql_lines : str = decrypt(file.read())

            with open(fr'{i}.sql', 'r') as file:
                target_sql_lines = file.read()
        except FileNotFoundError:
            print("File not found")
            continue
        cursor : sqlite3.Cursor = connection.cursor()


        cursor.execute(sql_lines)
        
        headers : list = [header[0] for header in cursor.description]
        ans : list = cursor.fetchall()
        ans = sort_fetch(ans, headers)
        # print(ans)

        cursor.execute(target_sql_lines)
        target : list = cursor.fetchall()

        target = sort_fetch(target, headers)
        if ans == target:
            print(f"{i}.sql is correct!:)")
        else:
            print(f"{i}.sql is incorrect!:(")

        # arg[1] is enable compare, arg[2] is the exercise's name
        if len(argv) > 1:
            if (bool(argv[1]) == True and int(argv[2]) == i) or int(argv[2]) == 0:
                print("ans:")
                print(read_sql_query(sql_lines, connection))
                print()
                print("your ans:")
                print(read_sql_query(target_sql_lines, connection))
                # return

    connection.close()

def sort_fetch(table, header) -> list:
        # turn all tuples into list
        table = [list(result) for result in table]
        # turn all other types into str
        for row in range(len(table)):
            for column in range(len(table[row])):
                table[row][column] = str(table[row][column])
        # sort them in other
        for row in table:
            row.sort(key= lambda header : header)
        # print(table)
        return table

def decrypt(text : str) -> str:
    result : str = ""
    text.lower()
    for char in text:
        if char.isalpha():
            temp : chr = chr((ord(char) - 7 - 65) % 26 + 65) if char.isupper() else chr((ord(char) - 7 - 97) % 26 + 97)
            result += temp
        else:
            result += char
    return result

if __name__ == "__main__":
    main()