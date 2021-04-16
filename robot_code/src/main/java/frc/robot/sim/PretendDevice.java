package frc.robot.sim;

import edu.wpi.first.hal.SimDevice;
import edu.wpi.first.hal.SimDouble;

public class PretendDevice {
    
    private SimDevice m_SimDevice;
    private SimDouble m_leftVelMPS, m_rightVelMPS;

    public PretendDevice() {
        m_SimDevice = SimDevice.create("PretendDevice");
        m_leftVelMPS = m_SimDevice.createDouble("left_vel_mps", SimDevice.Direction.kInput, 0);
        m_rightVelMPS = m_SimDevice.createDouble("right_vel_mps", SimDevice.Direction.kInput, 0);
    }

    // public double getData() {
    //     return m_leftVelMPS.get();
    // }
}
