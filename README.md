# rover2
Rover based on DiddyBorg v2 Robot Kit.

Second Raspberry Pi
---

Responsible for:
- Sense HAT
  - LED matrix
  - Gyroscope
  - Accelerometer
  - Magnetometer
  - Temperature
  - Humidity
  - Barometric pressure

Connects over ethernet to primary Raspberry Pi.


Installation
---
| Item         | Description                   |
|--------------|-------------------------------|
| OS           | Raspberry Pi OS Lite (64-bit) |
| User name    | rover2                        |
| Install Path | /home/rover2/rover2/          |

Project application needs to be present in Install Path. SSH into Raspberry Pi and run in Install Path for installation:

```
  chmod u+x env_setup.sh
  ./env_setup.sh
  chmod u+x install_dev.sh
  ./install_dev.sh
```