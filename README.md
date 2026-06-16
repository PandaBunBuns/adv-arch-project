# µRISCV Processor Simulator
## Milestone #1: Program input w/ error checking, opcode
### Implement RISC-V code parsing for opcode construction

We are using streamlit as our web framework. 

We have implemented opcode generation for each instruction. Each line is parsed for its mnemonic, rs1, rs2, and immediate parameters, as well as checking for branch instructions and branch labels. For this milestone, we've decided to utilize a symbol table for handling branching. 

## Running the Program
Initializing the environment</br>
```source venv/Scripts/activate```
</br>
</br>
Install dependencies</br>
```pip install -r requirements.txt```
</br>
</br>
Running the application </br>
```streamlit run app.py ```

## Authors
**Frances Danielle Solis**<br>
**Kaizen Edwin Rodriguez**<br>
# Demonstration Video
[![Demonstration Video](https://markdown-videos-api.jorgenkh.no/youtube/DKUcyWy09rM)](https://youtu.be/DKUcyWy09rM)

Link: <a href="https://youtu.be/DKUcyWy09rM">https://youtu.be/DKUcyWy09rM</a>
