from dicts import isa_dict, reg_dict

def try_convert(x_str):
    try:
        int(x_str)
        return True
    except ValueError:
        return False


def convert(x_str, if_int=False):
    x_str = x_str.replace(',', '')
    if if_int:
        print(if_int)
        if try_convert(x_str):
            x = int(x_str) 
        elif "x" not in x_str:
            x_str = reg_dict[x_str]
            x = int(x_str.replace('x', ''))
        else: x = int(x_str.replace('x', ''))
        
    else:
        print(if_int)
        # Checks if the address is a variable
        if "x" not in x_str: x_str = reg_dict[x_str]

        # Removes "x" from hex
        x = int(x_str.replace('x', ''))

    return x

def assemble_r_type(opcode_bin, funct3_bin, funct7_bin, rd_str, rs1_str, rs2_str):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    funct7 = int(funct7_bin, 2)
    rd = convert(rd_str)
    rs1 = convert(rs1_str)
    rs2 = convert(rs2_str)

    instruction = 0
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
    rd = convert(rd_str)
    rs1 = convert(rs1_str)
    imm = convert(imm_val, True)

    #Calculate Two's Complement
    if imm < 0:
        imm = (1 << 12) + imm

    instruction = 0
    instruction |= (imm << 20)
    instruction |= (rs1 << 15)
    instruction |= (funct3 << 12)
    instruction |= (rd << 7)
    instruction |= opcode

    return f"0x{instruction:08X}"

def assemble_i_shift_type(opcode_bin, funct3_bin, funct7_bin, rd_str, rs1_str, shamt_str):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    funct7 = int(funct7_bin, 2)
    rd = convert(rd_str)
    rs1 = convert(rs1_str)
    shamt = convert(shamt_str, True)

    instruction = 0
    instruction |= (funct7 << 25)
    instruction |= (shamt << 20)
    instruction |= (rs1 << 15)
    instruction |= (funct3 << 12)
    instruction |= (rd << 7)
    instruction |= opcode

    return f"0x{instruction:08X}"

def assemble_s_type(opcode_bin, funct3_bin, rs1_str, imm_val, rs2_str):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    rs1 = convert(rs1_str)
    rs2 = convert(rs2_str)
    imm = convert(imm_val, True)

    #Calculate Two's Complement
    if imm < 0:
        imm = (1 << 12) + imm

    imm_11_5 = (imm >> 5)  & 0x7F   # shift to the right by 05, gets 7 bit (0x7F = 1111111)
    imm_4_0  = (imm >> 0)  & 0x1F   # shift to the right by 00, gets 5 bit (0x1F = 11111)

    instruction = 0
    instruction |= (imm_11_5 << 25)
    instruction |= (rs2 << 20)
    instruction |= (rs1 << 15)
    instruction |= (funct3 << 12)
    instruction |= (imm_4_0 << 7)
    instruction |= opcode

    return f"0x{instruction:08X}"

def assemble_b_type(opcode_bin, funct3_bin, rs1_str, rs2_str, imm_val):
    opcode = int(opcode_bin, 2)
    funct3 = int(funct3_bin, 2)
    rs1 = convert(rs1_str)
    rs2 = convert(rs2_str)
    imm = convert(imm_val, True)

    # Checks if the address is a variable
    if "x" not in rs1_str: rs1_str = reg_dict[rs1_str]
    if "x" not in rs2_str: rs2_str = reg_dict[rs2_str]

    # Removes "x" from hex
    rs1 = int(rs1_str.replace('x', '').replace(',', ''))
    rs2 = int(rs2_str.replace('x', '').replace(',', ''))
    
    #Calculate Two's Complement
    if imm < 0:
        imm = (1 << 12) + imm
        
    imm_12   = (imm >> 12) & 0x1    # shift to the right by 12, gets 1 bit
    imm_11   = (imm >> 11) & 0x1    # shift to the right by 11, gets 1 bit
    imm_10_5 = (imm >> 5)  & 0x3F   # shift to the right by 05, gets 6 bit (0x3F = 111111)
    imm_4_1  = (imm >> 1)  & 0xF    # shift to the right by 01, gets 4 bit (0xF = 1111)
    
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