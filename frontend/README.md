
## Installation

Clone the repository
```
git clone https://github.com/ECSHackWeek/ECSBatteryDatabase
cd ECSBatteryDatabase/frontend
```

Install backend dependencies:
```
conda env create -f environment.yaml
conda activate example
```

Use npm to install frontend dependencies:
```
cd frontend/static
npm install
```

## Running example

In one terminal window start webpack:
```
cd frontend/static
npm run watch
```

In a second terminal window, start flask server:
```
python application.py
```

In a web browser, go to the address

http://localhost:5000/
