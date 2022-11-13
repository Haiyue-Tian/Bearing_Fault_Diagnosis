clc
clear

global Train_Counter
global Test_Counter
Train_Counter = 1 ;
Test_Counter = 1;
classes = {'Outer_Race/', ...
           'Inner_Race/', ...
           'Ball/', ...
           'Normal/'};
savePath = '../../../data/overlap_sampling_picked_data/' ;
strides = [150, 100, 100, 50];
for clsIdx = 1:4
    cls = string(classes(clsIdx));
    path = strcat('../../../data/picked_data/', cls) ;
    files = dir(strcat(path,'*.mat'));
    number_files = length(files) ;

    trainSavePath = strcat(savePath, 'train/', cls) ;
    testSavePath = strcat(savePath, 'test/', cls) ;

    stride = strides(clsIdx);
    len = 512 ;


    for idx = 1:number_files
        data = strcat(path,files(idx).name) ;
        load(data);
        num_name = strrep(files(idx).name,'.mat','') ;
        files(idx).Name = str2num(num_name) ;
        if size(num_name,2) == 1
            num_name = ['00', num_name] ;
        elseif size(num_name,2) == 2
            num_name = ['0', num_name] ;
        else
            num_name = num_name ;
        end
        S = ['X', num_name] ;
        E = ['_','time'] ;
        M = char( '_DE','_FE');
        for j = 1:2
            if j == 1 
                Variable = [S,M(j,:),E] ;
                temp=subs(Variable) ;
                temp = double(temp) ;
                temp = temp' ;
                [trainS, testS] = ThreeSeven(temp) ;
                train_DE = overlap(trainS, len, stride) ;
                test_DE = overlap(testS, len, stride) ;
                clear trainS testS
                clear Variable temp
            else
                Variable = [S,M(j,:),E] ;
                temp=subs(Variable) ;
                temp = double(temp) ;
                temp = temp' ;
                [trainS, testS] = ThreeSeven(temp) ;
                train_FE = overlap(trainS, len, stride) ;
                test_FE = overlap(testS, len, stride) ;
                clear trainS testS
                clear Variable temp
            end
        end
        Train(:,:,1) = train_DE ;
        Train(:,:,2) = train_FE ;
        Test(:,:,1) = test_DE ;
        Test(:,:,2) = test_FE ;

        SaveSample(trainSavePath, Train, 1)
        SaveSample(testSavePath, Test, 0)
        clear Variable 
        clear train_DE train_FE test_DE test_FE
        clear Train Test
    end
end
