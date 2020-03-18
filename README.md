# Carnet organizer
GUI for organizing your carnets with qr codes.

## Installation
```bash
git clone https://github.com/hyperxpizza/carnet_organizer
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python3 run.py
```

## Adding new carnets
When adding the carnet, program will generate a qr code with unique id of the carnet inside app/engine/database directory

## Screenshots
![alt text](https://raw.githubusercontent.com/hyperxpizza/carnet_organizer/master/img/main.png)

![alt text](https://raw.githubusercontent.com/hyperxpizza/carnet_organizer/master/img/add_img.png)

## TODO
Printing labels with BrotherQL printers (QL-700)