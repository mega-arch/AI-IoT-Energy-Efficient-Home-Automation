from machine import Pin, ADC, PWM
import time

# Pin configurations
ldr_pin = ADC(Pin(26))  # LDR sensor connected to GPIO26 (ADC0)
relay_pin = Pin(15, Pin.OUT)  # Relay connected to GPIO15 (for controlling light)
pwm_pin = PWM(Pin(14))  # PWM pin for adjusting light intensity

# LDR reading range
ldr_min = 0  # Minimum LDR reading
ldr_max = 65535  # Maximum LDR reading (for 16-bit ADC)

# Set PWM frequency (to adjust brightness)
pwm_pin.freq(1000)  # Frequency 1kHz for smooth brightness control

def read_ldr():
    ldr_value = ldr_pin.read_u16()  # Read the LDR value
    return ldr_value

def adjust_light_intensity(ldr_value):
    # Calculate the brightness as a percentage of maximum intensity
    brightness = (ldr_value / ldr_max) * 100
    pwm_duty = int((brightness / 100) * 1023)  # Map brightness to PWM duty cycle (0-1023)
    pwm_pin.duty_u16(pwm_duty)  # Set PWM duty cycle to control brightness

def main():
    while True:
        ldr_value = read_ldr()
        print("LDR Value:", ldr_value)  # Print LDR value for debugging
        
        # Adjust the light intensity based on LDR sensor reading
        adjust_light_intensity(ldr_value)
        
        # Control relay (turn on/off based on LDR reading)
        if ldr_value < 30000:  # If light level is low, turn on the light
            relay_pin.value(1)  # Turn light ON
        else:  # If light level is high, turn off the light
            relay_pin.value(0)  # Turn light OFF
        
        time.sleep(1)  # Delay for 1 second before taking the next reading

if __name__ == '__main__':
    main()
