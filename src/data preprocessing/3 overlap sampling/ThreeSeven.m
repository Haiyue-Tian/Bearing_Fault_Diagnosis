function [train, test] = ThreeSeven(Sample)

SampleSize = size(Sample,2) ; 
bound = round(0.7*SampleSize) ;
train = Sample(1:bound) ;
test = Sample(bound:SampleSize) ;