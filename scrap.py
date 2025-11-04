import keyboard 
def main():
    print (" hello nigas")
    print ("NIC NICE")
keyboard.add_hotkey('a', lambda: keyboard.write('Geek')) 
keyboard.add_hotkey('ctrl + shift + a', main) 

keyboard.wait('esc')
