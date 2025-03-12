import time  #✅
import queue

import ttkbootstrap as tb
import customtkinter
import threading  #✅
from datetime import datetime
from tkinter import messagebox



from Check_driver import Check_and_install_Updated_driver
from Chek_unfinshed_push import check_last_push_file, check_last_push_file_epin
from Delete_file_when_done import delete, delete_last_push_date, delete_last_push_date_epin
from Error_messges import openNewWindow
from Get_Niid_Spool import get_niid_spool
from Get_Niid_Spool_byPolicyNumber import get_niid_spool_byPolicyNumber
from Get_last_push_dates import get_last_push_dates
from Get_last_push_dates_epin import get_last_push_dates_epin
from Push_to_Niid import Push_to_Niid
import os
from pathlib import Path
from dotenv import load_dotenv
#
from Write_logs import write_logs  #✅
from Write_logs_epin import write_logs_epin  #✅
from check_update import check_for_update
from push_date import run  #✅
from Change_Sheet_Name import change_sheet_name
from write_last_date import write_last_push_date
from write_last_date_epin import write_last_push_date_epin

LightTheme = ["pulse", "default", "default", "white"]
DarkTheme = ["cyborg", "dark", "default", "black"]
Theme = LightTheme

root = tb.Window(themename=Theme[0])
# root = Tk()

root.title("A&G Policy Push Software")
root.iconbitmap("./A&GICON.ico")
root.state('zoomed')

# Done = ""
push_Sdate = ""
push_Edate = ""

#Chrome window state
SHOW_WINDOW = "null"


def run_program():
    Status = Check_and_install_Updated_driver()

    messagebox.showinfo("Driver verification",
                        Status)

    # Detremine if the chrome window will run headless or not
    def window_satus_on():
        global SHOW_WINDOW
        show_window_button.config(bootstyle="success", text="ON", command=window_satus_off)
        SHOW_WINDOW = "null"

    def window_satus_off():
        global SHOW_WINDOW
        show_window_button.config(bootstyle="secondary", text="OFF", command=window_satus_on)
        SHOW_WINDOW = "--headless"

    #Automatic Push Function
    # def run_auto_update():
    #     # enviroment variables
    #     load_dotenv()
    #     THIRD_PARTY_PLATFORM_LINK = os.getenv("3RD_PARTY_PLATFORM_LINK")
    #     THIRD_PARTY_PLATFORM_EMAIL = os.getenv("3RD_PARTY_PLATFORM_EMAIL")
    #     THIRD_PARTY_DETAILS = [THIRD_PARTY_PLATFORM_LINK, THIRD_PARTY_PLATFORM_EMAIL]
    #     global push_Sdate
    #     global push_Edate
    #     error_message.config(text=f"Starting👩‍💻...", bootstyle="success")
    #     Reg_update_button.config(state="disabled")
    #     auto_push.config(state="disabled")
    #     try:
    #         error_message.config(text=f"Pushing👩‍💻...", bootstyle="success")
    #         # running push
    #         Pushing_dates = run("", "", SHOW_WINDOW, THIRD_PARTY_DETAILS)
    #         for Pushing_date in Pushing_dates:
    #             error_message.config(text=f"Pushed {Pushing_date[0]} to {Pushing_date[1]}", bootstyle="success")
    #             print(f" form auto update pushed {Pushing_date[0]} to {Pushing_date[1]}")
    #             write_logs(Pushing_date[0], Pushing_date[1], Pushing_date[2])
    #             push_Sdate = Pushing_date[3]
    #             push_Edate = Pushing_date[4]
    #             print(push_Sdate, push_Edate)
    #             # write_last_push_date(push_Sdate, push_Edate)
    #         error_message.config(text=f"Done✅", bootstyle="success")
    #         delete_last_push_date()
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="success")
    #         continue_push.config(state="disabled")
    #         return push_Sdate, push_Edate
    #     except Exception as e:
    #         # writing the last push date so for the continue function
    #         write_last_push_date(push_Sdate, push_Edate)
    #         print(e)
    #         #deleting the niid file
    #         delete()
    #         continue_push.config(state="enabled")
    #         error_message.config(text=f"There was an error", bootstyle="danger")
    #         Reg_update_button.config(state="enabled")
    #         auto_push.config(state="enabled")
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="danger")
    #         return push_Sdate, push_Edate
    #     finally:
    #         Reg_update_button.config(state="enabled")
    #         auto_push.config(state="enabled")

    # Continue Pusshing if an error occurs
    # def continue_run_program_auto():
    #     # enviroment variables
    #     load_dotenv()
    #     THIRD_PARTY_PLATFORM_LINK = os.getenv("3RD_PARTY_PLATFORM_LINK")
    #     THIRD_PARTY_PLATFORM_EMAIL = os.getenv("3RD_PARTY_PLATFORM_EMAIL")
    #     THIRD_PARTY_DETAILS = [THIRD_PARTY_PLATFORM_LINK, THIRD_PARTY_PLATFORM_EMAIL]
    #     START_DATE, END_DATE = get_last_push_dates()
    #     print(f"push dates {START_DATE},{END_DATE}")
    #     time.sleep(4)
    #     error_message.config(text=f"Starting👩‍💻...", bootstyle="success")
    #     Reg_update_button.config(state="disabled")
    #     auto_push.config(state="disabled")
    #     continue_push.config(state="disabled")
    #     try:
    #         error_message.config(text=f"Pushing👩‍💻...", bootstyle="success")
    #         # Continuing push form last date
    #         Pushing_dates = run(START_DATE, END_DATE, SHOW_WINDOW, THIRD_PARTY_DETAILS)
    #         for Pushing_date in Pushing_dates:
    #             error_message.config(text=f"Pushed {Pushing_date[0]} to {Pushing_date[1]}", bootstyle="success")
    #             print(f" from continue update pushed {Pushing_date[0]} to {Pushing_date[1]}")
    #             write_logs(Pushing_date[0], Pushing_date[1], Pushing_date[2])
    #             # write_last_push_date(START_DATE, END_DATE)
    #         error_message.config(text=f"Done✅", bootstyle="success")
    #         delete_last_push_date()
    #         Reg_update_button.config(state="enabled")
    #         auto_push.config(state="enabled")
    #         continue_push.config(state="disabled")
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="success")
    #     except Exception as e:
    #         # write_last_push_date(START_DATE, END_DATE)
    #         delete()
    #         error_message.config(text=f"There was an error", bootstyle="danger")
    #         print(e)
    #         continue_push.config(state="enabled")
    #         Reg_update_button.config(state="enabled")
    #         auto_push.config(state="enabled")
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="danger")

    # def run_epin_auto():
    #     # enviroment variables
    #     load_dotenv()
    #     E_PIN_PLATFORM_LINK = os.getenv("E_PIN_PLATFORM_LINK")
    #     E_PIN_PLATFORM_EMAIL = os.getenv("E_PIN_PLATFORM_EMAIL")
    #     E_PIN_DETAILS = [E_PIN_PLATFORM_LINK, E_PIN_PLATFORM_EMAIL]
    #     global push_Sdate
    #     global push_Edate
    #     error_message.config(text=f"Starting👩‍💻...", bootstyle="success")
    #     Reg_update_button.config(state="disabled")
    #     auto_push_epin.config(state="disabled")
    #     try:
    #         error_message.config(text=f"Pushing👩‍💻...", bootstyle="success")
    #         # running push
    #         Pushing_dates = run("", "", SHOW_WINDOW, E_PIN_DETAILS)
    #         for Pushing_date in Pushing_dates:
    #             error_message.config(text=f"Pushed {Pushing_date[0]} to {Pushing_date[1]}", bootstyle="success")
    #             print(f"pushed {Pushing_date[0]} to {Pushing_date[1]}")
    #             write_logs_epin(Pushing_date[0], Pushing_date[1], Pushing_date[2])
    #             push_Sdate = Pushing_date[3]
    #             push_Edate = Pushing_date[4]
    #             print(push_Sdate, push_Edate)
    #             write_last_push_date_epin(push_Sdate, push_Edate)
    #         error_message.config(text=f"Done✅", bootstyle="success")
    #         delete_last_push_date_epin()
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="success")
    #         continue_push.config(state="disabled")
    #         return push_Sdate, push_Edate
    #     except Exception as e:
    #         # writing the last push date so for the continue function
    #         write_last_push_date_epin(push_Sdate, push_Edate)
    #         print(e)
    #         #deleting the niid file
    #         delete()
    #         continue_push.config(state="enabled")
    #         error_message.config(text=f"There was an error", bootstyle="danger")
    #         Reg_update_button.config(state="enabled")
    #         auto_push_epin.config(state="enabled")
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="danger")
    #         return push_Sdate, push_Edate
    #     finally:
    #         Reg_update_button.config(state="enabled")
    #         auto_push_epin.config(state="enabled")

    # def continue_run_program_auto_epin():
    #     # enviroment variables
    #     load_dotenv()
    #     E_PIN_PLATFORM_LINK = os.getenv("E_PIN_PLATFORM_LINK")
    #     E_PIN_PLATFORM_EMAIL = os.getenv("E_PIN_PLATFORM_EMAIL")
    #     E_PIN_DETAILS = [E_PIN_PLATFORM_LINK, E_PIN_PLATFORM_EMAIL]
    #

    #     START_DATE, END_DATE = get_last_push_dates_epin()
    #     print(f"push dates {START_DATE},{END_DATE}")
    #     time.sleep(4)
    #     error_message.config(text=f"Starting👩‍💻...", bootstyle="success")
    #     Reg_update_button.config(state="disabled")
    #     auto_push_epin.config(state="disabled")
    #     continue_push_epin.config(state="disabled")
    #     try:
    #         error_message.config(text=f"Pushing👩‍💻...", bootstyle="success")
    #         # Continuing push form last date
    #         Pushing_dates = run(START_DATE, END_DATE, SHOW_WINDOW, E_PIN_DETAILS)
    #         for Pushing_date in Pushing_dates:
    #             error_message.config(text=f"Pushed {Pushing_date[0]} to {Pushing_date[1]}", bootstyle="success")
    #             print(f"pushed {Pushing_date[0]} to {Pushing_date[1]}")
    #             write_logs_epin(Pushing_date[0], Pushing_date[1], Pushing_date[2])
    #             write_last_push_date_epin(START_DATE, END_DATE)
    #         error_message.config(text=f"Done✅", bootstyle="success")
    #         delete_last_push_date_epin()
    #         Reg_update_button.config(state="enabled")
    #         auto_push_epin.config(state="enabled")
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="success")
    #     except Exception as e:
    #         write_last_push_date_epin(START_DATE, END_DATE)
    #         delete()
    #         error_message.config(text=f"There was an error", bootstyle="danger")
    #         print(e)
    #         continue_push_epin.config(state="enabled")
    #         Reg_update_button.config(state="enabled")
    #         auto_push_epin.config(state="enabled")
    #         time.sleep(10)
    #         error_message.config(text=f"", bootstyle="danger")

    Stop_Loop = False

    def stop_Loop():
        Stop_Loop = True

    #Manual update function
    def update():
        # enviroment variables
        load_dotenv()
        THIRD_PARTY_PLATFORM_LINK = os.getenv("3RD_PARTY_PLATFORM_LINK")
        THIRD_PARTY_PLATFORM_EMAIL = os.getenv("3RD_PARTY_PLATFORM_EMAIL")
        THIRD_PARTY_DETAILS = [THIRD_PARTY_PLATFORM_LINK, THIRD_PARTY_PLATFORM_EMAIL]
        # my_progress.start()
        error_message.config(text="Working on it👩‍💻", bootstyle="success")
        Reg_update_button.config(state="disabled")
        policy_push_button.config(state="disabled")
        downloads_path = Path.home() / "Downloads"
        file_path = f"{downloads_path}/NIID Spool.xlsx"

        # Getting the date from the input
        input_start_date = start_date.entry.get()
        input_end_date = end_date.entry.get()

        # Converting dates to objects for comparison
        date_format = "%d-%b-%y"  # Day-Month-Year format
        startDate = datetime.strptime(input_start_date, date_format)
        endDate = datetime.strptime(input_end_date, date_format)
        print(startDate)
        print(endDate)




        # Getting error message if the date format is wrong
        ErrorMessage = "Enter a valid Date"
        if (endDate < startDate):
            print(input_end_date + input_start_date)
            error_message.config(text=ErrorMessage, bootstyle="danger")
            Reg_update_button.config(state="enabled")
            policy_push_button.config(state="enabled")
            time.sleep(3)
            error_message.config(text="")
        else:
            Reg_update_button.config(state="disabled")
            policy_push_button.config(state="disabled")
            # Getting the formated date
            # formated_start_date = format_date(edited_start_date)
            # formated_end_date = format_date(edited_end_date)
            #Getting the file from A&G
            try:
                Reg_update_button.config(state="disabled")
                policy_push_button.config(state="disabled")
                error_message.config(text="Geting the file👩‍💻", bootstyle="success")
                # Deleting the NIIID File If it exists
                delete()
                get_niid_spool(input_start_date, input_end_date, SHOW_WINDOW, THIRD_PARTY_DETAILS)
                error_message.config(text="Edditing Sheet‍💻", bootstyle="success")
                change_sheet_name()
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    Reg_update_button.config(state="enabled")
                    policy_push_button.config(state="enabled")
                    delete()
                    time.sleep(3)
                    error_message.config(text="", )
                    return

            print("gotten Data")
            try:
                error_message.config(text="Pushing to NIID👩‍💻", bootstyle="success")
                errmessage = Push_to_Niid(SHOW_WINDOW)
                openNewWindow(root, errmessage)
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    Reg_update_button.config(state="enabled")
                    policy_push_button.config(state="enabled")
                    delete()
                    time.sleep(3)
                    error_message.config(text="", )
                    return

            error_message.config(text="Done✅", bootstyle="success")
            time.sleep(3)
            error_message.config(text="")
            print("Done")
            #deleting file when done
            delete()
            Reg_update_button.config(state="enabled")
            policy_push_button.config(state="enabled")

    def update_byPolicyNumber():
        # enviroment variables
        load_dotenv()
        THIRD_PARTY_PLATFORM_LINK = os.getenv("3RD_PARTY_PLATFORM_LINK")
        THIRD_PARTY_PLATFORM_EMAIL = os.getenv("3RD_PARTY_PLATFORM_EMAIL")
        THIRD_PARTY_DETAILS = [THIRD_PARTY_PLATFORM_LINK, THIRD_PARTY_PLATFORM_EMAIL]
        # my_progress.start()
        error_message.config(text="Working on it👩‍💻", bootstyle="success")
        policy_push_button.config(state="disabled")
        Reg_update_button.config(state="disabled")
        downloads_path = Path.home() / "Downloads"
        file_path = f"{downloads_path}/NIID Spool.xlsx"

        # Getting the date from the input
        POLICY_NUMBER = policy_number.get()

        # Getting error message if the date format is wrong
        ErrorMessage = "Enter a valid Policy number"
        if (POLICY_NUMBER == ""):
            error_message.config(text=ErrorMessage, bootstyle="danger")
            policy_push_button.config(state="enabled")
            Reg_update_button.config(state="enabled")
            time.sleep(3)
            error_message.config(text="")
        else:
            policy_push_button.config(state="disabled")
            Reg_update_button.config(state="disabled")
            # Getting the formated date
            # formated_start_date = format_date(edited_start_date)
            # formated_end_date = format_date(edited_end_date)
            #Getting the file from A&G
            try:
                policy_push_button.config(state="disabled")
                Reg_update_button.config(state="disabled")
                error_message.config(text="Geting the file👩‍💻", bootstyle="success")
                # Deleting the NIIID File If it exists
                delete()
                get_niid_spool_byPolicyNumber(POLICY_NUMBER, SHOW_WINDOW, THIRD_PARTY_DETAILS)
                error_message.config(text="Edditing Sheet‍💻", bootstyle="success")
                change_sheet_name()
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    policy_push_button.config(state="enabled")
                    Reg_update_button.config(state="enabled")
                    delete()
                    time.sleep(3)
                    error_message.config(text="", )
                    return

            print("gotten Data")
            try:
                error_message.config(text="Pushing to NIID👩‍💻", bootstyle="success")
                errmessage = Push_to_Niid(SHOW_WINDOW)
                openNewWindow(root, errmessage)
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    policy_push_button.config(state="enabled")
                    Reg_update_button.config(state="enabled")
                    delete()
                    time.sleep(3)
                    error_message.config(text="", )
                    return

            error_message.config(text="Done✅", bootstyle="success")
            time.sleep(3)
            error_message.config(text="")
            print("Done")
            #deleting file when done
            delete()
            policy_push_button.config(state="enabled")
            Reg_update_button.config(state="enabled")


    def update_epin():
        # enviroment variables
        load_dotenv()
        E_PIN_PLATFORM_LINK = os.getenv("E_PIN_PLATFORM_LINK")
        E_PIN_PLATFORM_EMAIL = os.getenv("E_PIN_PLATFORM_EMAIL")
        E_PIN_DETAILS = [E_PIN_PLATFORM_LINK, E_PIN_PLATFORM_EMAIL]
        # my_progress.start()
        error_message.config(text="Working on it👩‍💻", bootstyle="success")
        Reg_update_button2.config(state="disabled")
        downloads_path = Path.home() / "Downloads"
        file_path = f"{downloads_path}/NIID Spool.xlsx"

        # Getting the date from the input
        input_start_date = start_date.entry.get()
        input_end_date = end_date.entry.get()

        # Getting error message if the date format is wrong
        ErrorMessage = "Enter a valid Date"
        if (input_end_date < input_start_date):
            error_message.config(text=ErrorMessage, bootstyle="danger")
            Reg_update_button2.config(state="enabled")
            time.sleep(3)
            error_message.config(text="")
        else:
            # Reg_update_button.config(state="enabled")
            # # Getting the formated date
            # formated_start_date = format_date(input_start_date)
            # formated_end_date = format_date(input_end_date)
            # Getting the file from A&G
            try:
                Reg_update_button2.config(state="disabled")
                error_message.config(text="Geting the file👩‍💻", bootstyle="success")
                get_niid_spool(input_start_date, input_end_date, SHOW_WINDOW, E_PIN_DETAILS)
                error_message.config(text="Edditing Sheet‍💻", bootstyle="success")
                change_sheet_name()
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    Reg_update_button2.config(state="enabled")
                    delete()
                    time.sleep(3)
                    error_message.config(text="", )
                    return

            print("gotten Data")
            try:
                error_message.config(text="Pushing to NIID👩‍💻", bootstyle="success")
                errmessage = Push_to_Niid(SHOW_WINDOW)
                openNewWindow(root, errmessage)
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    Reg_update_button2.config(state="enabled")
                    delete()
                    time.sleep(3)
                    error_message.config(text="", )
                    return

            error_message.config(text="Done✅", bootstyle="success")
            time.sleep(3)
            error_message.config(text="")
            print("Done")
            # deleting file when done
            delete()
            Reg_update_button2.config(state="enabled")

    # Push Manally run in background thread
    def run_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update, daemon=True)
        thread.start()

    def run_function_in_background_update_epin():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_epin, daemon=True)
        thread.start()

    def run_function_in_background_update_byPolicyNumber():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update_byPolicyNumber, daemon=True)
        thread.start()

    def run_check_and_update_software():
        window = root
        thread = threading.Thread(target=check_for_update, args=(window,), daemon=True)
        thread.start()

    # check_for_update(root)


    run_check_and_update_software()

    # Push Automatically run in background thread
    # def run_program_auto():
    #     # Create a thread to run the long_running_function
    #     thread = threading.Thread(target=run_auto_update)
    #     thread.start()
    #
    # def run_epin_program_auto():
    #     # Create a thread to run the long_running_function
    #     thread = threading.Thread(target=run_epin_auto)
    #     thread.start()
    #
    # # Continuing Push Automatically run in background thread
    # def continue_run_program_auto_background():
    #     # Create a thread to run the long_running_function
    #     thread = threading.Thread(target=continue_run_program_auto)
    #     thread.start()
    #
    # def continue_run_program_auto_epin_background():
    #     # Create a thread to run the long_running_function
    #     thread = threading.Thread(target=continue_run_program_auto_epin)
    #     thread.start()

    #User Interface GUI
    my_frame = customtkinter.CTkFrame(root, fg_color=Theme[3], border_width=2, width=800, height=550)
    my_frame.pack(fill="both", expand=True, pady=50, padx=100)
    root.rowconfigure(4, weight=1)

    my_label = tb.Label(my_frame, text="Push Manually", bootstyle="default", font=("Inter", 18))
    my_label.pack(pady=(20, 1), padx=(20, 20))

    start_date = tb.DateEntry(my_frame, bootstyle="danger", dateformat=('%d-%b-%y'))
    start_date.pack(pady=5)

    end_date = tb.DateEntry(my_frame, bootstyle="danger", dateformat=('%d-%b-%y'))
    end_date.pack(pady=5)

    Reg_update_button = tb.Button(my_frame, bootstyle="danger", text="Push", width=30,
                                  command=run_function_in_background)
    Reg_update_button.pack(padx=0, pady=10, )

    Reg_update_button2 = tb.Button(my_frame, bootstyle="danger", text="Push (E-PIN)", width=30,
                                   command=run_function_in_background_update_epin)
    Reg_update_button2.pack(padx=0, pady=10, )

    # my_label = tb.Label(my_frame, text="Push Policy Automatically ", bootstyle="default", font=("Inter", 18))
    # my_label.pack(pady=(20, 1), padx=(20, 20))
    #
    # info = tb.Label(my_frame, text="If an error occurs while pushing the continue push button will be enabled",
    #                 bootstyle="default", font=("Inter", 9))
    # info.pack(pady=0, padx=(20, 20))
    #
    # info = tb.Label(my_frame, text="Check the README.md file for more info", bootstyle="default", font=("Inter", 9))
    # info.pack(pady=5, padx=(20, 20))
    #
    # auto_push = tb.Button(my_frame, bootstyle="danger", text="Push Automatically", width=30, command=run_program_auto)
    # auto_push.pack(padx=(0, 0), pady=10, )
    #
    # auto_push_epin = tb.Button(my_frame, bootstyle="danger", text="Push Automatically (E-PIN)", width=30,
    #                            command=run_epin_program_auto)
    # auto_push_epin.pack(padx=(0, 0), pady=10, )
    #
    # if check_last_push_file() == True:
    #     continue_push = tb.Button(my_frame, bootstyle="danger", text="Continue Push?", width=25, state="enabled",
    #                               command=continue_run_program_auto_background)
    #     continue_push.pack(padx=(0, 0), pady=10, )
    # else:
    #     continue_push = tb.Button(my_frame, bootstyle="danger", text="Continue Push?", width=25, state="disabled",
    #                               command=continue_run_program_auto_background)
    #     continue_push.pack(padx=(0, 0), pady=10, )
    #
    # if check_last_push_file_epin() == True:
    #     continue_push_epin = tb.Button(my_frame, bootstyle="danger", text="Continue Push(E-PIN)?", width=25,
    #                                    state="enabled",
    #                                    command=continue_run_program_auto_epin_background)
    #     continue_push_epin.pack(padx=(0, 0), pady=10, )
    # else:
    #     continue_push_epin = tb.Button(my_frame, bootstyle="danger", text="Continue Push(E-PIN)?", width=25,
    #                                    state="disabled",
    #                                    command=continue_run_program_auto_epin_background)
    #     continue_push_epin.pack(padx=(0, 0), pady=10, )

    my_label = tb.Label(my_frame, text="Push by Policy Number", bootstyle="default", font=("Inter", 18))
    my_label.pack(pady=(20, 1), padx=(20, 20))

   #Push by Policy Number
    policy_number = tb.Entry(my_frame, bootstyle="default", width=30,)
    policy_number.pack(pady=5)

    policy_push_button = tb.Button(my_frame, bootstyle="danger", text="Push", width=30,
                                   command=run_function_in_background_update_byPolicyNumber)
    policy_push_button.pack(padx=0, pady=10,)


    my_label = tb.Label(my_frame, text="Show Chrome Window", bootstyle=Theme[2], font=("Helvetica", 12))
    my_label.pack(pady=10, padx=(20, 20))

    show_window_button = tb.Button(my_frame, text="ON", state="enabled", bootstyle="success", width=20,
                                   command=window_satus_off)
    show_window_button.pack(pady=0, padx=0)

    # stop_loop = tb.Button(my_frame, text="Stop Loop", state="enabled", bootstyle="success", width=20,
    #                                command=stop_Loop)
    # stop_loop.pack(pady=20, padx=10)

    error_message = tb.Label(my_frame, text="", bootstyle="danger", font=("Inter", 9))
    error_message.pack(pady=2, padx=(10, 20))

    root.mainloop()


if __name__ == '__main__':
    run_program()

