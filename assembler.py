def assemble_r_type(opcode_bin, funct3_bin, funct7_bin, rs1_str, rs2_str, rd_str):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    funct7 = int(funct7_bin, 2)
    rs1 = int(rs1_str.replace('x', '').replace(',', ''))
    rs2 = int(rs2_str.replace('x', '').replace(',', ''))
    rd = int(rd_str.replace('x', '').replace(',', ''))

    instruction = 0
    instruction |= (funct7 << 25)
    instruction |= (funct7 << 25)
    instruction |= (rs2 << 20)
    instruction |= (rs1 << 15)
    instruction |= (funct3 << 12)
    instruction |= (rd << 7)
    instruction |= opcode

    return f"0x{instruction:08X}"

def assemble_i_type(opcode_bin, funct3_bin, rd_str, imm_val, rs1_str):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    rd = int(rd_str.replace('x', '').replace(',', ''))
    imm = int(imm_val)
    rs1 = int(rs1_str.replace('x', '').replace(',', ''))

    instruction = 0
    instruction |= (imm << 20)
    instruction |= (rs1 << 15)
    instruction |= (funct3 << 12)
    instruction |= (rd << 7)
    instruction |= opcode

    return f"0x{instruction:08X}"

def assemble_i_shift_type(opcode_bin, funct3_bin, rd_str, imm_val, rs1_str):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    rd = int(rd_str.replace('x', '').replace(',', ''))
    imm = int(imm_val.replace(',', ''))
    rs1 = int(rs1_str.replace('x', '').replace(',', ''))

    instruction = 0
    instruction |= (imm << 20)
    instruction |= (rs1 << 15)
    instruction |= (funct3 << 12)
    instruction |= (rd << 7)
    instruction |= opcode

    return f"0x{instruction:08X}"

def assemble_s_type(opcode_bin, funct3_bin, funct7_bin, rs1_str, rs2_str):
    pass

def assemble_b_type(opcode_bin, funct3_bin, rs1_str, rs2_str, imm_val):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    rs1 = int(rs1_str.replace('x', '').replace(',', ''))
    rs2 = int(rs2_str.replace('x', '').replace(',', ''))
    
    #Calculate Two's Complement
    if imm_val < 0:
        imm_val = (1 << 13) + imm_val
        
    imm_12   = (imm_val >> 12) & 0x1    # shift to the right by 12, gets 1 bit
    imm_11   = (imm_val >> 11) & 0x1    # shift to the right by 11, gets 1 bit
    imm_10_5 = (imm_val >> 5)  & 0x3F   # shift to the right by 06, gets 6 bit (0x3F = 111111)
    imm_4_1  = (imm_val >> 1)  & 0xF    # shift to the right by 11, gets 4 bit (0xF = 1111)
    
    instruction = 0
    instruction |= (imm_12 << 31)
    instruction |= (imm_10_5 << 25)
    instruction |= (rs2 << 20)
    instruction |= (rs1 << 15)
    instruction |= (funct3 << 12)
    instruction |= (imm_4_1 << 8)
    instruction |= (imm_11 << 7)
    instruction |= opcode
    
    return f"0x{instruction:08X}"