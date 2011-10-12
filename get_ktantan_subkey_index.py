#!/usr/bin/env python

IR_state = [1] * 8

def gen_ir():
    global IR_state
    tmp = IR_state.pop()
    IR_state.insert(0, tmp ^ IR_state[6] ^ IR_state[4] ^ IR_state[2])
    return IR_state[7]


def get_keys():
    T_7654 = (IR_state[7] << 3) | (IR_state[6] << 2) | (IR_state[5] << 1) | IR_state[4]
    T_10 = (IR_state[1] << 1) | IR_state[0]
    a = [0] * 5
    for i in range(5):
        a[i] = T_7654 + 16 * i
    
    if IR_state[3] == 0 and IR_state[2] == 0:
        k_a = a[0]
    else:
        k_a = a[T_10 + 1]
    
    if IR_state[3] == 0 and IR_state[2] == 1:
        k_b = a[4]
    else:
        k_b = a[0b11 - T_10]
        
    return (k_a, k_b)
     

if __name__ == '__main__':
    IR = []
    K_A = []
    K_B = []
    for i in range(254):
	IR.append(gen_ir())
        (k_a, k_b) = get_keys()
        K_A.append(k_a)
        K_B.append(k_b)
        
    
    print 'IR'
    for round in range(254):
        print '%d, ' % IR[round],
        if round % 16 == 15:
            print
    print
    
    print
    print 'k_a'
    for round in range(254):
        print '%2d, ' % K_A[round],
        if round % 16 == 15:
            print
    print

    print
    print 'k_b'
    for round in range(254):      
        print '%2d, ' % K_B[round],
        if round % 16 == 15:
            print
    print
