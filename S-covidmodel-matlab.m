>> ts=1;
>> nsim=30;
>> a=0.75;
>> gama=0.4;
>> S=0.8; I=0.1; R=0.0;
>> for kk=1:nsim
SOLD=S;
IOLD=I;
ROLD=R;

s1(kk)=S;
I1(kk)=I;
R1(kk)=R;
D(kk)=10.0e+6*R*0,01; %number of deaths
R0(kk)=S*a/gama;

S=SOLD-a*SOLD*IOLD;
I=IOLD+a*SOLD*IOLD-gama*IOLD;
R=ROLD+gama*IOLD;
end
>> figure
>> k=0:(nsim-1);
>> figure
>> subplot(231)
>> stairs(k*ts,s1,'g')
>> legend('ΕΥΠΑΘΕΙΣ')
>> grid
>> subplot(232)
>> stairs(k*ts,I1,'g')
>> legend('ΜΟΛΥΣΜΕΝΟΙ')
>> grid
>> subplot(233)
>> stairs(k*ts,R1,'g')
>> legend('ΔΙΕΓΡΑΜΜΕΝΟΙ')
>> grid
>> subplot(234)
>> stairs(k*ts,R0,'g')
>> legend('R0')
>> grid
