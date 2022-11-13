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

### 1. Fault Specifications

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

### 2. Bearing Information
* **Drive end bearing**: 6205-2RS JEM SKF, deep groove ball bearing

  **Size**: (inches)
  | Inside Diameter | Outside Diameter | Thickness | Ball Diameter | Pitch Diameter |
  |:---------------:|:----------------:|:---------:|:-------------:|:--------------:|
  |     0.9843      |      2.0472      |  0.5906   |    0.3126     |     1.537      |

  **Defect frequencies**: (multiple of running speed **in Hz**)
  | Inner Ring | Outer Ring | Cage Train | Rolling Element |
  |:----------:|:----------:|:----------:|:---------------:|
  |   5.4152   |   3.5848   |  0.39828   |     4.7135      |


* **Fan end bearing**: 6203-2RS JEM SKF, deep groove ball bearing

  **Size**: (inches)
  | Inside Diameter | Outside Diameter | Thickness | Ball Diameter | Pitch Diameter |
  |:---------------:|:----------------:|:---------:|:-------------:|:--------------:|
  |     0.6693      |      1.5748      |  0.4724   |    0.2656     |     1.122      |

  **Defect frequencies**: (multiple of running speed **in Hz**)
  | Inner Ring | Outer Ring | Cage Train | Rolling Element |
  |:----------:|:----------:|:----------:|:---------------:|
  |   4.9469   |   3.0530   |   0.3817   |     3.9874      |

### 3. Data Exist or Not

  <table width="1503" border="0" cellpadding="0" cellspacing="0" style="width:1127.25pt;border-collapse:collapse;table-layout:fixed;">
   <colgroup><col width="142" class="xl65" style="mso-width-source:userset;mso-width-alt:4038;">
   <col width="80" span="5" class="xl65" style="mso-width-source:userset;mso-width-alt:2275;">
   <col width="81" style="width:60.75pt;">
   <col width="80" span="11" class="xl65" style="mso-width-source:userset;mso-width-alt:2275;">
   </colgroup><tbody><tr height="20" style="height:15.00pt;">
    <td class="xl66" height="20" width="142" style="height:15.00pt;width:106.50pt;"></td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">Name</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">DE</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">FE</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">BA</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">RPM</td>
    <td class="xl66" width="81" style="width:60.75pt;"></td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">Name</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">DE</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">FE</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">BA</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">RPM</td>
    <td class="xl66" width="80" style="width:60.00pt;"></td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">Name</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">DE</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">FE</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">BA</td>
    <td class="xl67" width="80" style="width:60.00pt;" x:str="">RPM</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl67" height="80" rowspan="4" style="height:60.00pt;border-right:none;border-bottom:none;" x:str="">Normal</td>
    <td class="xl66" x:num="">100</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl68" rowspan="45" style="border-right:none;border-bottom:none;" x:str="">12k Fan End Bearing Fault Data</td>
    <td class="xl66" x:num="">270</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl68" rowspan="52" style="border-right:none;border-bottom:none;" x:str="">48k Drive End Bearing Fault Data</td>
    <td class="xl66" x:num="">109</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">97</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">271</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">110</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">98</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">272</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">111</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">99</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">273</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">112</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl68" height="1200" rowspan="60" style="height:900.00pt;border-right:none;border-bottom:none;" x:str="">12k Drive End Bearing Fault Data</td>
    <td class="xl66" x:num="">105</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">274</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">122</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">106</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">275</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">123</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">107</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">276</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">124</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">108</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">277</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">125</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">118</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">278</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">135</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">119</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">279</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">136</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">120</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">280</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">137</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">121</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">281</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">138</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">130</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">282</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">148</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">131</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">283</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">149</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">132</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">284</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">150</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">133</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">285</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">151</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">144</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">286</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">161</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">145</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">287</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">162</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">146</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">288</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">163</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">147</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">289</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">164</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">156</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">290</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">174</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">158</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">291</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">175</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">159</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">292</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">176</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">160</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">293</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">177</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">169</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">294</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">189</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">170</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">295</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">190</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">171</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">296</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">191</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">172</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">297</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">192</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">185</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">298</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">201</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">186</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">299</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">202</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">187</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">300</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">203</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">188</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">301</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">204</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">197</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">302</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">213</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">198</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">305</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">214</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">199</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">306</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">215</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">200</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">307</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">217</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">209</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">309</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">226</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">210</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">310</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">227</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">211</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">311</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">228</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">212</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">312</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">229</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">222</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">313</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">238</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">223</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">315</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">239</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">224</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">316</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">240</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">225</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">317</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">241</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">234</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">318</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">250</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">235</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="5" style="mso-ignore:colspan;"></td>
    <td class="xl66" x:num="">251</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">236</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="5" style="mso-ignore:colspan;"></td>
    <td class="xl66" x:num="">252</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">237</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="5" style="mso-ignore:colspan;"></td>
    <td class="xl66" x:num="">253</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">246</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="5" style="mso-ignore:colspan;"></td>
    <td class="xl66" x:num="">262</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">247</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="5" style="mso-ignore:colspan;"></td>
    <td class="xl66" x:num="">263</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">248</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="5" style="mso-ignore:colspan;"></td>
    <td class="xl66" x:num="">264</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">249</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="5" style="mso-ignore:colspan;"></td>
    <td class="xl66" x:num="">265</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" x:num="">1</td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">258</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">259</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">260</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">261</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3001</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3002</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3003</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3004</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3005</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3006</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3007</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <tr height="20" style="height:15.00pt;">
    <td class="xl66" x:num="">3008</td>
    <td class="xl66" x:num="">1</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl66" style="mso-ignore:style;mso-pattern:auto none;background:#FFC7CE;color:#9C0006;" x:num="">0</td>
    <td class="xl70"></td>
    <td class="xl66" colspan="11" style="mso-ignore:colspan;"></td>
   </tr>
   <!--[if supportMisalignedColumns]-->
    <tr width="0" style="display:none;">
     <td width="142" style="width:107;"></td>
     <td width="80" style="width:60;"></td>
     <td width="80" style="width:60;"></td>
    </tr>
   <!--[endif]-->
  </tbody></table>
