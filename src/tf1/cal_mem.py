import sys 
import numpy as np
import parameters.parameters2_1 as pm
from prettytable import PrettyTable

###FLOPs
def conv(input, output, kernel, if_bias=0):
    if if_bias == -1:
        ## calculation
        c = (input[2]*2*kernel[0]*kernel[1])*output[0]*output[1]*output[2]
        p = input[2]*(kernel[0]*kernel[1]+1)*output[2] + 2*output[2]
    else:
        ## calculation 
        c = (input[2]*2*kernel[0]*kernel[1]-1)*output[0]*output[1]*output[2]
        ##parameters
        p = input[2]*kernel[0]*kernel[1]*output[2] + 3*output[2]
    p = p*4/(1024*1024)
    return c, p

def full_connection(input_neuron, output_neuron, if_bias=1):
    if if_bias:
        ## calculation
        c = 2*input_neuron*output_neuron
        ## parameters
        p = input_neuron*output_neuron + output_neuron
    else:
        ##calculation
        c = (2*input_neuron-1)*output_neuron
        ## parameters
        p = input_neuron*output_neuron
    p = p*4/(1024*1024)
    return c, p

def depthwise_conv(input, output, kernel):
    ## calculation
    c = (input[2]*2*kernel[0]*kernel[1]-1)*output[0]*output[1]
    ##parameters
    p = input[2]*kernel[0]*kernel[1] + 2*output[2]
    p = p*4/(1024*1024)
    return c, p

def pointwise_conv(input, output, kernel):
    ##calculation
    c = input[2]*2*output[0]*output[1]*output[2]
    ##parameters
    p = input[2]*output[2] + 2*output[2]
    p = p*4/(1024*1024)
    return c, p

def stack(i, o, k, input, output, kernel):
    i.append(input)
    o.append(output)
    k.append(kernel)
    return i, o, k

def get_graph(input, t, channel, s):
    i = []
    o = []
    k = []

    if t != 1:
        output_channel = input[-1]*t
        output = [input[0], input[1], output_channel]
        kernel = [1,1,output_channel]
        i, o, k = stack(i, o, k, input, output, kernel)

        input = output
    else:
        i.append([0,0,0])
        o.append([0,0,0])
        k.append([0,0,0])
    output_size1 = int(input[0]/s)
    output_size2 =int(input[1]/s)
    output = [output_size1, output_size2, input[-1]]
    kernel = [3,3,input[-1]]
    i, o, k = stack(i, o, k, input, output, kernel)

    input = output
    output = [input[0], input[1], channel]
    kernel = [1,1,channel]
    i, o, k = stack(i, o, k, input, output, kernel)

    return i, o, k

def bneck(input, t, channel, n ,s, c, p, table, index):
    for i in range(n):
        if s != 1 and i != 0:
            s = 1
        input, output, kernel = get_graph(input, t, channel, s)
        if t != 1:
            c1, p1 = pointwise_conv(input[0], output[0], kernel[0])
        else:
            c1 = 0
            p1 = 0
        c2, p2 = depthwise_conv(input[1], output[1], kernel[1]) 
        c3, p3 = pointwise_conv(input[2], output[2], kernel[2])
        c_temp = c1 + c2 + c3
        p_temp = p1 + p2 + p3
        Layer1 = 'bneck'+str(index)+'/conv' +str(i+1)+'_1'
        Layer2 = 'bneck'+str(index)+'/d_conv' +str(i+1)+'_1'
        Layer3 = 'bneck'+str(index)+'/conv'+str(i+1)+'_2'
        table.add_row([Layer1, ''.join(str(input[0]).strip()), ''.join(str(kernel[0]).strip()), ''.join(str(output[0]).strip()), 1, p1, c1])
        table.add_row([Layer2, ''.join(str(input[1]).strip()), ''.join(str(kernel[1]).strip()), ''.join(str(output[1]).strip()), s, p2, c2])
        table.add_row([Layer3, ''.join(str(input[2]).strip()), ''.join(str(kernel[2]).strip()), ''.join(str(output[2]).strip()), 1, p3, c3])
        (c1, c2, c3, p1, p2, p3) = (0, 0, 0, 0, 0, 0)
        c.append(c_temp)
        p.append(p_temp)
        input = output[2]
    return c, p, output[2], table

def conv2d(input, kernel_channel, kernel_size0, kernel_size1, c, p, table, index, stride=1, if_bias=0):
    output = [int(input[0]/stride), int(input[1]/stride), kernel_channel]
    kernel = [kernel_size0, kernel_size1, kernel_channel]
    c_temp, p_temp = conv(input, output, kernel, if_bias)
    c.append(c_temp)
    p.append(p_temp)
    Layer = 'conv'+str(index)
    table.add_row([Layer, ''.join(str(input).strip()), ''.join(str(kernel).strip()), ''.join(str(output).strip()), stride, p_temp, c_temp])
    return c, p, output, table

def full_connection_op(input, output, if_bias, c, p, table, index):
    c_temp, p_temp = full_connection(input, output, if_bias)
    c.append(c_temp)
    p.append(p_temp)
    Layer = 'fc'+str(index)
    table.add_row([Layer, input, 0, output, 0, p_temp, c_temp])
    input = output
    return c, p, input, table

def main(sys):
    table = PrettyTable(['Layer','Input', 'Kernel','Output', 'Stride', 'Parameters', 'FLOPs'])
    args = pm.parse_arguments(sys)
    c = []
    p = []
    input = args.input
    (index_pool, index_conv, index_bneck, index_fc) = (1, 1, 1, 1)

    for (t, channel, n, n1, s)  in args.model_def:
        if t==1 and channel == 1:
            output0 = int(((input[0]-n)/s) + 1)
            output1 = int(((input[1]-n1)/s) + 1)
            output = [output0,output1,input[-1]]
            Layer = 'Pool'+str(index_pool)
            kernel = [n, n1]
            table.add_row([Layer, ''.join(str(input).strip()), ''.join(str(kernel).strip()), ''.join(str(output).strip()), s, 0, 0])
            input = output
            index_pool += 1
        elif t == -2:
            if type(input) != int:
                input = input[0]*input[1]*input[2]
            if_bias = channel
            output = n
            c, p, input,  table = full_connection_op(input, output, if_bias, c, p, table, index_fc)
            index_fc += 1
        elif (t == 0 or t == -1) and channel != 1:
            (kernel0, kernel1, if_bias) = (n, n1, t)
            c, p, input, table = conv2d(input, channel, kernel0, kernel1, c, p,  table, index_conv, s, if_bias)
            index_conv += 1
        else :
            c, p, input, table = bneck(input, t, channel, n, s, c, p, table, index_bneck)
            index_bneck += 1
    p =np.array(p)
    c = np.array(c)
    total_c = np.sum(c)
    total_p = np.sum(p)
    table.add_row(['Total', 0, 0, 0, 0, total_p, total_c])
    print(table)



if __name__ == '__main__':
    main(sys.argv[1:])