import streamlit as st
from dicts import isa_dict, reg_dict
from assembler import assemble_r_type, assemble_i_type, assemble_i_shift_type, assemble_s_type, assemble_b_type

st.set_page_config(page_title="µRISCV Assembler", layout="wide")

st.title("µRISCV Processor Simulator")
st.subheader("Milestone #1: Parser & Opcode Generator")

# Error Messages (Placed at top for visibility)
error_container = st.empty()

# The Code Editor Input
code_input = st.text_area("Assembly Code Input (Try typing: BEQ x1, x2, 8)", height=150)

if st.button("Assemble"):
    if not code_input.strip():
        error_container.error("Error: Please enter some assembly code.")
    else:
        try:
            parts = code_input.strip().split()
            
            # if len(parts) != 4:
            #     raise ValueError("Syntax Error: Expected format 'MNEMONIC x, y, z'")
            
            mnemonic = parts[0].upper()
            x = parts[1]
            y = parts[2]
            print(len(parts))
            print(x)
            print(y)

            if len(parts) > 3:
                z = parts[3]
                print(z)
            
            if mnemonic in isa_dict:
                instruction_info = isa_dict[mnemonic]
                
                # Check the type to route it to the correct assembler function
                if instruction_info["type"] == "R":
                    rd_str = x
                    rs1_str = y
                    rs2_str = z
                    hex_result = assemble_r_type(
                        instruction_info["opcode"], 
                        instruction_info["funct3"], 
                        instruction_info["funct7"], 
                        rd_str, rs1_str, rs2_str
                    )
                    # st.warning("R-Type assembler function not built yet!")
                    st.success("Assembly Successful!")
                    st.code(f"Original: {code_input}\nHex Opcode: {hex_result}", language="plaintext")

                elif instruction_info["type"] == "I":
                    rd_str = x
                    y_split = y.split("(")
                    imm_val = y_split[0]
                    rs1_str = y_split[1][:-1]
                    print(imm_val)
                    print(rs1_str)
                    hex_result = assemble_i_type(
                        instruction_info["opcode"], 
                        instruction_info["funct3"], 
                        rd_str, imm_val, rs1_str
                    )
                    # st.warning("I-Type assembler function not built yet!")
                    st.success("Assembly Successful!")
                    st.code(f"Original: {code_input}\nHex Opcode: {hex_result}", language="plaintext")
                
                elif instruction_info["type"] == "I_shift":
                    rd_str = x
                    rs1_str = y
                    shamt_str = z
                    hex_result = assemble_i_shift_type(
                        instruction_info["opcode"], 
                        instruction_info["funct3"], 
                        instruction_info["funct7"], 
                        rd_str, rs1_str, shamt_str
                    )
                    # st.warning("I-Type assembler function not built yet!")
                    st.success("Assembly Successful!")
                    st.code(f"Original: {code_input}\nHex Opcode: {hex_result}", language="plaintext")

                elif instruction_info["type"] == "S":
                    rs2_str = x
                    y_split = y.split("(")
                    imm_val = y_split[0]
                    rs1_str = y_split[1][:-1]
                    hex_result = assemble_s_type(
                        instruction_info["opcode"], 
                        instruction_info["funct3"],  
                        rs1_str, imm_val, rs2_str
                    )
                    # st.warning("S-Type assembler function not built yet!")
                    st.success("Assembly Successful!")
                    st.code(f"Original: {code_input}\nHex Opcode: {hex_result}", language="plaintext")

                elif instruction_info["type"] == "B":
                    rs1_str = x
                    rs2_str = y
                    imm_val = int(z)
                    hex_result = assemble_b_type(
                        instruction_info["opcode"], 
                        instruction_info["funct3"], 
                        rs1_str, rs2_str, imm_val
                    )
                    st.success("Assembly Successful!")
                    st.code(f"Original: {code_input}\nHex Opcode: {hex_result}", language="plaintext")
                else:
                    error_container.warning(f"The assembler logic for {instruction_info['type']}-Type instructions isn't built yet!")
            else:
                error_container.error(f"Error: Instruction '{mnemonic}' is not currently supported in this demo.")
                
        except Exception as e:
            error_container.error(f"Parsing Error: {str(e)}")