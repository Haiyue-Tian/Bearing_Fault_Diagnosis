function RS = overlap(Sample, Length, Stride)

SampleSize = size(Sample,2) ;
Total = floor((SampleSize - Length)/Stride + 1);
RS = zeros([Total,Length]) ;
StartCounter = 1 ;
TempL = Length - 1 ;

for ii = 1:Total 
    RS(ii,:) = Sample(StartCounter:StartCounter+TempL) ;
    StartCounter = StartCounter + Stride ;
end