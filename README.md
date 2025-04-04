RGB LED Controller
==================

A simple Python program to control an RGB LED strip using a Raspberry Pi's GPIO pins. This program allows you to manually set the color of the LED strip via sliders for Red, Green, and Blue components. You can also fade through colors in a loop with a customizable fade speed and configure which GPIO pins to use.

Features
--------

-   **Manual Color Control**: Adjust the RGB values via sliders.

-   **Fade Loop**: Automatically cycles through colors with a speed controlled by a slider.

-   **Custom GPIO Pin Configuration**: Specify which GPIO pins to use for the Red, Green, and Blue channels.

-   **Real-time Updates**: Displays the current color values as they change.

Requirements
------------

-   **Hardware**:

    -   Raspberry Pi with the RPi.GPIO library installed

    -   RGB LED strip connected to your Raspberry Pi's GPIO pins

-   **Software**:

    -   Python 3.x

    -   Tkinter for the GUI

    -   RPi.GPIO library

Installation
------------

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/rupoo04/RGB-LED-Controller.git
    cd RGB-LED-ontroller
    ```

2.  **Install required libraries**:\
    Update your package list and install Tkinter if it's not already installed:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-tk
    ```

    Then install the RPi.GPIO library:
    ```bash
    sudo pip3 install RPi.GPIO
    ```

4.  **Run the program**:

    bash

    CopyEdit

    ```bash
    python3 rgb_controller.py
    ```

Usage
-----

-   **Set Color**:\
    Use the Red, Green, and Blue sliders to set the desired color, then click the "Set Color" button.

-   **Fade Colors**:\
    Click the "Toggle Fade" button to start or stop the continuous color fade. Adjust the fade speed with the "Fade Speed" slider.

-   **Configure GPIO Pins**:\
    Enter your desired GPIO pin numbers for each color channel (Red, Green, Blue) and click the "Apply GPIO Pins" button.

Default GPIO Pins
-----------------

The program uses the following GPIO pins by default:

-   **Red**: GPIO 17

-   **Green**: GPIO 22

-   **Blue**: GPIO 24

To use different pins, simply change the values in the provided input fields in the GUI and click "Apply GPIO Pins".

Troubleshooting
---------------

-   Verify that your wiring matches the GPIO pins configured in the program.

-   Ensure that the RPi.GPIO library is correctly installed.

-   Check that the correct Python version is being used (Python 3.x).

License
-------

This project is open-source and available under the MIT License. See the LICENSE file for more details.

Contributions
-------------

Feel free to fork this project and submit pull requests. Contributions and improvements are welcome!

* * * * *

Happy coding and enjoy controlling your RGB LED strip!
