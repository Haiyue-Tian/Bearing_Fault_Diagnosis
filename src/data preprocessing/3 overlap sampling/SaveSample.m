function SaveSample(Path, Sample,iftrain)

global Train_Counter
global Test_Counter

[x,y,z] = size(Sample) ;
for i = 1:x
    temp_DE = Sample(i,:,1) ;
    temp_FE = Sample(i,:,2) ;
    Data = [temp_DE; temp_FE] ;
    if iftrain == 1
        Counter = num2str(Train_Counter) ;
        Dir = strcat(Path,Counter) ;
        Train_Counter = Train_Counter + 1 ;
    else
        Counter = num2str(Test_Counter) ;
        Dir = strcat(Path,Counter) ;
        Test_Counter = Test_Counter + 1 ;
    end
    save(Dir,'Data') ;
    clear temp_DE temp_FE Data Counter Dir
end