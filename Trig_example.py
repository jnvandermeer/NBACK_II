import serial
import time
import threading

Connected = True
PulseWidth = 0.01

def ReadThread(port):
    while Connected:
        if port.inWaiting() > 0:
            print ("0x%X"%ord(port.read(1)))

# Open the Windows device manager, search for the "TriggerBox VirtualSerial Port (COM6)"
# in "Ports /COM & LPT)" and enter the COM port number in the constructor.
port = serial.Serial('COM3')

# Start the read thread
thread = threading.Thread(target=ReadThread, args=(port,))
thread.start()

# Set the port to an initial state
port.write([0x00])
time.sleep(PulseWidth)


# Set Bit 0, Pin 2 of the Output(to Amp) connector
port.write([0x01])
time.sleep(PulseWidth)

# Reset Bit 0, Pin 2 of the Output(to Amp) connector
port.write([0x00])
time.sleep(PulseWidth)

# Reset the port to its default state
port.write([0xFF])
time.sleep(PulseWidth)

# Terminate the read thread
Connected = False
thread.join(1.0)

# Close the serial port
port.close()