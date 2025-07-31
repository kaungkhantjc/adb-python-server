# ADB Python Server
ADB Python Server is a simple demo program for connecting to ADB devices and controlling them using a REST API.

## Development

1. Create a Python virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    ```bash
    ./venv/Scripts/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the program:
    ```bash
    uvicorn main:app --reload
    ```
    To access the REST API from other devices, run the program with host `0.0.0.0`:
    ```bash
    uvicorn main:app --host 0.0.0.0 --reload
    ```
    Then, access it using your PC's IP address. On Windows, use the `ipconfig` command to find your PC's IP address.

## REST API

- Test REST API response:
    `GET http://127.0.0.1:8000`

- Get devices:
    `GET http://127.0.0.1:8000/devices`

- Connect to a device via its IP address and port:
    `POST http://127.0.0.1:8000/connect/{{addr}}`
    > Address example: `192.168.0.1:5555`

- Send volume up command to a specified device:
    `POST http://127.0.0.1:8000/device/{serial}/volume_up`
    > Device serial example: `192.168.0.1:5555`

- Send volume down command to a specified device:
    `POST http://127.0.0.1:8000/device/{serial}/volume_down`
    > Device serial example: `192.168.0.1:5555`