% check variable data after run

clc
clear
s = struct;
s.names = "";
s.files = struct;
data = repmat(s, 1, 4);
directory = {'48k Drive End Bearing Fault Data', ...
             '12k Drive End Bearing Fault Data', ...
             '12k Fan End Bearing Fault Data', ...
             'Normal Baseline Data'};
for idxDir = 1:4
    d = string(directory(idxDir));
    path = '../../../data/CWRU Bearing Data Center/' ;
    files = dir(strcat(path, d, '/*.mat'));
    number_files = length(files) ;

    files = rmfield(files,'folder') ;
    files = rmfield(files,'date') ;
    files = rmfield(files,'bytes') ;
    files = rmfield(files,'isdir') ;
    files = rmfield(files,'datenum') ;

    for idx = 1:number_files
        dataPath = strcat(path, d, '/', files(idx).name) ;
        load(dataPath);
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
        M = char( '_DE','_FE', '_BA');
        for j = 1:4
            if j == 1 
                Variable = [S,M(j,:),E] ;
                files(idx).DE = exist(Variable) ;
                clear Variable
            elseif j == 2
                Variable = [S,M(j,:),E] ;
                files(idx).FE = exist(Variable) ;
                clear Variable
            elseif j == 3 
                Variable = [S,M(j,:),E] ;
                files(idx).BA = exist(Variable) ;
                clear Variable
            else
                Variable = [S,'RPM'] ;
                files(idx).RPM = exist(Variable) ;
                clear Variable
            end
        end
        clear Variable
    end
    data(idxDir).files = rmfield(files,'name') ;
    data(idxDir).names = d ;
end
clearvars -except data