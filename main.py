from datetime import datetime
import os

# global variables
# global variables related to datetime
current_date = datetime.now().strftime("%d-%m-%Y")
datetime_header = datetime.now().strftime("%H:%M - %d/%m/%Y")

# global variable related to paths and os
path = "~/Desktop/DO_Lists"
full_path = os.path.expanduser(path)
file_name = os.path.join(full_path, current_date + ".md")


# create a function to check for directory and file
# WARNING: This is not in use for now...
def create_check_dir():
    # exception handling
    try:
        # check if directory ( to keep markdown files ) exists
        if os.path.exists(full_path):
            # output appropriate message
            print(f"Directory {path} Has Been Created")
        # if the directory does not exist
        else:
            # make the folder / directory
            os.mkdir(full_path)

        # exception handling for creation of file
        try:
            # create the markdown file for today
            with open(file_name, 'x') as md_file:
                # just create the markdown file
                pass

        # if the directory has not been found
        except FileExistsError as e:
            print(f"\nError: {e}")
            print(f"File '{current_date + ".md"}' Already Exists\n")

    # if the file has not been found
    except OSError as e:
        print(f"\nError: {e}")
        print(f"Error has occured when creating / handling the directory at '{path}'")

# create a function to display options to user
def display_options():
    print(f"\nOption [1]: Insert Task(s) for Today ( {current_date} )")
    print("Option [2]: Remove Tasks")
    print("Option [3]: Display Uncompleted Tasks")
    print("Option [4]: Display Completed Tasks")
    print("Option [5]: Exit Program")


# create a function to check for header in the file
def check_header():
    # exception handling
    try:
        # open the file for read and check for header
        with open(file_name, 'r') as md_file:
            # make the contents for the file a list
            lines_in_file = md_file.readlines()

            # check for header
            return (len(lines_in_file) > 0) and (lines_in_file[0].startswith("#"))

    # if the file had not been found
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print(f"File '{current_date + ".md"}' has Not been Found at '{path}'\n")


# create a function to "create" and insert tasks to markdown file
def insert_task():
    # exception handling
    try:
        result_check = check_header()
        # create and open the file in append mode
        with open(file_name, 'a') as md_file:
            # check for the header in the file
            if result_check == False or result_check == None:
                md_file.write(f"# Tasks for {datetime_header}\n\n")

            # ask the user how many tasks to add
            task_amount_insert = int(input("\nPlease Enter Amount of Tasks To Add: "))

            print()

            # start entering tasks for that amount
            for amount in range(task_amount_insert):
                # prompt the user to start entering the tasks
                user_task = input(f"Please Enter Task {amount}: ")
                # start appending tasks to file
                md_file.write(f"- [ ] {user_task}\n")

    # if the user does not enter integer number for amount of task
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please Enter Integer Number Only for Amount of Tasks\n")

    # if the file has not been found
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print(f"File '{current_date + ".md"}' has Not been Found at '{path}'\n")


# create a function to check off tasks
def check_off():
    try:
        # open the file for read
        with open(file_name, 'r') as md_file:
            # place the contents of the file in a list
            lines_in_file = md_file.readlines()

        # call the function to display the uncompleted tasks
        tasks_uncompleted_remove()

        # prompt the user to enter numeber of tasks to remove
        task_amount_remove = int(input("\nPlease Enter Number of Tasks To Check Off: "))

        print()

        # start prompting the user to check off tasks in file
        for amount in range(task_amount_remove):
            # ask the user to enter index of tasks
            user_index = int(input("Please Enter Index of Task to be Removed: "))

            # validate what the user is removing
            if lines_in_file[user_index + 1].startswith("- [ ]"):
                # check off / remove the task
                lines_in_file[user_index + 1] = lines_in_file[user_index + 1].replace("- [ ]", "- [x]")

        # open the file for writing
        with open(file_name, 'w') as md_file:
            # place contents of updated list in file
            md_file.writelines(lines_in_file)

    # if the user does not enter integer data for index
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please Enter Integer Value for Index of Tasks\n")

    # if the file has not been found
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print(f"File '{current_date + ".md"}' has Not been Found at '{path}'\n")


# create a function to display uncompleted tasks
def tasks_uncompleted():
    # exception handling
    try:
        # open the file for read only
        with open(file_name, 'r') as md_file:
            # place the contents of lines into a list
            lines_in_file = md_file.readlines()

            # get the uncompleted tasks only
            for i in range(1, len(lines_in_file)):
                # check if tasks is not completed
                if lines_in_file[i].startswith("- [ ]"):
                    # output that line if not completed
                    print(lines_in_file[i].strip())

    # if the file has not been found
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print(f"File '{current_date + ".md"}' has Not been Found at '{path}'\n")


# create a function to display uncompleted tasks
def tasks_uncompleted_remove():
    # exception handling
    try:
        # open the file for read only
        with open(file_name, 'r') as md_file:
            # place the contents of lines into a list
            lines_in_file = md_file.readlines()

            # get the uncompleted tasks only
            for i in range(1, len(lines_in_file)):
                # check if tasks is not completed
                if lines_in_file[i].startswith("- [ ]"):
                    # output that line if not completed
                    print(f"Line Number: {i - 1} {lines_in_file[i].strip()}")

    # if the file has not been found
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print(f"File '{current_date + ".md"}' has Not been Found at '{path}'\n")


# create a function to display completed tasks
def tasks_completed():
    # exception handling
    try:
        # open the file for read only
        with open(file_name, 'r') as md_file:
            # place the contents of lines into a list
            lines_in_file = md_file.readlines()

            # get the uncompleted tasks only
            for i in range(1, len(lines_in_file)):
                # check if tasks is not completed
                if lines_in_file[i].startswith("- [x]"):
                    # output that line if not completed
                    print(lines_in_file[i].strip())

    # if the file has not been found
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print(f"File '{current_date + ".md"}' has Not been Found at '{path}'\n")


# create a function to take the user's choice
def choice(user_choice: str):
    # if the user want to create and insert tasks
    if user_choice == "1":
        # call function to create file + insert tasks
        insert_task()
    # if the user wants to check of tasks
    elif user_choice == "2":
        # call the function to check off tasks
        check_off()
    # if the user wants to display the uncompleted tasks
    elif user_choice == "3":
        print()
        # call the function to display uncompleted tasks
        tasks_uncompleted()
    # if the user wants to display the completed tasks
    elif user_choice == "4":
        print()
        # call the function to display completed tasks
        tasks_completed()
    # if the user wants to exit the "program"
    elif user_choice == "5":
        # exit the "program" and output appropriate message
        print("\nGood Bye!\n")
        exit(0)
    # if the user enters something other than '1' - '5'
    else:
        # output appropriate message
        print("\nYou Have Hit the Wrong Key; Try Again!!!\n")
        choice(user_choice)




# our main function
def main():
    # call the function to display the options to user
    display_options()

    # ask the user to enter a choice
    user_choice = input("\nPlease Select an option: ")

    # call the function to evaluate the choice
    choice(user_choice)

# run the main function
if __name__ == '__main__':
    main()
