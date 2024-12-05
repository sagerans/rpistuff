import network, socket, machine
from time import sleep

ssid = 'Verizon_7HTM4Y'
password = 'bye4-jet-clear'

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected == False:
        print('Waiting for connection...')
        sleep(1)
    return(wlan.ifconfig()[0])

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)

def serve(connection):
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = cline.recv(1024)
        request = str(request)
        print(request)
        client.close()
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request == '/lightoff?':
            pico_led.off()
            state = 'OFF'
        temperature = pico_temp_sensor.temp
        html = webpage(temperature, state)
        client.send(html)
        client.close()

def webpage(temperature, state):
    html = f"""
        <!DOCTYPE html>
        <html>
          <body>
            Hi Betsy :-)
            <form action="./lighton">
              <input type="submit" value="Turn me on" />
            </form>
            <form action="./lightoff">
              <input type="submit" value="Turn me off" />
            </form>
            <p>LED is {state}!</p>
            <p>Temperature is {temperature}!</p>
          </body>
        </html>
        """
    return str(html)

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except:
    machine.reset()
