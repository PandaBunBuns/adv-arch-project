import streamlit as st
from dicts import isa_dict, reg_dict
from assembler import assemble_r_type, assemble_i_type, assemble_i_shift_type, assemble_s_type, assemble_b_type
from parser import parse_and_assemble

st.set_page_config(page_title="µRISCV Assembler", layout="wide")

st.title("µRISCV Processor Simulator")
st.subheader("Milestone #1: Parser & Opcode Generator")

# Error Messages (Placed at top for visibility)
error_container = st.empty()

# The Code Editor Input
code_input = st.text_area("Assembly Code Input", height=150)

if st.button("Assemble"):
    if not code_input.strip():
        error_container.error("Error: Please enter some assembly code.")
    else:
        try:
            opcodes = parse_and_assemble(code_input, isa_dict)

            st.success("Assembly Successful!")
            st.code(f"Original:\n{code_input}\nHex Opcode: {opcodes}", language="plaintext")
        
        except ValueError as ve:
            error_container.error(f"Error: {ve}")

        except NotImplementedError as nie:
            error_container.warning(f"Warning: {nie}")
        
        except Exception as e:
            error_container.error(f"Parsing Error: {str(e)}")