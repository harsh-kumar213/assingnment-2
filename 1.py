def reverse_file_content(input_file_path):

    try:

      

        with open(input_file_path, 'r') as file:

            content = file.read()



        reversed_content = content[::-1]

      

        with open(input_file_path, 'w') as file:

            file.write(reversed_content)



        print(f"Content of '{input_file_path}' has been successfully reversed and updated in the file.")

    except FileNotFoundError:

        print(f"Error: File '{input_file_path}' not found.")

    except Exception as e:

        print(f"Error: {e}")



input_file_path = 'file1.txt'

reverse_file_content(input_file_path)
