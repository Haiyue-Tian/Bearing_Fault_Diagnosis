import shutil

dir = {'from': '../../../data/CWRU Bearing Data Center/',
       'to': '../../../data/picked_data/'}
pos = ['12k Drive End Bearing Fault Data/', 
       '12k Fan End Bearing Fault Data/',
       'Normal Baseline Data/']
posCls = ['DE_Innr', 'DE_Ball', 'DE_Outr', 
           'FE_Innr', 'FE_Ball', 'FE_Outr', 'Normal']
cls = ['Inner_Race/', 'Ball/', 'Outer_Race/', 'Normal/']
pickedData = \
    {'DE_Innr': [str(j + i)+'.mat' for j in [105, 169, 209] for i in range(4)],
     'DE_Ball': [str(j + i)+'.mat' for j in [118, 185, 222] for i in range(4)],
     'DE_Outr': [str(j + i)+'.mat' for j in [130, 197, 234, 144, 246, 157, 258] for i in range(4)],
     'FE_Innr': [str(270 + i)+'.mat' for i in range(12)],
     'FE_Ball': [str(282 + i)+'.mat' for i in range(12)],
     'FE_Outr': [str(294 + i)+'.mat' for i in range(25)],
     'Normal': [str(97 + i) + '.mat' for i in range(4)]}
pickedData['DE_Outr'].remove('157.mat')
pickedData['DE_Outr'].append('156.mat')
remove = ['303.mat', '304.mat', '308.mat', '314.mat'] 
for r in remove:
    pickedData['FE_Outr'].remove(r)

for i, c in enumerate(posCls):
    for mat in pickedData[c]:
        fromDir = dir['from'] + pos[i//3] + mat
        toDir = dir['to'] + cls[i%3+(3 if i//6 else 0)] + mat
        shutil.copy(fromDir,toDir)