import sqlite3

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
        ans : list = cursor.fetchall()

        cursor.execute(target_sql_lines)
        target : list = cursor.fetchall()

        if ans == target:
            print(f"{i}.sql is correct!:)")
        else:
            print(f"{i}.sql is incorrect!:(")
        

    connection.close()

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