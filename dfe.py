import numpy as np


class dfe:
    def __init__(self, dorg, datain, htaps):
        self.din = datain
        self.dorg = dorg
        # self.ekin=ekin
        self.htaps = htaps
        # self.vth=vth

    def summer(self):
        dout = self.dorg \
               - self.htaps[1][-1] * self.din[-1] \
               - self.htaps[2][-1] * self.din[-2] \
               - self.htaps[3][-1] * self.din[-3] \
               - self.htaps[4][-1] * self.din[-4] \
               - self.htaps[5][-1] * self.din[-5] \
               - self.htaps[6][-1] * self.din[-6] \
               - self.htaps[7][-1] * self.din[-7]
        # -self.htaps[8][-1]*self.din[-8]
        return dout

    def cmp(self, dsum, vth):
        self.vth = vth
        self.dsum = dsum
        cmpOut = np.sign(self.dsum - self.vth)
        return cmpOut

    def sslms(self, ekin):
        self.ekin = ekin
        delta = 16.
        vpgain=1/8
        utgain=1/8
        tapgain=1/8
        dfe_tap = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfe_tap[0] =1. / 64. * 0.64*(self.htaps[0][-1]*64/0.64/vpgain + 1. / 8 * delta * self.ekin * (
        np.sign(self.din[-1] + 2) )) *vpgain     #-1 * np.sign(self.ekin) * np.sign(self.din[-2]) + 2) / 8
        dfe_vp_dig=self.htaps[0][-1]*64/0.64
        tbout=1. / 8 * delta * self.ekin * (np.sign(self.din[-1] + 2) )
        print(dfe_vp_dig,tbout)
        dfe_tap[1] = 1./ 64. * 0.64*(self.htaps[1][-1]*64/0.64/utgain + 1. / 16 * delta * np.sign(self.ekin) * np.sign(self.din[-2]))*utgain
        dfe_tap[2] = 1./ 64. * 0.32*(self.htaps[2][-1]*64/0.32/tapgain + 1. / 32 * delta * np.sign(self.ekin) * np.sign(self.din[-3]))*tapgain
        # dfe_tap[3] = self.htaps[3][-1] + 1. / 64 * delta * np.sign(ekin) * np.sign(self.din[-4]) / 32. * 0.32
        # dfe_tap[4] = self.htaps[4][-1] + 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-5]) / 16. * 0.16
        # dfe_tap[5] = self.htaps[5][-1] + 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-6]) / 16. * 0.16
        # dfe_tap[6] = self.htaps[6][-1] + 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-7]) / 16. * 0.16
        # dfe_tap[7] = self.htaps[7][-1] + 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-8]) / 16 * 0.16
        # dfe_tap[8]=self.htaps[8][-1]+1./128*delta*np.sign(ekin)*np.sign(self.din[-9])/128.*0.48
        return dfe_tap


    def msgd(self, ekin, vtaps):
        self.ekin = ekin
        self.vtaps = vtaps

        delta = 16.
        v_tap = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        #vntap = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # v_tap[0] = self.vtaps[0][-1] + 1. / 8 * delta * self.ekin / 128. * 0.64 * (
        #     -1 * np.sign(self.ekin) * np.sign(self.din[-2]) + 2) / 8
        v_tap[0] = 1./ 64. * 0.64*(self.vtaps[0][-1]*64/0.64 + 1. / 8 * delta * self.ekin  * (
            np.sign(self.din[-2] + 1) ))/8
        #print(self.vtaps[0][-1],v_tap[0])


        v_tap[1] = 0.5*self.vtaps[1][-1] - 1. / 16 * delta * np.sign(self.ekin) * np.sign(self.din[-2]) / 64. * 0.64

        v_tap[2] = 0.5*self.vtaps[2][-1] - 1. / 32 * delta * np.sign(self.ekin) * np.sign(self.din[-3]) / 64. * 0.32
        v_tap[3] = 0.5*self.vtaps[3][-1] - 1. / 64 * delta * np.sign(ekin) * np.sign(self.din[-4]) / 64. * 0.16
        v_tap[4] = 0.5*self.vtaps[4][-1] - 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-5]) / 64. * 0.16
        v_tap[5] = 0.5*self.vtaps[5][-1] - 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-6]) / 64. * 0.16
        v_tap[6] = 0.5*self.vtaps[6][-1] - 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-7]) / 64. * 0.16
        v_tap[7] = 0.5*self.vtaps[7][-1] - 1. / 128 * delta * np.sign(ekin) * np.sign(self.din[-8]) / 64 * 0.16
        # v_tap[8]=self.htaps[8][-1]+1./128*delta*np.sign(ekin)*np.sign(self.din[-9])/64.*0.64

        #print(v_tap)
        return v_tap
