from assembler import assemble_r_type, assemble_i_type, assemble_i_shift_type, assemble_s_type, assemble_b_type



def parse_and_assemble(code_input, isa_dict):


    parts_newLine = code_input.split('\n')
    lines = []
    symbol_table={}
    current_pc = 0

    opcodes =[]
    output =[]

    # Parse labels and basic structure
    for line in parts_newLine:
        temp = line.split()
        if not temp:
            continue

        if ':' in line:
            label, rest = line.split(':', 1)
            symbol_table[label.strip()] = current_pc

            print("label: ", label)
            print("rest: ", rest)

            # Address code past the semicolon
            rest = rest.strip()

            if rest:
                lines.append((current_pc, rest.split()))
                current_pc +=4
                

        else:
            lines.append((current_pc, temp))
            current_pc +=4            

    # Assemble instructions
    for pc, parts in lines:
        mnemonic = parts[0].upper()

        # Grab arguments based on their length
        rd_str = parts[1] if len(parts) > 1 else None
        rs1_str = parts[2] if len(parts) > 2 else None
        rs2_str = parts[3] if len(parts) > 3 else None

        if mnemonic not in isa_dict:
            raise ValueError( f"Error: Instruction '{mnemonic}' is not currently supported in this demo.")
        
        instruction_info = isa_dict[mnemonic]

        if instruction_info["type"] == "R":
            hex_result = assemble_r_type(
                instruction_info["opcode"], instruction_info["funct3"],
                instruction_info["funct7"], rd_str, rs1_str, rs2_str
            )

        elif instruction_info["type"] == "I":
            rs1_split = rs1_str.split("(")
            imm_val = rs1_split[0]
            rs1_str = rs1_split[1][:-1]
            hex_result = assemble_i_type(
                instruction_info["opcode"], instruction_info["funct3"],
                rd_str, imm_val, rs1_str
            )
        
        elif instruction_info["type"] == "I_shift":
            hex_result = assemble_i_shift_type(
                instruction_info["opcode"], instruction_info["funct3"],
                instruction_info["funct7"], rd_str, rs1_str, rs2_str
            )
        elif instruction_info["type"] == "S":
            rs1_split = rs1_str.split("(")
            imm_val = rs1_split[0]
            rs1_str = rs1_split[1][:-1]
            hex_result = assemble_s_type(
                instruction_info["opcode"], instruction_info["funct3"],
                rs1_str, rs1_split, rd_str
            )
        
        elif instruction_info["type"] == "B":
            target_label = rs2_str
        
            # Calculate offset
            if target_label in symbol_table:
                target_pc = symbol_table[target_label]
                offset = target_pc - pc
            else:
                try:
                    offset = int(target_label)
                except ValueError:
                    raise ValueError(f"Label '{target_label}' not found.")
                
            hex_result = assemble_b_type(
                instruction_info["opcode"], instruction_info["funct3"],
                rd_str, rs1_str, rs2_str
            )
        
        else:
            raise NotImplementedError(f"The assembler logic for {instruction_info['type']}-Type instructions isn't built yet!")        

        opcodes.append(hex_result)

    return opcodes

        

