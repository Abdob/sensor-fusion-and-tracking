# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        self.dt = params.dt
        self.dim_state = params.dim_state
        self.q = params.q

    def F(self):
        # system matrix
        dt = self.dt
        return np.matrix([[1, 0, 0, dt, 0, 0],
                        [0, 1, 0, 0, dt, 0],
                        [0, 0, 1, 0, 0, dt],
                        [0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1]])
        

    def Q(self):
        # process noise covariance Q
        q = self.q
        dt = self.dt
        q1 = ((dt**3)/3) * q 
        q2 = ((dt**2)/2) * q 
        q3 = dt * q 
        return np.matrix([[q1, 0, 0, q2, 0, 0],
                        [0, q1, 0, 0, q2, 0],
                        [0, 0, q1, 0, 0 , q2],
                        [q2, 0, 0, q3, 0, 0],
                        [0, q2, 0, 0, q3, 0],
                        [0, 0, q2, 0, 0, q3]])

    def predict(self, track):
        ############
        # Predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        # predict state and estimation error covariance to next timestep
        F = self.F()
        x = F*track.x # state prediction
        P = F*track.P*F.transpose() + self.Q() # covariance prediction
        track.set_x(x)
        track.set_P(P)

    def update(self, track, meas):
        ############
        # Update state x and covariance P with associated measurement, save x and P in track
        ############
        # measurement matrix
        H = meas.sensor.get_H(track.x)
        # residual
        gamma = self.gamma(track, meas)
        # covariance of residual
        S = self.S(track, meas, meas.sensor.get_H(track.x)) 
        # kalman gain
        K = track.P * H.transpose() * S.I #P*H.transpose()*np.linalg.inv(S)
        # state update
        x = track.x + (K * gamma) #x + K*gamma
        # identity 
        I = np.identity(self.dim_state)
        # covariance update
        P = (I - K*H) * track.P
        track.set_P(P)
        track.set_x(x)
    
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # calculate and return residual gamma
        ############
        # z - H*x
        g = meas.z - meas.sensor.get_hx(track.x)
        return g
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # calculate and return covariance of residual S
        ############
        # H*P*H.transpose() + R
        result = H * track.P * H.transpose() + meas.R
        return result
        
        ############
        # END student code
        ############ 