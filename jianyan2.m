data=[
0.10 11.1 0.80 34.2 1.5 44.4 3.53 61.1 15.0 106.5
0.24 19.9 0.94 36.3 1.65 46.0 3.80 62.9 25.0 130.0
0.38 25.4 1.08 38.9 1.79 46.9 4.07 64.3 34.0 145.0
0.52 28.8 1.22 41.0 1.93 48.7 4.34 65.6 53.0 175.0
0.66 31.9 1.36 42.8 3.26 59.0 4.61 67.3 62.0 185.0
];
t=[];r=[];
for i=1:5
t=[t;data(:,2*i-1)];
r=[r;data(:,2*i)];
end
r1=log(r);t1=log(t);
s=polyfit(t1,r1,1);b=s(1);a=s(2);
tt=0:0.1:70;rr=exp(a)*tt.^b;
plot(tt,rr,t,r,'+')