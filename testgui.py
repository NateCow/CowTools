import dearpygui.dearpygui as dpg
import os

def save_callback():
    try:
        directory = dpg.get_value("filepath_string")
        if not os.path.isdir(directory):
            print(f"Error: The directory '{directory}' does not exist.")
            return
        files = os.listdir(directory)
        report = open(f'{directory}/_files.txt', 'w')
        report.write('\n'.join(files))
        report.close()
        print(f"File list saved to {directory}/_files.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="List Files"):
    dpg.add_text("This tool will create and open a text file with a list of files in a directory.")
    dpg.add_input_text(label="Filepath", tag="filepath_string", default_value="/path/to/directory")
    dpg.add_button(label="List Files", callback=save_callback)
    
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()