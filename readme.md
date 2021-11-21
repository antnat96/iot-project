# Instructions

## Package Install
1. Create a virtual environment and place the field_processing_unit.py and analytics_engine.py files within it.
2. Activate the virtual environment
3. Install the following with pip
    CounterFit==0.1.3.dev29
    counterfit-connection==0.1.0.dev5
    counterfit-shims-grove==0.1.4.dev5
    counterfit-shims-seeed-python-dht==0.1.0.dev1

## Run
1. Open 3 terminals inside the virtual environment
2. In one, run 'counterfit'
3. In the web browser that opens to the counterfit interface, create a light sensor with a pin of 1.
4. Set the values between 400 and 600, random.
4. In one, run 'python analytics_engine.py'
5. In one, run 'python field_processing_unit.py'