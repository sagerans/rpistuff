
import network, socket, machine
from time import sleep
from picozero import pico_temp_sensor, pico_led

ssid = 'Verizon_7HTM4Y'
password = 'bye4-jet-clear'

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return connection

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

def serve(connection):
    state = 'ON'
    pico_led.on()
    temperature = pico_temp_sensor.temp
    print(temperature)
    while True:
        print('serving 1')
        client = connection.accept()[0]
        print('client', client)
        print('serving 2')
        request = client.recv(1024)
        print('serving 3')
        request = str(request)
        print(request)
        client.close()
        print('serving 4')
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
        print('serving 5')
        temperature = pico_temp_sensor.temp
        print('serving 6')
        html = webpage(temperature, state)
        print('serving 7')
        client.send(html)
        print('serving 8')
        client.close()



try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except:
    machine.reset()
 
