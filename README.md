# Heart Pulse Monitoring and Notification System using Arduino

## Step-by-Step Guide

### Step 1: Connecting the Heart Rate Sensor Module to Arduino

Before connecting the Arduino UNO module, ensure that the Arduino programming software is installed on your system. Follow these steps to connect the pulse sensor to the Arduino:

1. **Connect the Pulse Sensor**: Use the three pins of the sensor (GND, VCC, and SIGNAL) to connect it to the Arduino UNO.
   - GND to GND
   - VCC to 5V
   - SIGNAL to A0 (analog pin)

2. **System Preparation**: After successfully connecting, the system is ready for compilation.

**Working of the Heart Rate Sensor**: The pulse sensor contains an LED and a photodiode. When a finger is placed on the sensor, the blood flow in the finger causes light disturbance. The blood absorbs some light, and the remaining light is reflected and detected by the photodiode. The photodiode then outputs a DC signal proportional to the blood volume and flow in the finger, thus detecting the heartbeat.

### Step 2: Coding in Arduino (Calculating Heart Pulse)

After connecting the heart rate sensor, you need to enter the code for calculating the heart pulse into the Arduino console. The process continues to the next step only if the code runs successfully; otherwise, recheck the uploaded code.

**Pseudocode**:
```cpp
// Import required libraries
#include <SoftwareSerial.h>

// Declare variables
int pulseSensorPurplePin = 0;
int LED13 = 13;
int signal;
int threshold = 550;
int s;

// Software serial setup
SoftwareSerial mySerial(10, 11);

void setup() {
  pinMode(LED13, OUTPUT);    // Pin that will blink to your heartbeat
  Serial.begin(9600);        // Setup Serial Communication at certain speed
  mySerial.begin(9600);
}

void loop() {
  signal = analogRead(pulseSensorPurplePin);
  s = signal / 8;
  Serial.print("Your heart beat is: ");
  Serial.println(s);
  if (signal > threshold) {
    digitalWrite(LED13, HIGH);
  } else {
    digitalWrite(LED13, LOW);
  }
  delay(1000);
}
```

### Step 3: Connecting BOLT Wi-Fi Module to Arduino

To automate the system, connect a BOLT Wi-Fi module to the Arduino to establish an internet connection.

1. **Connect BOLT Wi-Fi Module**:
   - Connect the BOLT Wi-Fi module to the Arduino UNO as shown in the respective documentation.

### Step 4: Using AWS VPS to Run Heart Rate Monitoring Code

To run the anomaly pulse checking process, an online Virtual Private Server (VPS) is used. We use Amazon Web Services (AWS) VPS for its reliability.

1. **Setup AWS VPS**:
   - Create a new Linux server dedicated to running the heart rate monitoring code.
   - Upload the code to the VPS to monitor and detect heartbeat anomalies.
   - Store data on the server for future reference.

### Step 5: Checking for Abnormalities

After successfully running the code on the AWS VPS:

1. **Monitor Heartbeat**:
   - If the heartbeat is normal, return to Step 2 to continue monitoring.
   - If an abnormality is detected, proceed to the notification step.

### Step 6: Sending Notification through SMS Service using Twilio

If any abnormality is detected in the heart pulse, the notification module is triggered.

1. **Setup Twilio**:
   - Enter the phone numbers of the concerned caretakers/doctors/end-users in Twilio.
   - Generate an API code in Twilio to connect the server code and trigger the notification.

2. **Trigger Notification**:
   - The system will immediately notify the concerned individuals if any abnormality is detected in the heart pulse.

---

This README file provides a detailed step-by-step guide for setting up and running the Heart Pulse Monitoring and Notification System using Arduino. For any further questions or support, please refer to the full project documentation or visit: https://ieeexplore.ieee.org/document/9395825 
