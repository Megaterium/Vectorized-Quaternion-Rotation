import quaternion as quat
import numpy as np

def rotate_vect(angles,vect,axis):
    '''
    Rotate an array of vectors useng Quaternions
    params:
    angles = array of angles that will be used for rotation
    vect   = array of vectors that will be rotated
    axis   = array of vectors that will be used as rotation axis
    
    returns:
    
    v_prime = array of rotated vectors
    
    '''
    assert vect.shape == axis.shape
    #angles = np.array(angles).reshape(3,1) # for broadcast
    theta  = np.radians(angles) # turn to radians
    #theta   = angles
    if len(vect.shape) == 3:
        vector_zeros = np.zeros((vect.shape[0],vect.shape[1],1)) 
        axis_zeros   = np.zeros((axis.shape[0],axis.shape[1],1))
        ax = 2
    elif len(vect.shape) == 2:
        vector_zeros = np.zeros((vect.shape[0],1))
        axis_zeros   = np.zeros((axis.shape[0],1))
        ax = 2
    else:
        raise ValueError('Vector Dimensions must be rank 2 or 3. Got',len(vect.shape))
        
    vector = np.array(np.concatenate([vector_zeros,vect],range(len(vect.shape))[-1])) # Prepare vector for quaternian
    rot_axis = np.array(np.concatenate([axis_zeros,axis],range(len(vect.shape))[-1])) # Prepare axis for quaternian

    # Determining vector prime using quaternians
    axis_angle = np.multiply((theta*0.5),np.divide(rot_axis,np.linalg.norm(rot_axis,axis=ax,keepdims=True)))
    vec = quat.as_quat_array(vector)
    qlog = quat.as_quat_array(axis_angle)
    q = np.exp(qlog)
    v_prime = q * vec * np.conjugate(q)
    v_prime = quat.as_float_array(v_prime)[:,:,1:] # Discard the real part and return the rotated vector
    return v_prime
