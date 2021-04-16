package frc.robot.sim;

import edu.wpi.first.hal.SimDevice;
import edu.wpi.first.hal.SimDouble;
import edu.wpi.first.wpilibj.simulation.SimDeviceSim;

public class PretendDeviceSim {
    
    private final SimDouble m_leftVelMPS, m_rightVelMPS;

    public PretendDeviceSim() {
        SimDeviceSim wrappedSimDevice = new SimDeviceSim("PretendDevice");
        m_leftVelMPS = wrappedSimDevice.getDouble("left_vel_mps");
        m_rightVelMPS = wrappedSimDevice.getDouble("right_vel_mps");
    }
    
    public void setLeftVel(double v) {
        m_leftVelMPS.set(v);
    }

    public void setRightVel(double v) {
        m_rightVelMPS.set(v);
    }

    
}
