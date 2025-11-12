#reading the data dynamically
#in to csv file
import csv
while(True):
    try:
        no_columns = int(input("Enter how many columns you want : "))
        if no_columns <= 0:
            print("Please enter a positive number greater than 0.")
            continue
        break
    except ValueError:
        print("Don't use strings or special characters as input. Try again....")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully...")
        exit()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
#Read columns names for csv file
col_name = []
for i in range(1,no_columns+1):
    while(True):
        try:
            a = input(f"Enter the name of Column {i} : ").strip()
            if not a:
                print("Column name cannot be empty. Try again...")
                continue
            col_name.append(a)
            break
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully...")
            exit()
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
#print(col_name)

#Reading the records according colum name
while(True):
    try:
        NoRecordes = int(input("Enter how many records you need to enter : "))
        if NoRecordes <=0:
            print("Please enter a positive number greater than 0.")
            continue
        break
    except ValueError:
        print("Don't use strings or special characters as input. Try again....")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully...")
        exit()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

OutrList = []
for j in range(1,NoRecordes+1):
    innerList = []
    print("*"*50)
    print(f"Enter your {j} Record")
    print("*" * 50)
    for k in range(len(col_name)):
        while(True):
            try:
                record_input = input(f"Enter value for {col_name[k]} : ").strip()
                if not record_input or record_input.isspace():
                    print("Don't enter empty or only-space input. Try again.")
                    continue

                innerList.append(record_input)
                break
            except KeyboardInterrupt:
                print("\nProgram interrupted by user. Exiting gracefully...")
                exit()
            except Exception as e:
                print(f"Unexpected error occurred: {e}")

    OutrList.append(innerList)
    print("*" * 50)
while(True):
    fileName = input("Enter you File Name with extension .csv :")
    if not fileName.endswith(".csv"):
        print("Enter the .csv at the end of File name")
        continue
    else:
        try:
            with open(fileName, "a",newline="") as fp:
                writer = csv.writer(fp)
                # Write header only if file is empty
                if fp.tell() == 0:
                    writer.writerow(col_name)
                writer.writerows(OutrList)
                print("CSV File Created and Records Saved Dynamically-Verify")
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully...")
            exit()
        except Exception as e:
            print(f"Unexpected error while saving CSV: {e}")
            break