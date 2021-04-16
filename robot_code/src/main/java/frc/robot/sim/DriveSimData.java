// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot.sim;

import edu.wpi.first.hal.SimDevice;
import edu.wpi.first.hal.SimDouble;
import edu.wpi.first.wpilibj.simulation.SimDeviceSim;

/** Add your docs here. */
public class DriveSimData {

    private final SimDouble m_leftVelMPS, m_rightVelMPS;

    public DriveSimData() {
        DriveData d = new DriveData();
        SimDeviceSim wrappedSimDevice = new SimDeviceSim("DriveData");
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

class DriveData {

    private SimDevice m_SimDevice;
    // private SimDouble m_leftVelMPS, m_rightVelMPS;

    public DriveData() {
        m_SimDevice = SimDevice.create("DriveData");
        // m_leftVelMPS = m_SimDevice.createDouble("left_vel_mps", SimDevice.Direction.kInput, 0);
        // m_rightVelMPS = m_SimDevice.createDouble("right_vel_mps", SimDevice.Direction.kInput, 0);
        m_SimDevice.createDouble("left_vel_mps", SimDevice.Direction.kInput, 0);
        m_SimDevice.createDouble("right_vel_mps", SimDevice.Direction.kInput, 0);
    }
}
