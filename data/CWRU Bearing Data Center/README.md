# Bearing Data Center Seeded Fault Test Data

## 1. Welcome/Overview
Welcome to [the Case Western Reserve University Bearing Data Center Website](https://engineering.case.edu/bearingdatacenter/welcome).

[This website](https://engineering.case.edu/bearingdatacenter/welcome) provides access to ball bearing test data for normal and faulty bearings.  Experiments were conducted using a 2 hp Reliance Electric motor, and acceleration data was measured at locations near to and remote from the motor bearings.  These web pages are unique in that the actual test conditions of the motor as well as the bearing fault status have been carefully documented for each experiment.

Motor bearings were seeded with faults using electro-discharge machining (EDM). Faults ranging from 0.007 inches in diameter to 0.040 inches in diameter were introduced separately at the inner raceway, rolling element (i.e. ball) and outer raceway. Faulted bearings were reinstalled into the test motor and vibration data was recorded for motor loads of 0 to 3 horsepower (motor speeds of 1797 to 1720 RPM).

## 2. Project History
Experiments are often required in order to validate new technologies, theories and techniques. These motor bearing experiments were initiated in order to characterize the performance of IQ PreAlert, a motor bearing condition assessment system developed at Rockwell. From the time of this original impetus, the experimental program has expanded to provide a motor performance database which can be used to validate and/or improve a host of motor condition assessment techniques. Some projects which have recently or are currently making use of this database include: Winsnode condition assessment technology, model based diagnostic techniques, and motor speed determination algorithms.

## 3. Apparatus & Procedures
<div align=center>
<img src="https://cdn.jsdelivr.net/gh/Tian-hy/Note-Images@main/images/test-stand.png"\>
</div>

As shown in **Figure** above, the test stand consists of a 2 hp motor (left), a torque transducer/encoder (center), a dynamometer (right), and control electronics (not shown). The test bearings support the motor shaft. Single point faults were introduced to the test bearings using electro-discharge machining with fault diameters of 7 mils, 14 mils, 21 mils, 28 mils, and 40 mils (1 mil=0.001 inches). See **[FAULT SPECIFICATIONS](https://engineering.case.edu/bearingdatacenter/fault-specifications)** for fault depths. SKF bearings were used for the 7, 14 and 21 mils diameter faults, and NTN equivalent bearings were used for the 28 mil and 40 mil faults. Drive end and fan end bearing specifications, including bearing geometry and defect frequencies are listed in the **[BEARING SPECIFICATIONS](https://engineering.case.edu/bearingdatacenter/bearing-information)**.

Vibration data was collected using accelerometers, which were attached to the housing with magnetic bases. Accelerometers were placed at the 12 o’clock position at both the drive end and fan end of the motor housing. During some experiments, an accelerometer was attached to the motor supporting base plate as well. Vibration signals were collected using a 16 channel DAT recorder, and were post processed in a Matlab environment. All data files are in Matlab (*.mat) format. Digital data was collected at 12,000 samples per second, and data was also collected at 48,000 samples per second for drive end bearing faults. Speed and horsepower data were collected using the torque transducer/encoder and were recorded by hand.

Outer raceway faults are stationary faults, therefore placement of the fault relative to the load zone of the bearing has a direct impact on the vibration response of the motor/bearing system. In order to quantify this effect, experiments were conducted for both fan and drive end bearings with outer raceway faults located at 3 o’clock (directly in the load zone), at 6 o’clock (orthogonal to the load zone), and at 12 o’clock

## 4. Download a Data File
  
Data was collected for normal bearings, single-point drive end and fan end defects.  Data was collected at 12,000 samples/second and at 48,000 samples/second for drive end bearing experiments.  All fan end bearing data was collected at 12,000 samples/second.  

Data files are in **Matlab** format.  Each file contains fan and drive end vibration data as well as motor rotational speed.  For all files, the following item in the variable name indicates:

DE - drive end accelerometer data  
FE - fan end accelerometer data  
BA - base accelerometer data  
time - time series data  
RPM - rpm during testing

Click on a link below to continue:

[Normal Baseline Data](https://engineering.case.edu/bearingdatacenter/normal-baseline-data)

[12k Drive End Bearing Fault Data](https://engineering.case.edu/bearingdatacenter/12k-drive-end-bearing-fault-data)

[48k Drive End Bearing Fault Data](https://engineering.case.edu/bearingdatacenter/48k-drive-end-bearing-fault-data)

[Fan-End Bearing Fault Data](https://engineering.case.edu/bearingdatacenter/12k-fan-end-bearing-fault-data)


## Appendix

### Fault Specifications

| Bearing   | Fault Location | Diameter | Depth | Bearing Manufacturer |
|:-----------:|:----------------:|:----------:|:-------:|:----------------------:|
| Drive End | Inner Raceway  | 0.007    | 0.011 | SKF                  |
| Drive End | Inner Raceway  | 0.014    | 0.011 | SKF                  |
| Drive End | Inner Raceway  | 0.021    | 0.011 | SKF                  |
| Drive End | Inner Raceway  | 0.028    | 0.05  | NTN                  |
| Drive End | Outer Raceway  | 0.007    | 0.011 | SKF                  |
| Drive End | Outer Raceway  | 0.014    | 0.011 | SKF                  |
| Drive End | Outer Raceway  | 0.021    | 0.011 | SKF                  |
| Drive End | Outer Raceway  | 0.04     | 0.05  | NTN                  |
| Drive End | Ball           | 0.007    | 0.011 | SKF                  |
| Drive End | Ball           | 0.014    | 0.011 | SKF                  |
| Drive End | Ball           | 0.021    | 0.011 | SKF                  |
| Drive End | Ball           | 0.028    | 0.15  | NTN                  |
| Fan End   | Inner Raceway  | 0.007    | 0.011 | SKF                  |
| Fan End   | Inner Raceway  | 0.014    | 0.011 | SKF                  |
| Fan End   | Inner Raceway  | 0.021    | 0.011 | SKF                  |
| Fan End   | Outer Raceway  | 0.007    | 0.011 | SKF                  |
| Fan End   | Outer Raceway  | 0.014    | 0.011 | SKF                  |
| Fan End   | Outer Raceway  | 0.021    | 0.011 | SKF                  |
| Fan End   | Ball           | 0.007    | 0.011 | SKF                  |
| Fan End   | Ball           | 0.014    | 0.011 | SKF                  |
| Fan End   | Ball           | 0.021    | 0.011 | SKF                  |
(All dimensions in inches)

### Bearing Information
**Drive end bearing**: 6205-2RS JEM SKF, deep groove ball bearing

**Size**: (inches)
| Inside Diameter | Outside Diameter | Thickness | Ball Diameter | Pitch Diameter |
|:---------------:|:----------------:|:---------:|:-------------:|:--------------:|
|     0.9843      |      2.0472      |  0.5906   |    0.3126     |     1.537      |

**Defect frequencies**: (multiple of running speed **in Hz**)
| Inner Ring | Outer Ring | Cage Train | Rolling Element |
|:----------:|:----------:|:----------:|:---------------:|
|   5.4152   |   3.5848   |  0.39828   |     4.7135      |

***
**Fan end bearing**: 6203-2RS JEM SKF, deep groove ball bearing

**Size**: (inches)
| Inside Diameter | Outside Diameter | Thickness | Ball Diameter | Pitch Diameter |
|:---------------:|:----------------:|:---------:|:-------------:|:--------------:|
|     0.6693      |      1.5748      |  0.4724   |    0.2656     |     1.122      |

**Defect frequencies**: (multiple of running speed **in Hz**)
| Inner Ring | Outer Ring | Cage Train | Rolling Element |
|:----------:|:----------:|:----------:|:---------------:|
|   4.9469   |   3.0530   |   0.3817   |     3.9874      |
