# Instructions

## Package Install
1. Create a virtual environment and place the field_processing_unit.py and analytics_engine.py files within it.
2. Activate the virtual environment
3. Install the requirements specified in the requirements.txt file

## Run
1. Open a terminal within the virtual environment (typically something like './venv\Scripts\Activate' or './venv\Scripts\Activate.ps1')
2. In one, run 'counterfit'
3. In the web browser that opens to the counterfit interface, create a light sensor with a pin of 1 and a relay with a pin of 2.
4. For the light sensor, set the values between 400 and 600, random.
5. In another terminal within the virtual environment, run 'python analytics_engine.py'
6. In another terminal within the virtual environment, run 'python field_processing_unit.py'
7. Watch the analytics engine send commands to the field processing unit and the photovoltaic array position change.
8. Observe the opening and closing of the relay on CounterFit's web interface, commensurate with the array position changes.